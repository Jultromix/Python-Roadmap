-- Get index description of a table:
EXEC sp_helpindex 'Pedidos';

-- If the table has no index, you can assign it by:
	-- CREATE CLUSTERED INDEX <Index_name> ON <Table_name> (<Field_name>);
	-- CREATE NONCLUSTERED INDEX <Index_name> ON <Table_name> (<Field_name>);

SELECT *
FROM Pedidos
WHERE FechaPedido >= '2024-01-01'
	AND FechaPedido < '2024-02-01';

CREATE NONCLUSTERED INDEX IX_Pedidos_Fecha_Estado
ON Pedidos (FechaPedido, Estado)
INCLUDE (Total, ClienteID);

CREATE NONCLUSTERED INDEX IX_Pedidos_Completados_Fecha ON Pedidos (FechaPedido, Total)
INCLUDE (ClienteID, SucursalID)
WHERE Estado = 'Completado'


-- Paging
DECLARE @Pagina INT = 1;
DECLARE	@SizePagina INT = 20;

SELECT
	p.PedidoID,
	c.Nombre,
	p.FechaPedido,
	p.Total,
	p.Estado
FROM Pedidos p
INNER JOIN Clientes c ON p.ClienteID = c.ClienteID
WHERE p.Estado = 'Completado'
ORDER BY p.FechaPedido DESC

OFFSET (@Pagina - 1) * @SizePagina ROWS
FETCH NEXT @SizePagina ROWS ONLY;

SELECT CEILING(COUNT(*) * 1.0 /@SizePagina) AS TotalPages
FROM Pedidos
WHERE Estado = 'Completado'


-- Keyset pagination
SELECT TOP 20			-- First Page
	PedidoID,
	FechaPedido,
	Total
FROM Pedidos
WHERE Estado = 'Completado'
ORDER BY FechaPedido DESC,  PedidoID DESC;

-- Next page
DECLARE @LastDate DATETIME = '2024-06-15 10:30:00';
DECLARE @LastOrder INT = 4500;

SELECT TOP 20			-- First Page
	PedidoID,
	FechaPedido,
	Total
FROM Pedidos
WHERE Estado = 'Completado'
	AND (FechaPedido < @LastDate)
	OR (FechaPedido = @LastDate AND PedidoID < @LastOrder)
ORDER BY FechaPedido DESC,  PedidoID DESC;