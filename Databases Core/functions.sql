-- Function to calculate the margin for a product using scalars:
CREATE OR ALTER FUNCTION FN_CalculateMargin
(
	@Cost	DECIMAL(10,2),		-- function param 1
	@Price	DECIMAL(10,2)		-- function param 2
)
RETURNS DECIMAL(5,2)
AS
	BEGIN
		IF @Price IS NULL OR @Price = 0 or @Cost IS NULL
			RETURN NULL
		RETURN CAST((@Price - @Cost) / @Price *100 AS DECIMAL(5,2));
	END;

-- Test the function
SELECT
	NombreProducto,
	Precio,
	Costo,
	dbo.FN_CalculateMargin(Precio, Costo) AS MarginPercentage
FROM Productos
WHERE Costo IS NOT NULL
ORDER BY dbo.FN_CalculateMargin(Precio, Costo) DESC;



-- Function to calculate the margin for a product using tables:
CREATE OR ALTER FUNCTION FN_SalesPerCountry
(
	@CodigoPais		NVARCHAR(20),
	@FechaInicio	DATE,
	@FechaFin		DATE
)
RETURNS TABLE
AS
RETURN (
	SELECT
		pa.NombrePais,
		pa.CodigoPais,
		COUNT(p.PedidoID)	AS total_orders,	
		SUM(p.Total)		AS total_sales,
		AVG(P.Total)		AS avg_sales
	FROM Pedidos p
	INNER JOIN Sucursales s ON p.SucursalID = s.SucursalID
	INNER JOIN Paises pa ON s.PaisID = pa.PaisID
	WHERE p.Estado = 'Completado'
			AND pa.CodigoPais = @CodigoPais
			AND p.FechaPedido >= @FechaInicio
			AND p.FechaPedido < DATEADD(DAY, 1, @FechaFin)
	GROUP BY pa.NombrePais, pa.CodigoPais
);
GO

SELECT * 
FROM dbo.FN_SalesPerCountry('AR','2024-01-01','2024-12-31')
GO;


-- Combine tables with CROSS APPLY:
SELECT
	pa.NombrePais,
	s.total_sales,
	s.total_orders
FROM Paises pa
CROSS APPLY dbo.FN_SalesPerCountry('AR','2024-01-01','2024-12-31') s
ORDER BY s.total_sales DESC;
GO


-- For more complex fuctions you can try the multi-statement ones:

CREATE OR ALTER FUNCTION FN_CustomerByCategory
(
	@CategoryName	NVARCHAR(100)
)
RETURNS @res TABLE
(
	ClienteID		INT,
	Nombre			NVARCHAR(100),
	TotalCompras	DECIMAL(18,2),
	LastCompra		DATE
)	
AS
	BEGIN
		INSERT INTO @res
		SELECT
			c.ClienteID,
			c.Nombre,
			SUM(dp.Cantidad*dp.PrecioUnitario)	AS TotalCompra,
			MAX(p.FechaPedido)					AS lastCompra
		FROM Clientes c					
		INNER JOIN Pedidos p			ON c.ClienteID = p.ClienteID
		INNER JOIN DetallePedidos dp	ON p.PedidoID = dp.PedidoID
		INNER JOIN Productos pr			ON dp.ProductoID = pr.ProductoID
		INNER JOIN Categorias cat		ON pr.CategoriaID = cat.CategoriaID
		WHERE cat.NombreCategoria = @CategoryName
				AND p.Estado = 'Completado'
		GROUP BY c.ClienteID, c.Nombre
		RETURN;
	END;
	GO


--Testing the multi-statement function	
SELECT*
FROM dbo.FN_CustomerByCategory('Electrónica')
ORDER BY TotalCompras DESC;
GO