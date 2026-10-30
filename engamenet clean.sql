SELECT  [EngagementID]
      ,[ContentID]
      ,[ContentType]
      ,[Likes]
      ,[EngagementDate]
      ,[CampaignID]
      ,[ProductID]
      ,[ViewsClicksCombined]
  FROM [PortfolioProject_MarketingAnalytics].[dbo].[engagement_data]



select 
	EngagementID , 
	ContentID , 
	CampaignID , 
	ProductID , 
	UPPER(ContentType) contentType ,
	likes , 
	LEFT(ViewsClicksCombined, CHARINDEX('-', ViewsClicksCombined) - 1) AS Views , 
	SUBSTRING(ViewsClicksCombined, CHARINDEX('-', ViewsClicksCombined) + 1, LEN(ViewsClicksCombined)) AS clicks ,
	EngagementDate
from engagement_data	
where ContentType != 'NEWSLETTER'

