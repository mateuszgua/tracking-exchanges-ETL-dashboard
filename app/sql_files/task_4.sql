WITH
    cource_median
    as
    (
        SELECT ii.Region, ip.IndexText,
            PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY ip.OpenCourse)
            OVER (PARTITION BY ip.IndexText)
            AS Median_OpenCourse
        FROM [dbexchanges].[dbo].[indexProcessed] ip
            LEFT JOIN [dbexchanges].[dbo].[indexInfo] ii ON ip.IndexText = ii.IndexText
    )
SELECT cm.Region, cm.IndexText, MAX(cm.Median_OpenCourse)
FROM cource_median as cm
GROUP BY cm.Region, cm.IndexText
ORDER BY cm.Region;