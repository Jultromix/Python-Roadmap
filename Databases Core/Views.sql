-- 1) How to create views for users lacking SQL context:
CREATE VIEW VW_SalesPerCountry AS

SELECT
	pa.NombrePais,
	YEAR(p.FechaPedido)		AS	order_year,
	MONTH(p.FechaPedido)	AS	order_month,
	COUNT(p.PedidoID)		AS	total_orders,
	SUM(p.Total)			AS	total_sales,
	AVG(p.Total)			AS	avg_sales
FROM Pedidos p
INNER JOIN Sucursales s ON p.SucursalID = s.SucursalID
INNER JOIN Paises pa	ON s.PaisID = pa.PaisID
WHERE p.Estado = 'Completado'
GROUP BY pa.NombrePais, YEAR(p.FechaPedido), MONTH(p.FechaPedido);


-- 2) Accessing the View:
SELECT * 
FROM VW_SalesPerCountry
WHERE NombrePais = 'Argentina'
ORDER BY order_year, order_month;

-- 3) Another type of query with operations:
SELECT
	NombrePais,
	SUM(total_sales)
FROM VW_SalesPerCountry
GROUP BY NombrePais;

-- 4) Editing the view
ALTER VIEW VW_SalesPerCountry AS

SELECT
	pa.CodigoPais,
	pa.NombrePais,
	YEAR(p.FechaPedido)		AS	order_year,
	MONTH(p.FechaPedido)	AS	order_month,
	COUNT(p.PedidoID)		AS	total_orders,
	SUM(p.Total)			AS	total_sales,
	AVG(p.Total)			AS	avg_sales,
	MAX(p.Total)			AS	max_sale,
	MIN(p.Total)			AS min_sale
FROM Pedidos p
INNER JOIN Sucursales s ON p.SucursalID = s.SucursalID
INNER JOIN Paises pa	ON s.PaisID = pa.PaisID
WHERE p.Estado = 'Completado'
GROUP BY pa.CodigoPais,pa.NombrePais, YEAR(p.FechaPedido), MONTH(p.FechaPedido);

-- 5) Accesing the view's info definition as a result:
EXEC sp_helptext 'VW_SalesPerCountry'


-- 6) Deletig a  View:
-- DROP VIEW IF EXISTS VW_SalesPerCountry;


-- Create Top 20 Product Sales

CREATE VIEW VW_TopProdSales AS

SELECT
	p.NombreProducto,
	SUM(dp.Cantidad * dp.PrecioUnitario)	AS	sale_by_prod
FROM DetallePedidos dp
INNER JOIN Productos p ON dp.ProductoID  = p.ProductoID
INNER JOIN Pedidos pe ON dp.PedidoID = pe.PedidoID
WHERE pe.Estado = 'Completado'
GROUP BY p.NombreProducto;

-- Create view: customers who neve bought anything
CREATE VIEW VW_ClienteSinPedido AS

SELECT
	c.ClienteID,
	c.Nombre + ' ' + c.Apellido AS cliente
FROM Pedidos p
FULL OUTER  JOIN Clientes c ON p.ClienteID = c.ClienteID
GROUP BY c.ClienteID,c.Nombre + ' ' + c.Apellido
HAVING COUNT(p.PedidoID) = 0;


-- 7) Case with an indexed View
--  7.1) Create a view with SCHEMABINDING:

CREATE VIEW VW_SalesPerCountry
WITH SCHEMABINDING AS
SELECT
	pa.NombrePais,
	YEAR(p.FechaPedido)		AS	order_year,
	MONTH(p.FechaPedido)	AS	order_month,
	COUNT_BIG(*)			AS	total_orders,
	SUM(p.Total)			AS	total_sales
FROM dbo.Pedidos p
INNER JOIN dbo.Sucursales s ON p.SucursalID = s.SucursalID
INNER JOIN dbo.Paises pa	ON s.PaisID = pa.PaisID
WHERE p.Estado = 'Completado'
GROUP BY pa.NombrePais, YEAR(p.FechaPedido), MONTH(p.FechaPedido);
GO

--  7.2) Create the unique index
CREATE UNIQUE CLUSTERED INDEX IX_VW_SalesPerCountry
ON VW_SalesPerCountry (NombrePais, order_year, order_month);
GO