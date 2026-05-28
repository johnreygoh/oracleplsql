-- create table1
create table table1 
(
    -- setting columns, data type and constraints
    id NUMBER(3) PRIMARY KEY,
    itemname VARCHAR(50) UNIQUE,
    quantity NUMBER(4),
    itemprice NUMBER(5,2)
);

