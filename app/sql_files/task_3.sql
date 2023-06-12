SELECT IndexText, AVG(Adj_CloseCourse) AvgClouseCourse, AVG(CloseUSDCourse) AvgClouseUSDCourse 
FROM [dbexchanges].[dbo].[indexProcessed]
GROUP BY IndexText
ORDER BY AvgClouseCourse DESC;