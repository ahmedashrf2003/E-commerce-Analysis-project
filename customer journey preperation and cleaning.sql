-- customer journey data cleaning and preperation 

-- check the duplicates 
select * 
from customer_journey 

select count (journeyId)
from customer_journey 

select  count(distinct journeyID)
from customer_journey

-- removing duplicates
with cte_clean as 
(
	select 
		JourneyID, 
		ROW_NUMBER() over(partition by journeyID order by journeyID) as row_num
	from customer_journey
)
delete from cte_clean 
where row_num > 1 


-- checking null values  
select 
	JourneyID, 
	CustomerID, 
	ProductID , 
	VisitDate , 
	stage , 
	Action , 
case 
	when Duration is null then (select round(AVG(duration), 0 ) from customer_journey)
	else Duration 
end as Duration 
from customer_journey