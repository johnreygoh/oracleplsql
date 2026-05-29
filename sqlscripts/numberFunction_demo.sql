-- number function

--select 
--    orderid,
--    round(sales,2),
--    ceil(sales),
--    floor(sales),
--    sales * 0.2 as "20pctOfSales"
--from myorders;

select 
    customername,
    orderid,
    sales as originalSales,
    sales + 1000 as modifiedSales,
    sales + (sales * 0.1) as markedUpSales
from myorders;



