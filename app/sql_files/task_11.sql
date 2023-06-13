WITH lastCourse_table as
    (
        SELECT IndexText, DateExch, Adj_CloseCourse,
            LAG(Adj_CloseCourse, 1) OVER (ORDER BY DateExch) last_ClouseCourse
        FROM [dbexchanges].[dbo].[indexData]
        WHERE Adj_CloseCourse > 0
    )
SELECT TOP 1 lc.IndexText, ABS(lc.last_ClouseCourse-lc.Adj_CloseCourse) DailyCourseDifference,
    RANK() OVER(PARTITION BY lc.IndexText ORDER BY ABS(lc.last_ClouseCourse-lc.Adj_CloseCourse) DESC) rank_no
FROM lastCourse_table lc;