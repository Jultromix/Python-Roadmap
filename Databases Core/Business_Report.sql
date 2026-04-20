-- Data exploration
SELECT COUNT(*) as total_pedidos FROM pedidos;
SELECT COUNT(*) AS total_clientes FROM clientes;
SELECT COUNT(*) AS total_productos FROM productos;
SELECT COUNT(*) AS total_detalle FROM detalle_pedidos;


-- Total sales per country:
SELECT
	pa.nombrepais AS pais,
	--These are the aggregations and represent the output columns of the query
	COUNT(DISTINCT p.pedidoid) AS total_pedidos,	-- We use "DISTINCT" because there're multiple records with same pedidoid
	COUNT(DISTINCT p.clienteid) AS clientes_unicos,
	TO_CHAR(SUM(dp.cantidad * dp.preciounitario), 'FM$999,999,999.00') AS monto_total,
	TO_CHAR(AVG(dp.cantidad * dp.preciounitario), 'FM$999,999.00') AS ticket_promedio

FROM pedidos p
INNER JOIN sucursales s			ON p.sucursalid = s.sucursalid
INNER JOIN paises pa			ON s.paisid = pa.paisid
INNER JOIN detalle_pedidos dp	ON p.pedidoid = dp.pedidoid
GROUP BY pa.paisid, pa.nombrepais
ORDER BY monto_total DESC;

-- Monthly Report Top 12 months
SELECT
	TO_CHAR(p.fechapedido, 'YYYY-MM') 											AS periodo,
	COUNT(DISTINCT p.pedidoid) 											AS total_pedidos,
	TO_CHAR(SUM(dp.cantidad * dp.preciounitario), 'FM$999,999,999.00') 	AS monto_total
FROM pedidos p
INNER JOIN detalle_pedidos dp	ON p.pedidoid = dp.pedidoid
GROUP BY TO_CHAR(p.fechapedido, 'YYYY-MM')
LIMIT 12;


-- Top 10 most sold products
SELECT 
	pr.nombreproducto 						AS producto,
	ca.nombrecategoria 						AS categoria,
	SUM(dp.cantidad)						AS sold_qty,
	SUM(dp.cantidad * dp.preciounitario)	AS ingreso_total
FROM detalle_pedidos dp
INNER JOIN productos pr ON pr.productoid = dp.productoid
INNER JOIN categorias ca ON ca.categoriaid = pr.categoriaid
GROUP BY pr.productoid, pr.nombreproducto, ca.categoriaid
ORDER BY ingreso_total DESC
LIMIT 10;

-- Report by category using HAVING
SELECT 
	ca.categoriaid							AS categoria,
	COUNT(DISTINCT p.pedidoid)				AS pedidos,
	SUM(dp.cantidad)						AS unidades,
	SUM(dp.cantidad * dp.preciounitario)	AS monto_total
FROM detalle_pedidos dp
INNER JOIN productos pr		ON pr.productoid = dp.productoid 
INNER JOIN categorias ca	ON pr.categoriaid = ca.categoriaid
INNER JOIN pedidos p		ON p.pedidoid = dp.pedidoid
GROUP BY ca.categoriaid, ca.nombrecategoria
HAVING SUM(dp.cantidad * dp.preciounitario) > 10000
ORDER BY monto_total DESC;

-- COMPLETE DASHBOARD:
SELECT 
	'Paises activos' AS indicador, COUNT(DISTINCT paisid)::TEXT AS valor FROM sucursales
UNION ALL
SELECT 'Sucursales', COUNT(*)::TEXT FROM sucursales
UNION ALL
SELECT 'Empleados', COUNT(*)::TEXT FROM empleados
UNION ALL
SELECT 'Clientes Activos', COUNT(*)::TEXT FROM clientes WHERE activo = TRUE
UNION ALL
SELECT 'Productos', COUNT(*)::TEXT FROM productos
UNION ALL
SELECT 'Pedidos Totales', COUNT(*)::TEXT FROM pedidos
UNION ALL 
SELECT 'Sucursales', COUNT(*)::TEXT FROM sucursales
UNION ALL
SELECT 'Líneas de Detalle', COUNT(*)::TEXT FROM detalle_pedidos;
