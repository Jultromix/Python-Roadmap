-- Show the growth of sales per coutnry from one month to the other
SELECT
	pa.NombrePais,
	YEAR(p.FechaPedido)		AS Anio,
	MONTH(p.FechaPedido)	AS Mes,
	SUM(p.Total)			AS MonthlySales,

	LAG(SUM(p.Total)) OVER(
		PARTITION BY pa.PaisID ORDER BY YEAR(p.FechaPedido), MONTH(p.FechaPedido)
	) AS PreviousMonthSales,

	SUM(p.Total) - 
	LAG(SUM(p.Total)) OVER(
		PARTITION BY pa.PaisID ORDER BY YEAR(p.FechaPedido), MONTH(p.FechaPedido)
	) AS AbsoluteDelta,

	CAST(
		(SUM(p.Total) - 
		LAG(SUM(p.Total)) OVER(
			PARTITION BY pa.PaisID ORDER BY YEAR(p.FechaPedido), MONTH(p.FechaPedido)
		)) * 100 /

		NULLIF(		--(avoids division by 0)
			LAG(SUM(p.Total)) OVER(PARTITION BY pa.PaisID ORDER BY YEAR(p.FechaPedido), MONTH(p.FechaPedido)),
			0
		) AS DECIMAL(10,2)
	)	 AS PercentualGrowth
FROM Pedidos p
INNER JOIN Clientes c ON p.ClienteID = c.ClienteID
INNER JOIN Paises pa ON c.PaisID = pa.PaisID
WHERE p.Estado = 'Completado'
GROUP BY pa.PaisID, pa.NombrePais, YEAR(p.FechaPedido), MONTH(p.FechaPedido)
ORDER BY pa.NombrePais, Anio, Mes



-- What is the accumulated value of sales per country and it's percentage against the total of sales?
SELECT
	pa.NombrePais,
	SUM(p.Total)			AS SalesPerCountry,

	SUM(SUM(p.Total)) OVER() AS TotalGlobal,
	SUM(SUM(p.Total)) OVER(ORDER BY SUM(p.Total) DESC ROWS UNBOUNDED PRECEDING) AS RankingAcc,

	CAST(
		SUM(p.Total) * 100 /
		SUM(SUM(p.Total)) OVER () AS DECIMAL(7,2) 
	) AS PercentageFromTotal
FROM Pedidos p
INNER JOIN Clientes c ON p.ClienteID = c.ClienteID
INNER JOIN Paises pa ON c.PaisID = pa.PaisID
WHERE p.Estado = 'Completado'
GROUP BY pa.PaisID, pa.NombrePais
ORDER BY SalesPerCountry

-- Rank Top 5 months with highest sales For Argentina
WITH RankMonthlySales AS (
	SELECT
		pa.NombrePais,
		YEAR(p.FechaPedido)		AS Anio,
		MONTH(p.FechaPedido)	AS Mes,
		SUM(p.Total)			AS MonthlySales,
		RANK() OVER(PARTITION BY pa.PaisID ORDER BY YEAR(p.FechaPedido),MONTH(p.FechaPedido) DESC)	AS Ranking
	FROM Pedidos p
	INNER JOIN Clientes c ON p.ClienteID = c.ClienteID
	INNER JOIN Paises pa ON c.PaisID  = pa.PaisID
	WHERE p.Estado = 'Completado'

	GROUP BY pa.PaisID, pa.NombrePais,YEAR(p.FechaPedido), MONTH(p.FechaPedido)
)

SELECT TOP 5
	NombrePais,
	Anio,
	Mes,
	MonthlySales,
	Ranking
FROM RankMonthlySales
WHERE NombrePais = 'Argentina'
ORDER BY Ranking