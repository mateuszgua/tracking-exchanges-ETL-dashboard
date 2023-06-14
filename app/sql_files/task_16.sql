WITH lastCourse_table as
    (
        SELECT IndexText, DateExch, Adj_CloseCourse,
            LAG(Adj_CloseCourse, 1) OVER (ORDER BY DateExch) last_ClouseCourse
        FROM [dbexchanges].[dbo].[indexData]
        WHERE Adj_CloseCourse > 0
    )
SELECT TOP 14 lc.IndexText, MONTH(lc.DateExch) MontExch, AVG(lc.last_ClouseCourse-lc.Adj_CloseCourse) Avg_MonthCourseDifference,
    RANK() OVER(Partition BY lc.IndexText ORDER BY AVG(lc.last_ClouseCourse-lc.Adj_CloseCourse)) rank_no
FROM lastCourse_table lc
GROUP BY lc.IndexText, MONTH(lc.DateExch)
ORDER BY rank_no;
