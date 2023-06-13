WITH rank_table as (
    SELECT ii.Exchange, id.IndexText, id.Adj_CloseCourse, YEAR(id.DateExch) DateYear,
        RANK () OVER (PARTITION BY id.IndexText ORDER BY id.Adj_CloseCourse ASC) ClouseCourse_rank
    FROM [dbexchanges].[dbo].[indexData] id
        LEFT JOIN [dbexchanges].[dbo].[indexInfo] ii ON id.IndexText = ii.IndexText
    WHERE id.Adj_CloseCourse > 0)
SELECT * 
FROM rank_table rt
WHERE rt.ClouseCourse_rank=1;