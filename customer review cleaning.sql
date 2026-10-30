select * from customer_reviews

select 
	MIN(rating) as min_rating , 
	max(Rating) as max_rating ,
	AVG(rating) as avg_rating
from customer_reviews


select 
	ReviewID , 
	CustomerID , 
	ProductID , 
	ReviewDate , 
	Rating ,
	replace(ReviewText , '  ', ' ' ) as review

from customer_reviews