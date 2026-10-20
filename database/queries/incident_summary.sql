SELECT 
    department,
    COUNT(*) as total_incidents,
    AVG(severity_level) as avg_severity,
    SUM(CASE WHEN severity_level >= 3 THEN 1 ELSE 0 END) as high_severity_count
FROM incidents
GROUP BY department
ORDER BY total_incidents DESC;
