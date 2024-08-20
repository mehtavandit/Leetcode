# Write your MySQL query statement below
WITH FirstQuaterSales AS(
    SELECT DISTINCT product_id
    FROM sales
    WHERE sale_date between '2019-01-01' AND '2019-03-31'
),
OTHERSALES As(
    SELECT DISTINCT product_id
    FROM sales
    WHERE sale_date < '2019-01-01' OR sale_date > '2019-03-31'
)

SELECT p.product_id, p.product_name
FROM product p
JOIN FirstQuaterSales fqs
ON p.product_id = fqs.product_id
LEFT JOIN OTHERSALES oth
ON fqs.product_id = oth.product_id
where oth.product_id is NULL;