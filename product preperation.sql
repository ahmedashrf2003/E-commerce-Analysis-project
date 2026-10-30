SELECT TOP (1000) [ProductID]
      ,[ProductName]
      ,[Price]
,case 
	when price < 50 then 'low' 
	when price between 50 and 200 then 'meduim'
	else 'High'
end as price_category 
FROM [PortfolioProject_MarketingAnalytics].[dbo].[products]
