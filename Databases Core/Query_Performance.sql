-- Show top 10 queries which consumed the most from the CPU since the las reboot
SELECT TOP 10
	SUBSTRING(st.text, (qs.statement_start_offset/2) + 1,
	((CASE qs.statement_end_offset WHEN -1 THEN DATALENGTH(st.text)
	ELSE qs.statement_end_offset END - qs.statement_start_offset)/2) + 1) AS QueryText,
	qs.execution_count,
	qs.total_worker_time / 1000							AS TotalCPU_ms,
	qs.total_worker_time / qs.execution_count / 1000	AS PromedioCPU_ms,
	qs.last_logical_reads / qs.execution_count			AS Promedio_readings,
	qs.last_elapsed_time / qs.execution_count / 1000	AS Promedio_tiempo_ms

FROM sys.dm_exec_query_stats qs
CROSS APPLY sys.dm_exec_sql_text(qs.sql_handle) st
ORDER BY qs.total_worker_time DESC;

-- The top 10 most cost consuming reads
SELECT TOP 10
	SUBSTRING(st.text, (qs.statement_start_offset/2) + 1,
	((CASE qs.statement_end_offset WHEN -1 THEN DATALENGTH(st.text)
	ELSE qs.statement_end_offset END - qs.statement_start_offset)/2) + 1) AS QueryText,
	qs.execution_count,
	qs.total_elapsed_time / qs.execution_count / 1000	AS Promedio_tiempo_ms,
	qs.last_logical_reads / qs.execution_count			AS Promedio_readings
FROM sys.dm_exec_query_stats qs
CROSS APPLY sys.dm_exec_sql_text(qs.sql_handle) st
ORDER BY qs.total_logical_reads DESC;


-- Which are the indexes with less usage
SELECT
	OBJECT_NAME(i.object_id)	AS Tabla,
	i.name						AS NombreIndice,
	i.type_desc					AS Tipo,
	ius.user_seeks				AS Seeks,
	ius.user_lookups			AS Lookups,
	ius.user_updates			AS Actualizaciones
FROM sys.indexes i
LEFT JOIN sys.dm_db_index_usage_stats ius
	ON i.object_id = ius.object_id
	AND i.index_id = ius.index_id
	AND ius.database_id = DB_ID()
WHERE OBJECT_NAME(i.object_id)	IS NOT NULL
	AND i.type_desc <> 'HEAP'
	AND (ius.user_seeks) = 0 OR ius.user_seeks IS NULL
	AND (ius.user_scans) = 0 OR ius.user_scans IS NULL
ORDER BY ius.user_updates DESC;