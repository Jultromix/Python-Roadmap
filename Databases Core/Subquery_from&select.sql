-- 1) Subquery in the FROM clause
SELECT TOP 3
    resumen.CodigoPais,
    resumen.NombrePais,
    resumen.PromedioVentas,
    resumen.TotalPedidos 
FROM (
    SELECT
        pa.CodigoPais,
        pa.NombrePais,
        AVG(p.Total) AS PromedioVentas,
        COUNT(p.PedidoID) AS TotalPedidos    
    FROM Pedidos p
    INNER JOIN Clientes c ON p.ClienteID = c.ClienteID
    INNER JOIN Paises pa ON pa.PaisID = c.PaisID
    WHERE p.Estado = 'Completado'
    GROUP BY pa.CodigoPais, pa.NombrePais
) AS resumen
ORDER BY resumen.PromedioVentas DESC;

-- 2) Another yet more complex Subquery in the FORM clause
SELECT TOP 5 *
FROM (
    SELECT
        c.PaisID,
        pa.NombrePais,
        COUNT(DISTINCT p.ClienteID)                 AS ClientesActivos,
        SUM(p.Total)                                AS VentasTotales,
        SUM(p.Total) / COUNT(DISTINCT p.ClienteID)  AS VentasPorCliente 
    FROM Pedidos p
    INNER JOIN Clientes c ON P.ClienteID = c.ClienteID
    INNER JOIN Paises pa ON pa.PaisID = c.PaisID
    GROUP BY c.PaisID, pa.NombrePais
) AS estadisticas
ORDER BY VentasPorCliente DESC;

-- 3) Subqueries in the Select clause: Each country with its percentage of total sales

SELECT 
    pa.NombrePais,
    SUM(p.Total) AS VentasPais,
    (
        SELECT SUM(Total)
        FROM Pedidos
        WHERE Estado = 'Completado'
    ) AS VentasTotalesGlobal,
    CAST (
        SUM(p.Total) * 100 / 
            (
                SELECT SUM(Total)
                FROM Pedidos
                WHERE Estado = 'Completado'
            ) AS DECIMAL(5,2)   
        ) AS PorcentajeDelTotal
FROM Pedidos p
INNER JOIN Clientes c ON p.ClienteID = c.ClienteID 
INNER JOIN Paises pa ON pa.PaisID = c.PaisID
WHERE p.Estado = 'Completado'
GROUP BY pa.NombrePais
ORDER BY VentasPais DESC;

-- 4) Local Variables
DECLARE @TotalGlobal DECIMAL(18,2);
SELECT @TotalGlobal = 
            SUM(Total) 
            FROM Pedidos 
            WHERE Estado = 'Completado';

SELECT
    pa.NombrePais,
    SUM(p.Total) AS VentasPais,
    CAST(SUM(p.Total) * 100.0 / @TotalGlobal AS DECIMAL(5,2)) AS PorcentageDeVentas
FROM Pedidos p
INNER JOIN Clientes c ON p.ClienteID = c.ClienteID 
INNER JOIN Paises pa ON pa.PaisID = c.PaisID
WHERE p.Estado = 'Completado'
GROUP BY pa.NombrePais
ORDER BY VentasPais DESC;