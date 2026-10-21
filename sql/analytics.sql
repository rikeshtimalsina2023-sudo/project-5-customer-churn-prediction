-- Project 5 SQL analytics

SELECT COUNT(*) AS customers,
       ROUND(AVG(ChurnFlag) * 100, 2) AS churn_rate_percent
FROM customers;

SELECT Contract,
       COUNT(*) AS customers,
       ROUND(AVG(ChurnFlag) * 100, 2) AS churn_rate_percent
FROM customers
GROUP BY Contract
ORDER BY churn_rate_percent DESC;

SELECT InternetService,
       COUNT(*) AS customers,
       ROUND(AVG(ChurnFlag) * 100, 2) AS churn_rate_percent
FROM customers
GROUP BY InternetService
ORDER BY churn_rate_percent DESC;

SELECT PaymentMethod,
       COUNT(*) AS customers,
       ROUND(AVG(ChurnFlag) * 100, 2) AS churn_rate_percent
FROM customers
GROUP BY PaymentMethod
ORDER BY churn_rate_percent DESC;

SELECT TenureGroup,
       COUNT(*) AS customers,
       ROUND(AVG(ChurnFlag) * 100, 2) AS churn_rate_percent
FROM customers
GROUP BY TenureGroup
ORDER BY churn_rate_percent DESC;
