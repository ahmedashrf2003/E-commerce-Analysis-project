SELECT  [CustomerID]
      ,[CustomerName]
      ,[Email]
      ,[Gender]
      ,[Age]
	  , g.City
	  , g.Country
  FROM customers c left join geography g 
  on c.GeographyID = g.GeographyID 




