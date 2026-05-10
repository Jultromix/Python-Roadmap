
CREATE PROCEDURE	SP_GetSalesPerCountry	-- SP name
	@CodigoPais		NVARCHAR(2),			-- parameter 1)
	@FechaInicio	DATE,					-- parameter 2)
	@FechaFin		DATE					-- parameter 3)
	AS										
		BEGIN								-- Initiate the logic query
			SET NOCOUNT ON;					-- Don't count affected rows
			SELECT
				pa.NombrePais,
				pa.CodigoPais,
				COUNT(p.PedidoID)		AS total_orders,
				SUM(p.Total)			AS total_sales,
				AVG(p.Total)			AS avg_sales,
				MAX(p.Total)			AS max_sale,
				MIN(p.Total)			AS min_sale
			FROM Pedidos p
			INNER JOIN Sucursales s ON p.SucursalID = s.SucursalID
			INNER JOIN Paises pa ON s.SucursalID = pa.PaisID
			WHERE p.Estado = 'Completado'
				AND pa.CodigoPais = @CodigoPais
				AND p.FechaPedido >= @FechaInicio
				AND p.FechaPedido <= DATEADD(DAY,1,@FechaFin)		-- Add the whole day
			GROUP BY pa.NombrePais, pa.CodigoPais
		END;								-- End the logic query

-- Call the last command with:
-- EXEC SP_name(var1, var2, var3)
EXEC SP_GetSalesPerCountry 'US', '2024-01-01', '2024-12-31';

-- 2) A variat SP with a defualt value assigned through logic:

CREATE PROCEDURE	SP_GetSalesPerCountry	-- SP name
	@CodigoPais		NVARCHAR(2) = NULL,			-- parameter 1)
	@FechaInicio	DATE  = NULL,				-- parameter 2)
	@FechaFin		DATE = NULL					-- parameter 3)
	AS										
		BEGIN								-- Initiate the logic query
			SET NOCOUNT ON;					-- Don't count affected rows

			SET @FechaInicio = ISNULL(@FechaInicio, CAST(GETDATE() AS DATE));	-- Default date if not param provided
			SET @FechaFin = ISNULL(@FechaFin, DATEADD(YEAR, -1,@FechaFin));

			SELECT							-- This is the query
				pa.NombrePais,
				pa.CodigoPais,
				COUNT(p.PedidoID)		AS total_orders,
				SUM(p.Total)			AS total_sales,
				AVG(p.Total)			AS avg_sales,
				MAX(p.Total)			AS max_sale,
				MIN(p.Total)			AS min_sale
			FROM Pedidos p
			INNER JOIN Sucursales s ON p.SucursalID = s.SucursalID
			INNER JOIN Paises pa ON s.SucursalID = pa.PaisID
			WHERE p.Estado = 'Completado'
				AND pa.CodigoPais = @CodigoPais
				AND p.FechaPedido >= @FechaInicio
				AND p.FechaPedido <= DATEADD(DAY,1,@FechaFin)		-- Add the whole day
			GROUP BY pa.NombrePais, pa.CodigoPais
		END;	

-- Calling the SP	
EXEC SP_GetSalesPerCountry;
EXEC SP_GetSalesPerCountry 'MX';
EXEC SP_GetSalesPerCountry @CodigoPais = 'CO', @FechaInicio = '2024-01-01', @FechaFin = '2024-12-31'; 


-- Extra steps to edit an SP:
	-- 1) Drop the SP
DROP PROCEDURE IF EXISTS SP_GetSalesPerCountry;

	-- 2) Create the SP again with the new logic
CREATE OR ALTER PROCEDURE	SP_GetSalesPerCountry	-- SP name

	-- 3) See the definition
EXEC sp_helptext 'SP_GetSalesPerCountry';

	-- 4) Grant permissions to execute the SP to a user
GRANT EXECUTE ON SP_GetSalesPerCountry TO [UserName];



-- 4) Exercise: Use the last script and now add more sales per employee, per country and period -- Pending
CREATE PROCEDURE	SP_GetSalesPerCountry	-- SP name
	@CodigoPais		NVARCHAR(2) = NULL,			-- parameter 1)
	@FechaInicio	DATE  = NULL,				-- parameter 2)
	@FechaFin		DATE = NULL					-- parameter 3)
	AS										
		BEGIN								-- Initiate the logic query
			SET NOCOUNT ON;					-- Don't count affected rows

			SET @FechaInicio = ISNULL(@FechaInicio, CAST(GETDATE() AS DATE));	-- Default date if not param provided
			SET @FechaFin = ISNULL(@FechaFin, DATEADD(YEAR, -1,@FechaFin));

			SELECT							-- This is the query
				pa.NombrePais,
				pa.CodigoPais,
				COUNT(p.PedidoID)		AS total_orders,
				SUM(p.Total)			AS total_sales,
				AVG(p.Total)			AS avg_sales,
				MAX(p.Total)			AS max_sale,
				MIN(p.Total)			AS min_sale
			FROM Pedidos p
			INNER JOIN Sucursales s ON p.SucursalID = s.SucursalID
			INNER JOIN Paises pa ON s.SucursalID = pa.PaisID
			Inner JOIN Empleados e ON p.EmpleadoID = e.EmpleadoID
			WHERE p.Estado = 'Completado'
				AND pa.CodigoPais = @CodigoPais
				AND p.FechaPedido >= @FechaInicio
				AND p.FechaPedido <= DATEADD(DAY,1,@FechaFin)		-- Add the whole day
			GROUP BY pa.NombrePais, pa.CodigoPais
		END;