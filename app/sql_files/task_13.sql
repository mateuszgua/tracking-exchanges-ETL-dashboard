SELECT TOP 10
    ii.Region, ABS(id.CloseCourse-id.OpenCourse) DifferenceOpenClouse, id.DateExch,
    RANK() OVER (ORDER BY ABS(id.CloseCourse-id.OpenCourse) DESC)
FROM [dbexchanges].[dbo].[indexData] id
    LEFT JOIN [dbexchanges].[dbo].[indexInfo] ii ON id.IndexText=ii.IndexText
WHERE id.Adj_CloseCourse > 0;