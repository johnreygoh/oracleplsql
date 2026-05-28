-- add record(s) using all columns
--insert into t_items 
--(id,itemname,quantity,itemprice)
--values 
--(1,'a',100,25);

-- add multiple records in 1 statement (v23+)
insert into t_items
values  
(2,'b',100,35),
(3,'c',90,67),
(4,'d',80,80),
(5,'e',30,200),
(6,'f',45,55),
(7,'g',300,6);

-- add multiple records in 1 statement (older than v23+)
insert all
into t_items values (2,'b',100,35)
into t_items values (3,'c',90,67)
into t_items values (4,'d',80,80)
into t_items values (5,'e',30,200)
into t_items values (6,'f',45,55)
into t_items values (7,'g',300,6)
select * from dual
;








