SELECT IndexText, MIN(Adj_CloseCourse) MinCourse, MAX(Adj_CloseCourse) MaxCourse
FROM [dbexchanges].[dbo].[indexData]
WHERE Adj_CloseCourse > 0
GROUP BY IndexText
ORDER BY IndexText;