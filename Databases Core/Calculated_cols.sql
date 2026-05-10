-- 1) Create the missing field
ALTER TABLE Productos
ADD Costo NUMERIC(12,2);

UPDATE Productos
SET Costo = ISNULL(Precio, 0) * 0.57;

-- 2) First you try a query to get the margin
SELECT
	NombreProducto,
	Precio,
	(Precio - Costo) / Precio * 100 AS MarginPercent
FROM Productos p;

-- 3) Once validated, the calculated column will get added
ALTER TABLE Productos
-- ADD MarginPercent AS (Precio - Costo) / Precio * 100	-- Add the margin as column
ADD PriceWithIVA AS (Precio * 1.21);


-- 4) Assume the IVA has changed to a new value... first delete it:
ALTER TABLE Productos
DROP COLUMN PriceWithIVA;
GO
-- 4.1) then add it again with the updated calculation:
ALTER TABLE Productos
ADD PriceWithIVA AS (Precio * 1.19);
GO


-- 5) Now lets create the same column but as a persisted column:
-- 5.1) Delete the column
ALTER TABLE Productos
DROP COLUMN MarginPercent;
GO

-- 5.2) Create it again but as a persisted one:
ALTER TABLE Productos
ADD MarginPercent AS (
	CASE
		WHEN Costo IS NULL OR Precio = 0 THEN NULL
		ELSE CAST(((Precio - Costo) / Precio) * 100 AS DECIMAL(5,2))
	END
) PERSISTED;
GO

-- 5.3 Verify the stored value:
SELECT 
	NombreProducto,
	Precio,
	Costo,
	MarginPercent
FROM Productos
WHERE Costo IS NOT NULL;


SELECT * FROM Productos;


-- 6) Exercise: create a persited column for inventory_value price*stock
-- 5.2) Create it again but as a persisted one:
ALTER TABLE Productos
ADD Inventory_value AS (
	CASE
		WHEN Precio IS NULL OR Stock = 0 THEN NULL
		ELSE CAST((Precio * Stock) AS DECIMAL(12,2))
	END
) PERSISTED;
GO