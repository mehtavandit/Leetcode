SELECT
    s.name
FROM SalesPerson S
where s.name not in(
    SELECT
        s.name
    FROM SalesPerson s
    LEFT JOIN ORDERS o on s.sales_id = o.sales_id
    LEFT JOIN Company c on o.com_id = c.com_id
    WHERE c.name = 'RED'
)