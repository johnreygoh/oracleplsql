-- fetch records on selected columns
--select orderid,productname,shipmode,shipdate from myorders;
--select orderid,productname,quantity from myorders;

-- get all records
--select * from myorders;

-- aggregate function
-- count rows
-- select count(id) from myorders;    

-- get sum of sales
-- select sum(sales) from myorders;

-- get distinct values of a column
--select distinct shipmode from myorders;
--select distinct category from myorders;
--select distinct subcategory from myorders;

-- get records filtered by column value
--select * from myorders where shipmode='First Class'; 
--select * from myorders where category='Furniture';
--select * from myorders where category='Technology' and shipmode='Same Day';

--select 
--    orderid,
--    productname,
--    sales,
--    category,
--    region
--from myorders
--where region='Central';

-- and / or
-- "first class" AND "central" AND "Furniture"
select 
    orderid,
    productname,
    shipmode,
    region,
    category,
    sales
from myorders
where shipmode='First Class'
and region='Central'
and category='Furniture';
    
--select 
--    count(*)
--from myorders
--where shipmode='First Class'
--and region='Central'
--and category='Furniture';

-- "Technology" or "Furniture"  and shipmode "Second Class"
--select 
--    orderid,
--    productname,
--    category,
--    shipmode
--from myorders
--where 
--    (category='Furniture' and shipmode='Second Class')
--or 
--    (category='Technology' and shipmode='Second Class');


-- where (=,>,>=,<,<=,<>,like,between)
--select * from myorders where sales < 5000;
--select * from myorders where sales > 5000;
--select * from myorders where sales BETWEEN 5000 and 7000;
--select * from myorders where orderdate < date '2017-1-1';

--select 
--    orderid,
--    customername,
--    orderdate
--from myorders 
--where orderdate 
--between 
--    date '2017-1-1' 
--and 
--    date '2017-3-1';


-- show records not equal to central region
--select * from myorders where region <> 'Central';

--select
--    *
--from myorders
--where region <> 'Central'
--and shipmode <> 'Same Day';

-- customer name starting with S
--select 
--    *
--from myorders
--where customername like '%S%';

--select
--    *
--from myorders
--where customername like 'S%'
--or customername like 'M%';

-- more wildcard (_)
-- example Tam, Tom, Tim, Tym, Tum
-- T%m, Tamim, temam,temadeem
-- T_m

--select 
--    *
--from myorders
--where customername like 'S_n%';

-- using "order by"
--select * 
--from myorders 
--order by sales desc;

--select *
--from myorders
--order by customername;

-- multiple column sorting
--select orderid,shipmode,customername,sales 
--from myorders
--order by shipmode desc,customername,sales desc;

-- filter then sort
--select orderid,shipmode,customername,sales
--from myorders
--where sales >= 1000
--order by shipmode,customername,sales desc;

-- column aliases
--select 
--    orderid as id,
--    customername as customer,
--    shipmode as shipping,
--    sales as sales_amount
--from myorders;

-- select from a set of given values
-- orderid 10,12,22,25,100
--select *
--from myorders
--where id in (10,12,22,25,100)
--and segment='Consumer';








