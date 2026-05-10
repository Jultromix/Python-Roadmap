
-- Usafe of IF and ELSE clause

CREATE OR ALTER PROCEDURE	SP_GetSalesPerCountry	-- SP name
	@CodigoPais		NVARCHAR(2) = NULL,			-- parameter 1)
	@FechaInicio	DATE  = NULL,				-- parameter 2)
	@FechaFin		DATE = NULL,				-- parameter 3)
	@AvailableResults	BIT OUTPUT				-- parameter 4)
	AS										
		BEGIN								-- Initiate the logic query
			SET NOCOUNT ON;					-- Don't count affected rows
			DECLARE @ResuLtCounter INT;

			SELECT							-- This is the query to check if has results
				@ResultCounter = COUNT(*)
			FROM Pedidos p
			INNER JOIN Sucursales s ON p.SucursalID = s.SucursalID
			INNER JOIN Paises pa ON s.SucursalID = pa.PaisID
			WHERE p.Estado = 'Completado'
				AND pa.CodigoPais = @CodigoPais
				AND p.FechaPedido >= @FechaInicio
				AND p.FechaPedido <= DATEADD(DAY,1,@FechaFin)		-- Add the whole day
			GROUP BY pa.NombrePais, pa.CodigoPais
		
		-- CONDITIONAL LOGIC
		IF @ResuLtCounter = 0					-- Make 1st conditional
			BEGIN								-- Operations if value is True
				SET NOCOUNT ON;					-- Don't count affected rows
				SET @AvailableResults = 0;		-- means no results
				PRINT 'There are no sales for ' + @CodigoPais + ' for selected period'
			END
		ELSE
			BEGIN							-- Operations if value is False
				SET @AvailableResults = 1;		-- means there are results
				DECLARE @UPPER_SALES_LIMIT INT = 1000000;
				DECLARE @Total_Sales NUMERIC(18,2);
				DECLARE @Total_Orders INT;

				SELECT							-- Get query
					@Total_Orders = COUNT(p.PedidoID),
					 @Total_Sales = SUM(p.Total)
				FROM Pedidos p
				INNER JOIN Sucursales s ON p.SucursalID = s.SucursalID
				INNER JOIN Paises pa ON s.SucursalID = pa.PaisID
				WHERE p.Estado = 'Completado'
					AND pa.CodigoPais = @CodigoPais
					AND p.FechaPedido >= @FechaInicio
					AND p.FechaPedido <= DATEADD(DAY,1,@FechaFin)		-- Add the whole day
				GROUP BY pa.NombrePais

				SELECT @CodigoPais AS pais,
					@Total_Sales AS ventas,
					@Total_Orders as pedidos

				IF @Total_Sales >= @UPPER_SALES_LIMIT
					BEGIN
						PRINT 'For the country:' + @CodigoPais + 'it is a high volume of sales'
					END;
				ELSE
					BEGIN
						PRINT 'For the country: ' + @CodigoPais + ' it is not a high sales volume period'
					END;
			END;
		END;								-- End the logic query
		GO


-- Testting the SP:
DECLARE @Result BIT;
EXEC SP_GetSalesPerCountry 'MX', '2024-01-01', '2024-12-31', @Result OUTPUT;
SELECT @Result AS AvailableReuslts;

-- Another example but with WHILE
DECLARE @CurrentCountry		NVARCHAR(2);
DECLARE @Counter			INT = 1;
DECLARE	@TotalCountries		INT;
DECLARE	@Acc_Sales			DECIMAL(18,2) = 0;

SELECT @TotalCountries = COUNT(*)		-- Get how many countries
FROM Paises

WHILE @Counter <= @TotalCountries
	BEGIN
		-- Get coutnry code:
		SELECT 
			@CurrentCountry = CodigoPais
		FROM(
			SELECT
				CodigoPais,
				ROW_NUMBER() OVER (ORDER BY PaisID) AS Fila
			FROM Paises 
		)	AS sorted_ctry_code
		WHERE Fila =  @Counter

		-- Accumulate sales
		SELECT
			@Acc_Sales = @Acc_Sales + ISNULL(SUM(p.Total),0)
		FROM Pedidos p
		INNER JOIN Sucursales s ON p.SucursalID = s.SucursalID
		INNER JOIN Paises pa ON s.PaisID = pa.PaisID
		WHERE pa.CodigoPais = @CurrentCountry AND p.Estado = 'Completado'

		PRINT 'Procesado: ' + @CurrentCountry + ' - Accumulated ' + CAST(@Acc_Sales AS NVARCHAR(20));
		SET @Counter = @Counter + 1;
	END;	