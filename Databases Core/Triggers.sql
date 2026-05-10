-- 1) Create the test table for Audits

CREATE TABLE OrderAudit (
	AuditoriaID		INT IDENTITY(1,1) PRIMARY KEY,
	PedidoID		INT NOT NULL,
	Accion			NVARCHAR(10) NOT NULL,
	EstadoAntes		NVARCHAR(50) NULL,
	EstadoDespues	NVARCHAR(50) NULL,
	TotalAntes		DECIMAL(10,2) NULL,
	TotalDespues	DECIMAL(10,2) NULL,
	Usuario			NVARCHAR(100) NOT NULL DEFAULT SYSTEM_USER,
	FechaHora		DATETIME NOT NULL DEFAULT GETDATE()
);

-- 2) Create the Trigger
CREATE TRIGGER TR_orderaudit
ON Pedidos
AFTER INSERT, UPDATE, DELETE	-- When to trigger
AS
	BEGIN						-- The automations start with this word
		SET NOCOUNT ON;
		-- Log the changes
		INSERT INTO OrderAudit (PedidoID, Accion, EstadoAntes, EstadoDespues, TotalAntes, TotalDespues, Usuario, FechaHora)
		SELECT
			ISNULL(i.PedidoID, d.PedidoID),
			CASE
				WHEN EXISTS (SELECT 1 FROM INSERTED) AND NOT EXISTS (SELECT 1 FROM DELETED)	THEN 'INSERT'
				WHEN EXISTS (SELECT 1 FROM INSERTED) AND EXISTS (SELECT 1 FROM DELETED)		THEN 'UPDATE'
				WHEN NOT EXISTS (SELECT 1 FROM INSERTED) AND EXISTS (SELECT 1 FROM DELETED)	THEN 'DELETE'
			END,
			d.Estado,
			i.Estado,
			d.Total,
			i.Total,
			SYSTEM_USER,
			GETDATE()
		FROM INSERTED i
		FULL OUTER JOIN DELETED d ON i.PedidoID = d.PedidoID;
	END;

UPDATE Pedidos SET Total = 2800 WHERE PedidoID = 1;
SELECT * FROM OrderAudit;

-- 2) Create the test table for Customer Audits

CREATE TABLE CustomerAudit (
	AuditoriaID		INT IDENTITY(1,1) PRIMARY KEY,
	ClienteID		INT NOT NULL,
	Accion			NVARCHAR(10) NOT NULL,
	EstadoAntes		NVARCHAR(50) NULL,
	EstadoDespues	NVARCHAR(50) NULL,
	NombreAntes		TEXT NULL,
	NombreDespues	TEXT NULL,
	Usuario			NVARCHAR(100) NOT NULL DEFAULT SYSTEM_USER,
	FechaHora		DATETIME NOT NULL DEFAULT GETDATE()
);

-- 2) Create the Trigger
CREATE TRIGGER TR_customeraudit
ON Clientes
AFTER INSERT, UPDATE, DELETE	-- When to trigger
AS
	BEGIN						-- The automations start with this word
		SET NOCOUNT ON;
		-- Log the changes
		INSERT INTO CustomerAudit (ClienteID, Accion, EstadoAntes, EstadoDespues, NombreAntes, NombreDespues, Usuario, FechaHora)
		SELECT
			ISNULL(i.ClienteID, d.ClienteID),
			CASE
				WHEN EXISTS (SELECT 1 FROM INSERTED) AND NOT EXISTS (SELECT 1 FROM DELETED)	THEN 'INSERT'
				WHEN EXISTS (SELECT 1 FROM INSERTED) AND EXISTS (SELECT 1 FROM DELETED)		THEN 'UPDATE'
				WHEN NOT EXISTS (SELECT 1 FROM INSERTED) AND EXISTS (SELECT 1 FROM DELETED)	THEN 'DELETE'
			END,
			d.Activo,
			i.Activo,
			d.Nombre,
			i.Nombre,
			SYSTEM_USER,
			GETDATE()
		FROM INSERTED i
		FULL OUTER JOIN DELETED d ON i.ClienteID = d.ClienteID;
	END;

UPDATE Clientes SET Nombre = 'Pancracio' WHERE ClienteID = 1;
SELECT * FROM CustomerAudit;