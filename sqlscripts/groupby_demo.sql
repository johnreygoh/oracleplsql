-- total sales
--select 
--    sum(sales)
--from myorders;

-- total sales per region
--select 
--    region,
--    round(sum(sales),2) as TOTAL_SALES
--from myorders
--group by region
--order by TOTAL_SALES desc;

-- more group by examples
-- shipmode, total sales, average sales, max sales, min sales, count
--select 
--    shipmode,
--    round(sum(sales),2) as TotalSales,
--    round(avg(sales),2) as AverageSales,
--    round(max(sales),2) as MaxSales,
--    round(min(sales),2) as MinSales,
--    count(*) as NoOfTransactions
--from myorders
--group by shipmode
--order by TotalSales desc;


-- total quantity sold per category
--select 
--    category,
--    sum(quantity) as QuantitySold
--from myorders
--group by category
--order by QuantitySold desc;

-- select from table WHERE <condition>
-- group by condition (having)
--select 
--    region,
--    sum(sales) as TotalSales
--from myorders
--group by region
--having sum(sales) > 500000;

-- customer names quantity < 100
select
    customername,
    sum(quantity) as QuantityPurchased
from myorders
group by customername
having sum(quantity) > 100
order by QuantityPurchased desc;








    



