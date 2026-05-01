create DATABASE SUBRISK;
USE SUBRISK;

CREATE TABLE CustomerSubscriptions (
    CustomerID INT,
    Name VARCHAR(50),
    Age INT,
    Gender VARCHAR(10),
    SubscriptionType VARCHAR(20),
    SubscriptionDate DATE,
    LastLoginDate DATE,
    TotalSessions INT,
    FeedbackScore INT,
    IsChurned INT
);

-- Active vs Churned Customers by Subscription Type

SELECT 
    SubscriptionType,
    SUM(CASE WHEN IsChurned = 0 THEN 1 ELSE 0 END) AS Active_Customers,
    SUM(CASE WHEN IsChurned = 1 THEN 1 ELSE 0 END) AS Churned_Customers
FROM CustomerSubscriptions
GROUP BY SubscriptionType;


-- Average Feedback Score by Subscription Type and Gender

SELECT 
    SubscriptionType,
    Gender,
    ROUND(AVG(FeedbackScore),2) AS Avg_Feedback
FROM CustomerSubscriptions
GROUP BY SubscriptionType, Gender
ORDER BY SubscriptionType;


-- Customers with Low Engagement

SELECT *
FROM CustomerSubscriptions
WHERE TotalSessions < 5 
  AND FeedbackScore < 5;


-- nactive Customers (Last 60 Days)

SELECT *
FROM CustomerSubscriptions
WHERE DATEDIFF(CURDATE(), LastLoginDate) > 60;


-- Churn Rate by Subscription Type
SELECT 
    SubscriptionType,
    COUNT(*) AS Total_Customers,
    SUM(IsChurned) AS Churned_Customers,
    ROUND(SUM(IsChurned)*100.0/COUNT(*),2) AS Churn_Rate_Percentage
FROM CustomerSubscriptions
GROUP BY SubscriptionType;


-- Top 10 Longest Subscription Customers

SELECT *
FROM CustomerSubscriptions
ORDER BY SubscriptionDate ASC
LIMIT 10;


-- Age Group-wise Churn Analysis

SELECT 
    CASE 
        WHEN Age BETWEEN 18 AND 25 THEN '18-25'
        WHEN Age BETWEEN 26 AND 35 THEN '26-35'
        WHEN Age BETWEEN 36 AND 45 THEN '36-45'
        ELSE '45+'
    END AS Age_Group,
    COUNT(*) AS Total_Customers,
    SUM(IsChurned) AS Churned_Customers,
    ROUND(SUM(IsChurned)*100.0/COUNT(*),2) AS Churn_Rate
FROM CustomerSubscriptions
GROUP BY Age_Group
ORDER BY Age_Group;


-- KPI Summary 

SELECT 
    COUNT(*) AS Total_Customers,
    ROUND(SUM(IsChurned)*100.0/COUNT(*),2) AS Churn_Percentage,
    ROUND(AVG(FeedbackScore),2) AS Avg_Feedback,
    ROUND(AVG(DATEDIFF(CURDATE(), LastLoginDate)),2) AS Avg_Days_Since_Last_Login
FROM CustomerSubscriptions;

-- Monthly churn trend
SELECT 
    DATE_FORMAT(SubscriptionDate, '%Y-%m') AS Month,
    COUNT(*) AS Total_Customers,
    SUM(IsChurned) AS Churned
FROM CustomerSubscriptions
GROUP BY Month
ORDER BY Month;
