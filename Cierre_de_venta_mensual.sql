-- Develop an SP to make the month closing 

-- 1) make auxiliar tables to store the resume
IF OBJECT_ID('ResumenMensual', 'U') IS NULL
	BEGIN
		CREATE TABLE ResumenMensual 
		(
			ResumenID			INT IDENTITY(1,1) PRIMARY KEY,
			CodigoPais			NVARCHAR(2) NOT NULL,
			Anio				INT NOT NULL,
			Mes					INT NOT NULL,
			TotalPedidos		INT NOT NULL,
			VentasTotales		DECIMAL(10,2) NOT NULL,
			TicketPromedio		DECIMAL(10,2) NOT NULL,
			FechaCierre			DATETIME NOT NULL DEFAULT GETDATE(),
			CONSTRAINT UQ_ResumenMensual UNIQUE (CodigoPais, Anio, Mes)
		);
	END;

-- 1.1 from the auxiliar resume table, make a log table
IF OBJECT_ID('LogCierres', 'U') IS NULL
	BEGIN
		CREATE TABLE LogCierres 
		(
			LogID			INT IDENTITY(1,1) PRIMARY KEY,
			CodigoPais		NVARCHAR(2) NOT NULL,
			Anio			INT NOT NULL,
			Mes				INT NOT NULL,
			Estado			NVARCHAR(20) NOT NULL,
			Mensaje			NVARCHAR(500) NOT NULL,
			Usuario			NVARCHAR(100) NOT NULL DEFAULT SYSTEM_USER,
			FechaHora		DATETIME NOT NULL DEFAULT GETDATE(),
		);
	END; GO

CREATE OR ALTER PROCEDURE SP_valid_name

	@Anio			INT,
	@Mes			INT,
	@CodigoPais		NVARCHAR(2) = NULL,
	@Resultado		NVARCHAR(20) OUTPUT
AS
	BEGIN
		SET NOCOUNT ON;

		DECLARE @FilasInsertadas INT = 0;
		-- Condition to evaluate if year and month have proper values
		IF @Anio < 2000 OR @Anio > YEAR(GETDATE()) + 1 OR @Mes < 1 OR @Mes >12
			BEGIN
				SET @Resultado = 'ERROR';

				INSERT INTO LogCierres	(CodigoPais, Anio, Mes, Estado, Mensaje)
				VALUES (ISNULL(@CodigoPais, 'ALL'), @Anio, @Mes, 'ERROR', 'Parametros invalidos');
				RETURN;
			END;

		-- Condition to verify if the current resume was already closed, if yes, don't add it again
		IF EXISTS 
		(
			SELECT 1
			FROM ResumenMensual
			WHERE (@CodigoPais IS NULL OR CodigoPais = @CodigoPais)
				AND Anio = @Anio
				AND Mes = @Mes
		)
			BEGIN
				SET @Resultado = 'ALREADY_CLOSED'

				INSERT INTO LogCierres	(CodigoPais, Anio, Mes, Estado, Mensaje)
				VALUES (ISNULL(@CodigoPais, 'ALL'), @Anio, @Mes, 'ALREADY_CLOSED', 'The period was closed previously');
				RETURN;
			END;

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

		SET @Resultado = 'SUCCESS';

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
	END;
	GO


--Execute it:
DECLARE @Res NVARCHAR(20);
	
EXEC SP_valid_name
	@Anio = 2024,
	@Mes = 1,
	@Resultado = @Res OUTPUT;

SELECT * FROM ResumenMensual;