SELECT * FROM (
    SELECT ii.Exchange, id.IndexText, id.Adj_CloseCourse, id.DateExch,
        RANK () OVER (PARTITION BY ii.Region ORDER BY id.Adj_CloseCourse DESC) ClouseCourse_rank
FROM [dbexchanges].[dbo].[indexData] id
    LEFT JOIN [dbexchanges].[dbo].[indexInfo] ii ON id.IndexText = ii.IndexText) t
WHERE ClouseCourse_rank <= 5;
