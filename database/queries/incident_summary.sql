-- Resumen de incidentes por severidad y días perdidos
SELECT 
    severity_level, 
    COUNT(*) as total_incidents, 
    SUM(days_lost) as total_days_lost
FROM incidents
GROUP BY severity_level;

-- Resumen por sector industrial
SELECT 
    sector, 
    COUNT(*) as incident_count
FROM incidents
GROUP BY sector;
