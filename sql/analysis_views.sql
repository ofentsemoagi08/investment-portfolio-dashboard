-- Investment Portfolio Analytics Dashboard
-- SQL reporting layer
-- Source table: transactions

CREATE OR REPLACE VIEW monthly_transaction_performance AS
SELECT
    year,
    month,
    year_month,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_transaction_value,
    AVG(amount) AS average_transaction_value,
    COUNT(DISTINCT customer_id) AS active_customers
FROM transactions
GROUP BY year, month, year_month
ORDER BY year, month;


CREATE OR REPLACE VIEW category_analysis AS
SELECT
    category,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_transaction_value,
    AVG(amount) AS average_transaction_value,
    COUNT(DISTINCT customer_id) AS unique_customers
FROM transactions
GROUP BY category
ORDER BY total_transaction_value DESC;


CREATE OR REPLACE VIEW customer_segment_analysis AS
SELECT
    customer_segment,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_transaction_value,
    AVG(amount) AS average_transaction_value,
    COUNT(DISTINCT customer_id) AS unique_customers
FROM transactions
GROUP BY customer_segment
ORDER BY total_transaction_value DESC;


CREATE OR REPLACE VIEW channel_analysis AS
SELECT
    channel,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_transaction_value,
    AVG(amount) AS average_transaction_value,
    COUNT(DISTINCT customer_id) AS unique_customers
FROM transactions
GROUP BY channel
ORDER BY total_transaction_value DESC;


CREATE OR REPLACE VIEW customer_activity AS
SELECT
    customer_id,
    customer_segment,
    account_type,
    city,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_transaction_value,
    AVG(amount) AS average_transaction_value,
    MIN(transaction_date) AS first_transaction_date,
    MAX(transaction_date) AS last_transaction_date
FROM transactions
GROUP BY
    customer_id,
    customer_segment,
    account_type,
    city
ORDER BY total_transaction_value DESC;


CREATE OR REPLACE VIEW monthly_category_trends AS
SELECT
    year,
    month,
    year_month,
    (year * 100 + month) AS year_month_sort,
    category,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_transaction_value,
    AVG(amount) AS average_transaction_value
FROM transactions
GROUP BY
    year,
    month,
    year_month,
    category
ORDER BY
    year,
    month,
    total_transaction_value DESC;
