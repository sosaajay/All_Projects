# 📊 Data Preprocessing and Feature Engineering Project

## 🚀 Customer Churn Analysis Using Data Analytics

---

## 📌 Project Overview

This project focuses on **Data Acquisition, Data Understanding, Data Cleaning, Exploratory Data Analysis (EDA), Feature Engineering, and Data Profiling** using a real-world customer churn dataset.

The main purpose of this project is to transform raw customer data into meaningful insights by applying different data preprocessing techniques and visualization methods.

The project demonstrates how data is collected from multiple sources, cleaned, analyzed, and prepared for machine learning applications.

---

# 🎯 Problem Statement

A consumer insights company provides customer behavior data collected from different sources.

The objective is to analyze customer purchase patterns and build a foundation for predicting customer churn.

The machine learning problem statement is:

**"Predict whether a customer will churn or continue using the service based on customer behavior, spending patterns, and subscription information."**

---

# 🎯 Project Objectives

The main objectives of this project are:

✅ Understand fundamentals of Data Analysis  
✅ Collect data from multiple sources  
✅ Perform data preprocessing and cleaning  
✅ Analyze customer behavior using EDA  
✅ Create visual insights from data  
✅ Perform feature engineering  
✅ Generate data profiling insights  
✅ Prepare data for machine learning workflow  

---

# 📂 Dataset Information

## Dataset Name

Customer Churn Dataset

## Dataset Features

| Feature | Description |
|---|---|
| Customer ID | Unique customer identifier |
| Age | Customer age |
| Gender | Customer gender |
| Item Purchased | Purchased product |
| Category | Product category |
| Purchase Amount | Customer purchase value |
| Previous Purchases | Number of previous purchases |
| Review Rating | Customer rating |
| Subscription Status | Subscription information |
| Payment Method | Payment details |
| Purchase Date | Date of purchase |
| Churn | Customer churn status |

---

# 🧠 Part A: Fundamentals

## 📈 What is Data Analysis?

Data Analysis is the process of collecting, cleaning, transforming, and interpreting data to discover useful information.

It helps organizations understand customer behavior, identify patterns, and make data-driven decisions.

In this project, customer purchase data is analyzed to understand spending behavior and churn patterns.

---

# 🔄 Data Science Project Lifecycle

A complete Data Science workflow includes:

## 1. Problem Understanding 🎯

Define the business problem and decide what needs to be predicted or analyzed.

## 2. Data Acquisition 📥

Collect data from different sources such as:

- CSV
- JSON
- SQL Database
- API

## 3. Data Cleaning 🧹

Remove errors, handle missing values, remove duplicates, and correct data formats.

## 4. Exploratory Data Analysis 📊

Analyze data using statistics and visualization techniques.

## 5. Feature Engineering ⚙️

Create meaningful features from existing data to improve analysis.

## 6. Model Preparation 🤖

Prepare clean data for machine learning algorithms.

## 7. Evaluation ✅

Check the quality and usefulness of the results.

---

# 🤖 Machine Learning Problem Statement

The objective is to predict customer churn using customer behavior data.

Input Features:

- Age
- Gender
- Purchase Amount
- Previous Purchases
- Review Rating
- Subscription Status

Target Variable:

**Churn**

0 → Customer Retained  
1 → Customer Churned

This is a classification problem because the output contains two categories.

---

# 🔢 Tensor

A Tensor is a multi-dimensional data structure used in Machine Learning and Deep Learning.

Types of tensors:

### Scalar (0D)
Single value data.

### Vector (1D)
A list of values.

### Matrix (2D)
Data represented in rows and columns.

### Higher Dimension Tensor (3D+)

Used in advanced applications like image processing and deep learning.

---

# 📥 Part B: Data Acquisition

Data was collected using multiple sources.

## 📄 CSV Data

CSV files store data in rows and columns.

In this project:

`EcommData_CSV.csv`

was used as the main dataset source.

Loaded using Pandas library.

---

## 🗂 JSON Data

JSON stores information in key-value format.

In this project:

`EcommData_JSON_5000.json`

was used to demonstrate JSON data loading.

---

## 🛢 SQL Database

SQL databases store structured data in tables.

In this project:

`EcommData_SQL.db`

was used.

SQLite connection was created and customer data was retrieved using SQL queries.

---

## 🌐 API Data

API allows communication between applications.

Customer related API data was fetched and converted into a Pandas DataFrame for analysis.

---

# 🧹 Part C: Data Understanding and Cleaning

Before analysis, the dataset was examined and cleaned.

## Initial Data Exploration

Performed:

```python
df.head()
```

Shows first records.

```python
df.info()
```

Shows columns and data types.

```python
df.describe()
```

Provides statistical summary.

---

# Data Quality Checks

Performed:

## Missing Value Detection

Checked missing values using:

```python
df.isnull().sum()
```

---

## Duplicate Detection

Checked duplicate records using:

```python
df.duplicated().sum()
```

---

## Data Type Checking

Verified correct data formats.

---

# 📊 Part D: Exploratory Data Analysis (EDA)

EDA helps understand patterns and relationships in data.

---

# 🔹 Univariate Analysis

Analysis of a single variable.

Performed analysis on:

- Age Distribution
- Purchase Amount Distribution
- Churn Distribution

Purpose:

To understand individual feature behavior.

---

# 🔹 Bivariate Analysis

Analysis between two variables.

Performed:

## Gender vs Churn

Used to understand whether gender affects churn.

## Category vs Churn

Used to analyze customer category behavior.

## Purchase Amount vs Churn

Used to compare spending patterns.

---

# 🔹 Multivariate Analysis

Multiple variables were analyzed together.

Methods used:

## Correlation Heatmap

Shows relationships between numerical features.

## Pair Plot

Shows interaction between multiple features.

---

# ⚙️ Part E: Feature Engineering

A new feature was created:

## Purchase Per History

Formula:

Purchase Amount / Previous Purchases


This feature helps understand customer spending behavior compared to purchase history.

---

# 📑 Part F: Data Profiling

Data profiling provides detailed information about the dataset.

It includes:

✅ Missing values  
✅ Data types  
✅ Statistical information  
✅ Duplicate records  
✅ Correlation analysis  

Profiling helps identify data quality problems before machine learning.

---

# 🛠 Technologies Used

## Programming Language

🐍 Python

## Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Requests
- SQLite3
- JSON

## Tools

- Jupyter Notebook
- Visual Studio Code

---

# 📁 Project Structure

```
Data_Profiler_Project/

│
├── EcommData_CSV.csv
│
├── EcommData_JSON_5000.json
│
├── EcommData_SQL.db
│
├── Data_Profiler_Project.ipynb
│
├── README.md
│
└── screenshots/
```

---

# 📈 Key Insights

From analysis:

✅ Customer spending behavior can affect churn  
✅ Purchase patterns help identify customer trends  
✅ Subscription type influences customer retention  
✅ Feature relationships can be identified using correlation analysis  
✅ Data preprocessing improves data quality  

---

# ✅ Expected Outcomes

After completing this project:

✔ Learned multi-source data acquisition  
✔ Performed data cleaning  
✔ Applied EDA techniques  
✔ Created visual analysis  
✔ Generated profiling insights  
✔ Prepared data for machine learning  

---

# 🚀 Conclusion

This project demonstrates the complete workflow of a Data Analytics project.

Customer data was collected from multiple sources, cleaned, explored, visualized, and transformed into useful insights.

The project provides practical understanding of data preprocessing and feature engineering techniques used in real-world machine learning applications.

---

## 👨‍💻 Author

**Ayush**

Junior Data Analyst Project

**Data Preprocessing and Feature Engineering**