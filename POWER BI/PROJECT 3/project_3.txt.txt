Sales Data Analysis Project 
Project Overview

In this project, I worked on sales data analysis using Power BI. I used multiple datasets and built a complete data model to perform analysis and understand business performance clearly.

Data Import

I imported the following datasets into Power BI:

Sales_Fact
Returns_Fact
Customer_Dim
Product_Dim
Date_Dim
Region_Dim

These datasets were used to build the overall data model for analysis.

Data Modeling

I created relationships between fact tables and dimension tables to connect the data properly.
I made sure that all tables were correctly linked so that the analysis would give accurate results.

Using this model, I was able to analyze data based on:

Customer
Product
Region
Date
Calculated Columns

I created the following calculated columns in the model:

Profit = SalesAmount - Cost
Return Flag → used to identify whether a product was returned
Customer Full Name → created by combining First Name and Last Name
DAX Measures

I created multiple DAX measures to perform calculations:

Total Sales using SUM
Total Cost
Total Profit calculated as Sales - Cost
Return Rate using DIVIDE
Average Sale

To manage all these measures properly, I created a separate Measure Table.

Filter Context and Functions

I used important DAX functions to control filter context:

CALCULATE → used to modify the filter context
ALL → used to remove filters from the data
FILTER → used to apply custom filtering conditions

These functions helped in creating dynamic and flexible calculations.

Other DAX Functions Used

In addition to the main functions, I also used:

Aggregation functions: SUM, AVERAGE, MAX
Logical functions: IF, SWITCH
Counting function: DISTINCTCOUNT
Text function: CONCATENATE
Date functions: YEAR, MONTH
Time Intelligence

I applied time intelligence functions for time-based analysis:

Year-to-Date using TOTALYTD
Previous Year comparison using SAMEPERIODLASTYEAR
Running Total using CALCULATE along with DATESBETWEEN
Visualization (Matrix)

I created a Matrix visual in Power BI to analyze and compare the data based on:

Region
Product Category
Customer Segment
Year and Month

This visual helps to compare performance in a structured way, similar to a pivot table.

Key Learnings

From this project, I learned:

How to build a data model
How to create and use DAX calculations
Understanding of filter context
Performing time-based analysis
Creating useful data visualizations
Important Note

Quick measures such as Year-over-Year and Previous Month are not working properly in this project due to an issue with the Date table.