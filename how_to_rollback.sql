-- How to create a transaction:

BEGIN TRANSACTION;
    -- Operation 1
    UPDATE Porductos
    SET Stock = Stock - 2;
    WHERE ProductID = 1;

    --Operation 2
    INSERT INTO Pedidos (ClienteID, SucursalID, EmpleadoID, FechaPedido,Estado, Total)
    VALUES (1, 1, 1, GETDATE(), 'Completado', 4599.98);

    --Operation 3
    INSERT INTO DetallePedidos (PedidoID, ProductoID, Cantidad, PrecioUnitario)
    VALUES (SCOPE_IDENTITY(), 1, 2, 2299.99);

COMMIT TRANSACTION;
  
SELECT @@TRANCOUNT AS TranCountAntes;

BEGIN TRANSACTION;
SELECT @@TRANCOUNT AS TranCountNivel1;

BEGIN TRANSACTION;
SELECT @@TRANCOUNT AS TranCountNivel2;

COMMIT TRANSACTION;
SELECT @@TRANCOUNT AS TranCountPostCommit1;
  
COMMIT TRANSACTION;
SELECT @@TRANCOUNT AS TranCountPostCommit2;




SELECT * FROM ResumenMensual;

-- Example 2 with mid save point
BEGIN TRANSACTION;
	--Operation 1
	INSERT INTO ResumenMensual
		(
		CodigoPais,
		Anio,
		Mes,
		TotalPedidos,
		VentasTotales,
		TicketPromedio
		)
	VALUES
		(
		'AR',
		1,
		10,
		150000.00,
		15000.00
		);

	SAVE TRANSACTION PuntoGuardado1;
	--Operation 2
	DELETE FROM LogCierres
	WHERE FechaHora < DATEADD(YEAR, -1, GETDATE());
	
	-- If OP was too aggressive, you go back ot he saving point
	IF @@ROWCOUNT > 1000
		BEGIN
			ROLLBACK TRANSACTION PuntoGuardado1;
			PRINT 'Log cleaning reverted - too many affected rows';
		END;
COMMIT TRANSACTION


-- Rollback demonstration

SELECT Stocl
FROM Porductos
WHERE ProductoID = 1;

BEGIN TRANSACTION
    UPDATE PorductosSET Stock = Stock - 999
    WHERE ProductoID = 1;

    -- "Something went wrong"
    SELECT Stock
    FROM Productos
    WHERE Producto = 1;
    
    ROLLBACK TRANSACTION;
        
    SELECT Stock
    FROM Productos
    WHERE ProductoID = 1;

