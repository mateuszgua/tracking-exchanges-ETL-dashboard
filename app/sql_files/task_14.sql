SELECT ii.Region, ii.IndexText, MAX(id.Volume) Volume_Max, AVG(id.Volume) Volume_Avg
FROM [dbexchanges].[dbo].[indexData] id
    LEFT JOIN [dbexchanges].[dbo].[indexInfo] ii ON id.IndexText=ii.IndexText
WHERE id.Adj_CloseCourse > 0
GROUP BY ii.Region, ii.IndexText;