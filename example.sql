USE my_first_db;
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    country VARCHAR(50),
    age INT,
    phone VARCHAR(15)
);

USE my_first_db;

INSERT INTO customers (customer_id, first_name, last_name, country, age, phone)
VALUES 
(1, 'John', 'Doe', 'USA', 28, '555-0199'),
(2, 'Jane', 'Smith', 'UK', 34, '555-0143'),
(3, 'Rahul', 'Sharma', 'India', 22, '555-0177');
/* selecting all coloumns */
select * from customers;
/* select firstname and lastname columns */
select first_name,last_name
from customers;
/* using where */
SELECT first_name
FROM customers
WHERE Age >= 21;

/* select with distinct clause */
SELECT DISTINCT Country
FROM customers;
/* select statement with having clause */
SELECT Country, COUNT(*) AS customer_count
FROM customers
GROUP BY Country
HAVING COUNT(*) >= 1;

/* select statement with orderby clause */
SELECT * FROM customers ORDER BY age DESC;  

CREATE TABLE employee (
    empid INT PRIMARY KEY,
    name VARCHAR(50),
    dept VARCHAR(50),
    salary INT
);

INSERT INTO employee VALUES (1, 'Rahul', 'IT', 50000);
INSERT INTO employee VALUES (2, 'Anita', 'HR', 45000);
INSERT INTO employee VALUES (3, 'John', 'Finance', 60000);
INSERT INTO employee VALUES (4, 'Sara', 'IT', 55000);
INSERT INTO employee VALUES (5, 'David', 'Marketing', 48000);

select * from employee;
/* examples of where clause */
CREATE TABLE emp (
    empid INT PRIMARY KEY,
    name VARCHAR(50),
    country VARCHAR(50),
    age INT,
    mobile_no VARCHAR(15)
);

INSERT INTO emp VALUES (1, 'Amit', 'India', 25, '9876543210');
INSERT INTO emp VALUES (2, 'Sara', 'USA', 30, '9123456780');
INSERT INTO emp VALUES (3, 'John', 'UK', 28, '9988776655');
INSERT INTO emp VALUES (4, 'Meera', 'India', 22, '8877665544');
INSERT INTO emp VALUES (5, 'David', 'Canada', 35, '7766554433');

select * from emp;
/* where clause with logical operators */
SELECT * FROM emp WHERE age=22;

SELECT empid, name, country FROM emp WHERE age > 21;

SELECT * FROM emp
WHERE age BETWEEN 22 AND 26;

SELECT * FROM emp
WHERE name LIKE 'L%';

SELECT name FROM emp
WHERE age IN (21,23);

SELECT empid, name, dept, salary
FROM employee
ORDER BY
salary DESC;








