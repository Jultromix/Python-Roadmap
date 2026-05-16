BEGIN TRY
	BEGIN TRANSACTION;
		INSERT INTO ResumenMensual
		(
			CodigoPais,
			Anio,
			Mes,
			TotalPedidos,
			VentasTotales,
			TicketPromedio
		)
		VALUES ('AR', 2024, 1, 150, 285000.00, 1900.00);

		INSERT INTO LogCierres
		(
			CodigoPais,
			Anio,
			Mes,
			Estado
		)
		VALUES ('AR', 2024, 1, 'SUCCESS');
	COMMIT TRANSACTION;
END TRY

BEGIN CATCH
	DECLARE @ErrorNumber	INT	= ERROR_NUMBER();
	DECLARE @ErrorMessage	NVARCHAR(4000)	= ERROR_MESSAGE();
	DECLARE @ErrorLine		INT	= ERROR_LINE();
	DECLARE @ErrorProcedure	INT	= ERROR_PROCEDURE();

	IF @@TRANCOUNT > 0 
		ROLLBACK TRANSACTION

	INSERT INTO LogCierres
	(
		CodigoPais,
		Anio,
		Mes,
		Estado,
		Mensaje
	)
	VALUES (
		'AR',
		2024, 
		1, 
		'ERROR', 
		'Error' + CAST(@ErrorNumber AS NVARCHAR(20)) + 
		CAST(@ErrorLine AS NVARCHAR(20)) + ': ' + 
		@ErrorMessage
	);

	THROW
END CATCH;
GO



--- A shorter example catching errors:
BEGIN TRY
	THROW 50000, 'Error de demostracion', 1;
END TRY

BEGIN CATCH
	SELECT
		ERROR_NUMBER()		AS	NumeroDeError,
		ERROR_MESSAGE()		AS MensajeDeError,
		ERROR_LINE()		AS	LineaDeFallo,
		ERROR_SEVERITY()	AS	Severidad,
		ERROR_STATE()		AS	Estado,
		ERROR_PROCEDURE()	AS	ProcedimientoDeFallo
END CATCH;


-- Applying that to the Cierre de venta mensual procedure:
CREATE OR ALTER PROCEDURE SP_valid_name

	@Anio			INT,
	@Mes			INT,
	@CodigoPais		NVARCHAR(2) = NULL,
	@Resultado		NVARCHAR(20) OUTPUT
AS
	BEGIN
		SET NOCOUNT ON;

		BEGIN TRY
			DECLARE @FilasInsertadas INT = 0;
			-- Condition to evaluate if year and month have proper values
			IF @Anio < 2000 OR @Anio > YEAR(GETDATE()) + 1 OR @Mes < 1 OR @Mes >12
				THROW 50001, 'Invalid date params',1;

			-- Condition to verify if the current resume was already closed, if yes, don't add it again
			IF EXISTS 
			(
				SELECT 1
				FROM ResumenMensual
				WHERE (@CodigoPais IS NULL OR CodigoPais = @CodigoPais)
					AND Anio = @Anio
					AND Mes = @Mes
			)
				THROW 50002, 'The period tome was already closed', 1;   --This is the error to raise


			BEGIN TRANSACTION       -- Make inserts into tables
				-- Logic if previous error cathers were false
				INSERT INTO ResumenMensual
				(CodigoPais, Anio, Mes, TotalPedidos, VentasTotales, TicketPromedio)

				SELECT
					pa.CodigoPais,
					@Anio,
					@Mes,
					COUNT(p.PedidoID),
					SUM(p.Total),
					AVG(p.Total)
				FROM Pedidos p
					INNER JOIN Sucursales s ON p.SucursalID = s.SucursalID
					INNER JOIN Paises pa  ON s.PaisID = pa.PaisID
				WHERE YEAR(p.FechaPedido)  = @Anio
				  AND MONTH(p.FechaPedido) = @Mes
				  AND p.Estado = 'Completado'
				  AND (@CodigoPais IS NULL OR pa.CodigoPais = @CodigoPais)
				GROUP BY pa.CodigoPais

				SET @FilasInsertadas = @@ROWCOUNT;



				INSERT INTO LogCierres
				(CodigoPais, Anio,Mes,Estado,Mensaje)
				VALUES 
				(
					ISNULL(@CodigoPais,'ALL'),
					@Anio,
					@Mes,
					'SUCCESS',
					'Cierre existoso. Paises procesados' + CAST(@FilasInsertadas AS NVARCHAR(10))
				);
			COMMIT TRANSACTION
			SET @Resultado = 'SUCCESS';
		END TRY
		
		BEGIN CATCH
			IF @@TRANCOUNT > 0
				ROLLBACK TRANSACTION;

			SET @Resultado = 
				CASE ERROR_NUMBER()
					WHEN 50002 THEN 'ALREADY CLOSED'
					ELSE 'ERROR'
				END;

			INSERT INTO LogCierres
			(CodigoPais, Anio,Mes,Estado,Mensaje)
			VALUES 
				(
					ISNULL(@CodigoPais,'ALL'),
					@Anio,
					@Mes,
					@Resultado,
					'Error' + CAST(ERROR_NUMBER() AS NVARCHAR(20)) + ': ' + ERROR_MESSAGE()
				);
			IF ERROR_NUMBER() NOT IN (50001, 50002)     --available errorr
				THROW;	

		END CATCH
	END;
	GO

--Execute it:
DECLARE @Res NVARCHAR(20);
	
EXEC SP_valid_name
	@Anio = 2019,
	@Mes = 13,
	@CodigoPais = 'AR',
	@Resultado = @Res OUTPUT;

SELECT @Res AS Resultado;

SELECT TOP 5 *
FROM LogCierres
ORDER BY FechaHora DESC;
