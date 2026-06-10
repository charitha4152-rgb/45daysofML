CREATE DATABASE company_db;
USE company_db;
CREATE TABLE Employee (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    dept VARCHAR(50),
    salary DECIMAL(10,2)
);

INSERT INTO Employee (id, name, dept, salary)
VALUES
(1, 'Alice', 'IT', 60000),
(2, 'Bob', 'HR', 50000),
(3, 'Charlie', 'Finance', 70000),
(4, 'David', 'IT', 65000),
(5, 'Emma', 'ML', 80000);

##GROUP BY is used to combine rows that have the same value in a column into a single group.
SELECT
    dept,
    COUNT(*) AS total_employees,
    SUM(salary) AS total_salary,
    AVG(salary) AS average_salary
FROM Employee
GROUP BY dept;

## filter groups after grouping
SELECT dept, AVG(salary) AS average_salary
FROM Employee
GROUP BY dept
HAVING AVG(salary) > 60000;
