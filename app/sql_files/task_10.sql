SELECT MIN(id.Adj_CloseCourse) ClouseCourse_Min, MAX(id.Adj_CloseCourse) ClouseCourse_Max,
    AVG(id.Adj_CloseCourse) ClouseCourse_Avg, STDEVP(id.Adj_CloseCourse) ClouseCourse_STDEVP
FROM [dbexchanges].[dbo].[indexData] id
    LEFT JOIN [dbexchanges].[dbo].[indexInfo] ii ON id.IndexText = ii.IndexText
WHERE ii.Currency = 'USD' and id.Adj_CloseCourse > 0;
