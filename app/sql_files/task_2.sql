SELECT year(DateExch) as ExchYear, AVG(Adj_CloseCourse) AvgClouseCourse
FROM [dbexchanges].[dbo].[indexData]
WHERE Adj_CloseCourse > 0
GROUP BY year(DateExch)
ORDER BY ExchYear;
