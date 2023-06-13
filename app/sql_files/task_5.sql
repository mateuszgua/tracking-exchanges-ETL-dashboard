WITH
    cource_median
    as
    (
        SELECT ii.Region, ip.IndexText,
            PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY ip.CloseUSDCourse)
            OVER (PARTITION BY ip.IndexText)
            AS Median_CloseUSDCourse,
            MIN(ip.CloseUSDCourse) OVER (PARTITION BY ip.CloseUSDCourse) AS MinClouseCourse,
            MAX(ip.CloseUSDCourse) OVER (PARTITION BY ip.CloseUSDCourse) AS MaxClouseCourse,
            AVG(ip.CloseUSDCourse) OVER (PARTITION BY ip.CloseUSDCourse) AS AvgClouseCourse,
            STDEVP(ip.CloseUSDCourse) OVER (PARTITION BY ip.CloseUSDCourse) AS STDEVPClouseCourse
        FROM [dbexchanges].[dbo].[indexProcessed] ip
            LEFT JOIN [dbexchanges].[dbo].[indexInfo] ii ON ip.IndexText = ii.IndexText
    )
SELECT cm.Region, cm.IndexText, MIN(cm.Median_CloseUSDCourse) as Median_CloseUSDCourse,
    MIN(cm.MinClouseCourse) as MinClouseCourse, MAX(cm.MaxClouseCourse) as MaxClouseCourse,
    STDEVP(cm.STDEVPClouseCourse) as STDEVPClouseCourse, AVG(cm.AvgClouseCourse) as AvgClouseCourse
FROM cource_median as cm
GROUP BY cm.Region, cm.IndexText
ORDER BY cm.Region;