SELECT ii.Region,
    COUNT(ip.LowCourse) AS CountTransaction
FROM [dbexchanges].[dbo].[indexProcessed] ip
    LEFT JOIN [dbexchanges].[dbo].[indexInfo] ii ON ip.IndexText = ii.IndexText
GROUP BY ii.Region
ORDER BY CountTransaction DESC;