-- Logins
CREATE LOGIN Demo_Login_analist WITH PASSWORD = 'Pass3WordSec';

-- User
USE TiendaLatam
CREATE USER Me_user_analist FOR LOGIN Demo_Login_analist;

-- Roles

CREATE ROLE Rol_Reportes;

-- Grant access
--GRANT SELECT ON	VW_VentasPorPais			TO Rol_Reportes;
--GRANT SELECT ON	VW_ProductosTopVentas		TO Rol_Reportes;
--GRANT SELECT ON	VW_ClientesSinPedido		TO Rol_Reportes;

-- Deny access
DENY SELECT ON Pedidos	TO Rol_Reportes;
DENY SELECT ON Clientes	TO Rol_Reportes;

-- Add users to the role
ALTER ROLE Rol_Reportes ADD MEMBER Demo_Login_analist;

EXECUTE AS USER = 'Me_user_analist';
--SELECT * FROM VW_VentasPorPais;
SELECT * FROM Pedidos;
REVERT; 

-- Know which user is being used
EXECUTE AS USER = 'Me_user_analist';
SELECT USER_NAME() AS UsuarioActual;

-- Grant access to SP but not the tables
GRANT EXECUTE ON SP_ConsultarVentasPorPais TO 'Me_user_analist';
DENY SELECT ON Pedidos TO 'Me_user_analist';


-- Permissions per User
SELECT 
	dp.permission_name,
	dp.state_desc,
	dp.class_desc,
	OBJECT_NAME(dp.major_id)	AS Objeto
FROM sys.database_permissions dp
WHERE dp.grantee_principal_id = USER_ID('Me_user_analist')