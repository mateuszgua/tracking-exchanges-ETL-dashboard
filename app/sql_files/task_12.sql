WITH rank_table as
    (
        SELECT IndexText, DateExch, (HighCourse-LowCourse) Difference,
            RANK() OVER (ORDER BY (HighCourse-LowCourse) DESC) Diff_rank
        FROM [dbexchanges].[dbo].[indexData]
    )
SELECT *
FROM rank_table
WHERE Diff_rank=1;