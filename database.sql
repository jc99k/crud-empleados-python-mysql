CREATE DATABASE IF NOT EXISTS empleados_crud;

USE empleados_crud;

CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL,
    birthday DATE NOT NULL
);
