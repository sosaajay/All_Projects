# 📊 Customer Churn Analysis Dashboard

## 📌 Project Overview
This project focuses on analyzing customer churn behavior in a subscription-based fitness and wellness service. The goal is to identify key patterns, trends, and factors influencing customer churn using SQL for data analysis and Power BI for visualization.

---

## 🧾 Dataset Description
The dataset includes the following key attributes:

- CustomerID  
- Name  
- Age  
- Gender  
- SubscriptionType (Monthly, Quarterly, Yearly)  
- SubscriptionDate  
- LastLoginDate  
- TotalSessions  
- FeedbackScore  
- IsChurned (1 = Churned, 0 = Active)  

---

## ⚙️ Tools & Technologies Used

- SQL (for data analysis)  
- Power BI (for dashboard visualization)  

---

## 📊 Dashboard Features

- KPI Cards:
  - Total Customers  
  - Churn Percentage  
  - Average Feedback Score  
  - Average Days Since Last Login  

- Visualizations:
  - Donut Chart (Active vs Churned Customers)  
  - Bar Chart (Churn Rate by Subscription Type)  
  - Line Chart (Monthly Churn Trend)  
  - Scatter Plot (Feedback Score vs Total Sessions)  

- Filters (Slicers):
  - Subscription Type  
  - Gender  
  - Age Group  

---

## 🔍 Key Insights

1. Customers with Monthly subscription plans have the highest churn rate, indicating lower retention in short-term plans.

2. Customers with less than 5 sessions are more likely to churn, showing low engagement as a major factor.

3. Customers with feedback scores below 5 tend to churn more frequently, indicating dissatisfaction.

4. Customers inactive for more than 60 days have a high probability of churn.

5. Scatter analysis shows that high sessions + high feedback = active customers, while low sessions + low feedback = churn risk.

6. Monthly churn trend shows fluctuations over time, indicating possible seasonal or behavioral changes.

---

## 📈 Conclusion

- Encourage long-term subscriptions (Quarterly/Yearly)  
- Improve customer engagement through sessions and follow-ups  
- Focus on improving service quality and feedback  
- Identify inactive users early and re-engage them  
- Use behavioral patterns to predict churn  

---

## 🏁 Final Outcome
The dashboard provides a clear, interactive view of customer behavior and churn patterns, helping businesses take data-driven decisions to improve customer retention.
