-- SQL-команды для создания таблиц

-- Создание таблицы employees
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    title VARCHAR(100) NOT NULL,
    birth_date DATE NOT NULL,
    notes TEXT
);

-- Создание таблицы customers
CREATE TABLE customers (
    customer_id VARCHAR(5) PRIMARY KEY,
    company_name VARCHAR(50) NOT NULL,
    contact_name VARCHAR(50) NOT NULL
);

-- Создание таблицы orders
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id VARCHAR(5) REFERENCES customers(customer_id) NOT NULL,
    employee_id INT REFERENCES employees(employee_id) NOT NULL,
    order_date DATE NOT NULL,
    ship_city VARCHAR(50) NOT NULL
);
