# Write your MySQL query statement below
WITH TEMP AS (SELECT product_id, 'store1' as store, store1 as price
FROM Products where store1 is not Null

UNION ALL

SELECT product_id, 'store2' as store, store2 as price
FROM Products where store2 is not Null

UNION ALL

SELECT product_id, 'store3' as store, store3 as price
FROM Products where store3 is not Null)


SELECT * from temp order by product_id;