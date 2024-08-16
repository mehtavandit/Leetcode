CREATE FUNCTION getNthHighestSalary(@N INT) 
RETURNS INT
AS
BEGIN
    DECLARE @result INT;

    WITH cte AS (
        SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS r 
        FROM employee
    )
    
    SELECT @result = salary
    FROM cte 
    WHERE r = @N;

    RETURN @result;
END;
