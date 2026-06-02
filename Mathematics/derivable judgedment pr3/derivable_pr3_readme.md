# 📊 Inferential Statistics Project (Health Dataset Analysis)

## 🎯 Objective
The objective of this project is to apply **inferential statistical techniques** on a health-related dataset and analyze how different factors such as smoking, age, BMI, glucose level, and diabetes are related.

---

## 📚 Theory

### 📌 Inferential Statistics
Inferential statistics helps us draw conclusions about a large population using a smaller sample of data. Instead of analyzing everyone, we analyze a subset and generalize the results.

---

### 📌 Hypothesis Testing
A hypothesis is a statement about a population parameter.

- **Null Hypothesis (H₀):** Assumes no effect or no difference.
- **Alternative Hypothesis (H₁):** Assumes there is an effect or difference.

Example:
- H₀: Mean glucose levels of smokers and non-smokers are equal.
- H₁: Mean glucose levels are different.

---

### 📌 Confidence Interval
A confidence interval gives a range where the true population parameter is expected to lie.

---

### 📌 P-value
- p-value < 0.05 → Reject H₀  
- p-value > 0.05 → Fail to reject H₀  

---

### 📌 Errors in Hypothesis Testing
- **Type I Error:** Rejecting a true null hypothesis  
- **Type II Error:** Failing to reject a false null hypothesis  

---

### 📌 Statistical Tests Used

#### 1. Z-Test
Used for large sample sizes (n > 30) when population standard deviation is known.

#### 2. T-Test
Used to compare means of two groups when sample size is small.

#### 3. Chi-Square Test
Used to find relationship between categorical variables.

#### 4. ANOVA
Used to compare means of three or more groups.

---

### 📌 Covariance
Measures the direction of relationship between two variables.

- Positive → both increase together  
- Negative → one increases, other decreases  
- Zero → no relationship  

---

### 📌 Correlation
Measures strength and direction of relationship between variables.

- Positive correlation  
- Negative correlation  
- No correlation  

---

## 🛠️ Tools & Libraries Used
- Python 🐍  
- Pandas  
- NumPy  
- Matplotlib  
- SciPy  

---

## 📂 Dataset
The dataset used is:  
`health_dataset.csv`

It includes:
- Age  
- BMI  
- Blood Pressure  
- Glucose Level  
- Smoking Status  
- Diabetes Status  
- Age Groups  

---

## 📊 Analysis & Visualizations

---

## 1️⃣ Confidence Interval: Mean Blood Pressure

A 95% confidence interval was calculated to estimate the mean blood pressure of the population.

### 📈 Result Visualization
<img src="Mean_Blood_Pressure.png" width="500"/>

---

## 2️⃣ T-Test: Glucose Levels (Smokers vs Non-Smokers)

This test compares whether smoking status affects glucose levels.

### 📊 Result Visualization
<img src="Smokers_vs_Non_Smokers.png" width="500"/>

---

## 3️⃣ Chi-Square Test: Smoking Status vs Diabetes

This test checks whether smoking is associated with diabetes.

### 📊 Result Visualization
<img src="Smoking_Status_vs_Diabetes.png" width="500"/>

---

## 4️⃣ ANOVA: Blood Pressure Across Age Groups

This test compares blood pressure across different age groups.

### 📊 Result Visualization
<img src="Blood_Pressure_Across_Age_Groups.png" width="500"/>

---

## 5️⃣ Correlation & Covariance: Age vs BMI

This analysis shows how age and BMI are related.

### 📊 Result Visualization
<img src="Age_vs_BMI.png" width="500"/>

---

## 📌 Final Observations

- Smoking has a measurable effect on glucose levels (based on statistical testing).
- Blood pressure varies across different age groups.
- Smoking and diabetes show a statistical relationship.
- Age and BMI show a measurable correlation.
- Visualizations help clearly understand patterns in health data.

---

## 📉 Conclusion

This project demonstrates how **inferential statistics** can be used to analyze health data and make meaningful conclusions. Using hypothesis testing, confidence intervals, and correlation analysis, we can identify important relationships between health factors.

All results were interpreted using a significance level of **α = 0.05**.

---

## 🖼️ Visual Summary (All Plots Used)

- Mean_Blood_Pressure.png  
- Smokers_vs_Non_Smokers.png  
- Smoking_Status_vs_Diabetes.png  
- Blood_Pressure_Across_Age_Groups.png  
- Age_vs_BMI.png  

---

## 🚀 Outcome

This project successfully demonstrates:
- Statistical reasoning  
- Data visualization  
- Hypothesis testing  
- Real-world health data analysis  

---

⭐ *End of Project*