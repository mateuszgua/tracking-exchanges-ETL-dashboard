WITH
    cource_median
    as
    (
        SELECT ii.Region, ii.Exchange,
            MIN(ip.LowCourse) OVER (PARTITION BY ip.LowCourse) AS MinCourse,
            MAX(ip.HighCourse) OVER (PARTITION BY ip.HighCourse) AS MaxCourse
        FROM [dbexchanges].[dbo].[indexProcessed] ip
            LEFT JOIN [dbexchanges].[dbo].[indexInfo] ii ON ip.IndexText = ii.IndexText
    )
SELECT cm.Region, cm.Exchange, AVG(cm.MaxCourse -cm.MinCourse) as AvgCourseMinMinusMax
FROM cource_median as cm
GROUP BY cm.Region, cm.Exchange
ORDER BY AvgCourseMinMinusMax DESC;