-- Show me the top 3 vendors per country, and only those countries whose sales are above a certain threshold, say 100,000.
SELECT *			-- Q 2)	Display SubQ 1 by adding more filters
FROM (
	SELECT			-- SubQ 1) assign a ranking to SubQ 0
		pais, empleado, total_sales,
		RANK() OVER (PARTITION BY pais ORDER BY total_sales DESC) AS ranking
	FROM (

		SELECT		-- SubQ 0) vendors per country (from totals)
			pa.NombrePais	AS pais,
			e.Nombre		AS empleado,	
			SUM(p.Total)	AS total_sales
		FROM Pedidos p										
		INNER JOIN Empleados e	ON p.EmpleadoID = e.EmpleadoID
		INNER JOIN Sucursales s ON e.SucursalID = s.SucursalID
		INNER JOIN Paises pa	ON s.PaisID = pa.PaisID
		WHERE p.Estado = 'Completado'
		GROUP BY pa.NombrePais, e.Nombre
		 ) AS BASE
	 ) AS ranked_result
WHERE ranking <= 3
	 AND pais IN (
      SELECT pa.NombrePais
      FROM Pedidos p
      INNER JOIN Clientes c ON p.ClienteID = c.ClienteID
      INNER JOIN Paises pa  ON c.PaisID    = pa.PaisID
      WHERE p.Estado = 'Completado'
      GROUP BY pa.NombrePais
      HAVING SUM(p.Total) > 1000)
ORDER BY pais, ranking;



-- 2) Now lets get each chunk of logic
WITH
base AS (						-- Table of vendors per country
	SELECT
			pa.NombrePais	AS pais,
			e.EmpleadoID,
			e.Nombre		AS empleado,	
			SUM(p.Total)	AS total_sales
		FROM Pedidos p										
		INNER JOIN Empleados e	ON p.EmpleadoID = e.EmpleadoID
		INNER JOIN Sucursales s ON e.SucursalID = s.SucursalID
		INNER JOIN Paises pa	ON s.PaisID = pa.PaisID
		WHERE p.Estado = 'Completado'
		GROUP BY pa.NombrePais, e.EmpleadoID, e.Nombre
	),
ranked_result AS (				-- Ranked table from "base"
	SELECT			
		pais, empleado, total_sales,
		RANK() OVER (PARTITION BY pais ORDER BY total_sales DESC) AS ranking
	FROM base
	),
relevant_countries AS (			-- Sales Threshold Table
    SELECT pais
    FROM base
    GROUP BY pais
    HAVING SUM(total_sales) > 1000
)


SELECT							-- With all tables created, add filters and select the treshold
	rr.pais,
	rr.empleado,
	rr.total_sales,
	rr.ranking
FROM ranked_result rr
INNER JOIN relevant_countries rc ON rr.pais = rc.pais
WHERE rr.ranking <=3
ORDER BY rc.pais, rr.ranking;