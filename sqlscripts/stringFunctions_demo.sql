-- string functions

select
    id,
    orderid,
    substr(orderid,9,6) as TransactionNo,
    substr(orderid,4,4) as OrderYear,
    upper(substr(category,1,4)),
    initcap(customername),
    replace(shipmode,'Class',''),
    upper(productname),
    id
    ||'-'
    ||substr(orderid,4,4)
    ||'-'
    ||substr(orderid,9,6)
    ||'-'
    ||upper(substr(category,1,3)) as TransactionCode

from myorders;

-- transactionCode
-- id-orderyear-transactiono-category(first3chars)



