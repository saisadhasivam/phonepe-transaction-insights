SELECT USER(), CURRENT_USER(), DATABASE();

CREATE DATABASE phonepe;

USE phonepe;

CREATE TABLE aggregated_transaction (
    id INT PRIMARY KEY AUTO_INCREMENT,
    year INT,
    quarter INT,
    country VARCHAR(50),
    state VARCHAR(50),
    transaction_type VARCHAR(100),
    transaction_count BIGINT,
    transaction_amount DOUBLE
);

CREATE TABLE aggregated_user (
    id INT PRIMARY KEY AUTO_INCREMENT,
    year INT,
    quarter INT,
    country VARCHAR(50),
    state VARCHAR(50),
    registered_users BIGINT,
    app_opens BIGINT
);

CREATE TABLE aggregated_insurance (
    id INT PRIMARY KEY AUTO_INCREMENT,
    year INT,
    quarter INT,
    country VARCHAR(50),
    state VARCHAR(50),
    insurance_count BIGINT,
    insurance_amount DOUBLE
);

SHOW TABLES;

SELECT COUNT(*) FROM aggregated_transaction;

SELECT COUNT(*) FROM aggregated_user;

SELECT COUNT(*) FROM aggregated_insurance;


CREATE TABLE IF NOT EXISTS map_transaction (
    id INT PRIMARY KEY AUTO_INCREMENT,
    year INT,
    quarter INT,
    state VARCHAR(100),
    transaction_type VARCHAR(100),
    transaction_count BIGINT,
    transaction_amount DOUBLE
);

USE phonepe;
SHOW TABLES;

SELECT COUNT(*) FROM aggregated_transaction;
SELECT COUNT(*) FROM aggregated_user;
SELECT COUNT(*) FROM aggregated_insurance;
SELECT COUNT(*) FROM map_transaction;

# How does PhonePe transaction volume grow year by year?

SELECT 
    year,
    SUM(transaction_amount) AS total_amount,
    SUM(transaction_count) AS total_count
FROM aggregated_transaction
GROUP BY year
ORDER BY year;

#Which states contribute most to PhonePe revenue?

SELECT
    state,
    SUM(transaction_amount) AS total_revenue
FROM map_transaction
GROUP BY state
ORDER BY total_revenue DESC
LIMIT 10;


#What kind of transactions dominate PhonePe?

SELECT
    transaction_type,
    SUM(transaction_amount) AS total_amount
FROM aggregated_transaction
GROUP BY transaction_type
ORDER BY total_amount DESC;

#Is PhonePe user adoption accelerating?

SELECT
    year,
    SUM(registered_users) AS users
FROM aggregated_user
GROUP BY year
ORDER BY year;

#When does insurance become significant?

SELECT
    year,
    SUM(insurance_amount) AS total_amount
FROM aggregated_insurance
GROUP BY year
ORDER BY year;

# Which states grow fastest over time?

SELECT
    state,
    year,
    SUM(transaction_amount) AS total_amount
FROM map_transaction
GROUP BY state, year
ORDER BY year, total_amount DESC;
