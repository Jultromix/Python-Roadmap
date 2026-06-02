-- The following lines let you only do the backup and evaluate the DB:
-- Full backup
BACKUP DATABASE TiendaLatam TO DISK = 'C:\Backups\TiendaLatam_Full.bak'
WITH 
-- COMPRESSION,		-- comprimir archivo
CHECKSUM,			-- verifies data integrity
STATS = 10;			-- shows the progress
GO

-- differential backup
BACKUP DATABASE TiendaLatam TO DISK = 'C:\Backups\TiendaLatam_Diff.bak'
WITH DIFFERENTIAL,
-- COMPRESSION,		-- comprimir archivo
CHECKSUM,			-- verifies data integrity
STATS = 10;			-- shows the progress
GO

-- Log backup
BACKUP LOG TiendaLatam TO DISK = 'C:\Backups\TiendaLatam_Log.bak'
WITH 
-- COMPRESSION,		-- comprimir archivo
CHECKSUM;			-- verifies data integrity
GO

-- Verify recovery model
SELECT name, recovery_model_desc FROM sys.databases WHERE name = 'TiendaLatam'

-- Change to Full if simple
ALTER DATABASE TiendaLatam SET RECOVERY FULL;



-- Assuming you were able to to de backup then you can start the recovery:
-- Step 1
    USE master;     -- Change DB
    GO

    SELECT          -- Verify existence
        name AS BaseDatos,
        state_desc AS Estado,
        user_access_desc AS Acceso
    FROM sys.databases
    WHERE name = 'TiendaLatam';
    GO

-- Step 2
    -- SINGLE_USER: solo una conexión puede quedar dentro
    -- WITH ROLLBACK IMMEDIATE: expulsa sesiones activas y revierte transacciones
    ALTER DATABASE TiendaLatam
    SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    GO

-- Step 3 restore del full
-- REPLACE: sobrescribe la base existente
-- NORECOVERY: la deja lista para seguir aplicando backups
-- MOVE: reubica archivos físicos
    RESTORE DATABASE TiendaLatam
    FROM DISK = 'C:\Backups\TiendaLatam_Full.bak'
    WITH
        REPLACE,
        NORECOVERY,
        MOVE 'TiendaLatam'     TO 'C:\Data\TiendaLatam.mdf',
        MOVE 'TiendaLatam_log' TO 'C:\Data\TiendaLatam_log.ldf',
        STATS = 10;
    GO

-- step 4 restor del diff
    RESTORE DATABASE TiendaLatam
    FROM DISK = 'C:\Backups\TiendaLatam_Diff.bak'
    WITH
        NORECOVERY,
        STATS = 10;
    GO

-- step 5 restor del log
    RESTORE LOG TiendaLatam
    FROM DISK = 'C:\Backups\TiendaLatam_Log.bak'
    WITH
        NORECOVERY,
        STATS = 10;
    GO

-- Step 6, finish recovery and set DB online
    RESTORE DATABASE TiendaLatam
    WITH RECOVERY;
    GO

-- Step 7 set DB as multiuser
    ALTER DATABASE TiendaLatam
    SET MULTI_USER;
    GO

-- Step 8 Final verification
    SELECT
        name AS BaseDatos,
        state_desc AS Estado,
        user_access_desc AS Acceso
    FROM sys.databases
    WHERE name = 'TiendaLatam';
    GO

    USE TiendaLatam;
    GO

    SELECT
        DB_NAME() AS BaseActual,
        DATABASEPROPERTYEX('TiendaLatam', 'Status') AS EstadoPropiedad;
    GO