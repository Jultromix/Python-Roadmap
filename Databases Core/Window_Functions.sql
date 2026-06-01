-- 1) Basic example of Window Function
SELECT
	c.Nombre,
	p.PedidoID,
	p.FechaPedido,
	p.Total,
	ROW_NUMBER() OVER(PARTITION BY p.ClienteID ORDER BY p.FechaPedido)	AS OrderNum,
	RANK() OVER(PARTITION BY p.ClienteID ORDER BY p.Total DESC)			AS RankPerSale
FROM Pedidos p
INNER JOIN Clientes c ON p.ClienteID = C.ClienteID
WHERE p.Estado = 'Completado'
ORDER BY c.Nombre, p.FechaPedido


-- 2) TOP 3 Customers with more orders
WITH ProductosRankeados AS (		-- Reminder this is CTE
	SELECT
		cat.NombreCategoria,
		prod.NombreProducto,
		SUM(dp.Cantidad) AS SoldUnits,
		RANK()	OVER(PARTITION BY cat.CategoriaID ORDER BY SUM(dp.Cantidad) DESC) AS Ranking
	FROM DetallePedidos dp
	INNER JOIN Productos prod ON dp.ProductoID = dp.ProductoID
	INNER JOIN Categorias cat ON prod.CategoriaID = cat.CategoriaID
	INNER JOIN Pedidos p ON dp.PedidoID = p.PedidoID
	WHERE p.Estado = 'Completado'
	GROUP BY cat.CategoriaID, cat.NombreCategoria, prod.ProductoID, prod.NombreProducto
)

SELECT
	NombreCategoria,
	NombreProducto,
	SoldUnits,
	Ranking
FROM ProductosRankeados
WHERE Ranking <= 3
ORDER BY NombreCategoria, Ranking;

--3 Show the growth of sales per country from one month to the other
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

-- What is the accumulated value of sales per country and it's percetage agains the total of sales?
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

-- 4 Rank best 5 top 5 months with highest sales For Argentina
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