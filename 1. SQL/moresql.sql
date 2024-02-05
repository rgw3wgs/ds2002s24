-- Sakila Sample Database - Basic Queries

-- 1. Count of Films in the `film` Table
SELECT COUNT(*) AS 'Total Films' FROM film;

-- 2. List All Categories in the `category` Table
SELECT name AS 'Category Name' FROM category;

-- 3. Find All Customers with Last Names Starting with 'S'
SELECT first_name, last_name FROM customer WHERE last_name LIKE 'S%';

-- 4. Show the First 10 Records from the `actor` Table
SELECT * FROM actor LIMIT 10;
