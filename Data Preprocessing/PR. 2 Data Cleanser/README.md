# 🏥 Healthcare Patient Data Cleaning Project

## Data Preprocessing & Feature Engineering — Missing Value Imputation & Outlier Handling

This project simulates the role of a **Data Analyst at a healthcare company**. The raw patient
health dataset contains **missing values** and **outliers** caused by inconsistent reporting
and measurement errors. The goal is to clean the dataset using multiple missing-data
imputation methods and outlier-handling techniques so it becomes suitable for downstream
machine learning — predicting **heart disease risk**.

---

## 📁 Project Files

| File | Description |
|---|---|
| `patient_health_records.csv` | Raw dataset (1000 patients) with intentionally injected missing values and outliers |
| `healthcare_data_cleansing_final.ipynb` | Jupyter notebook containing the full, executed data-cleaning workflow (Part A, B, C) |
| `cleaned_health_data.csv` | Final, machine-learning-ready cleaned dataset |
| `README.md` | This file — full project documentation |

---

## 📊 Dataset Structure

| Field Name | Data Type | Description | Missingness / Outliers |
|---|---|---|---|
| `patient_id` | String/Int | Unique identifier for each patient | No missing, no outliers |
| `age` | Integer | Age of the patient (in years) | Missing values in some records |
| `gender` | Categorical | Male / Female | Missing values |
| `region` | Categorical | North / South / East / West | Missing values |
| `bmi` | Float | Body Mass Index (weight/height²) | Missing values + outliers (very high/low BMI) |
| `blood_pressure` | Float | Average systolic blood pressure (mmHg) | Outliers (extreme high values) |
| `cholesterol` | Float | Cholesterol level (mg/dL) | Missing values + outliers (extreme low/high) |
| `glucose` | Float | Fasting glucose level (mg/dL) | Missing values + outliers (very high spikes) |
| `disease_risk` | Binary Int | Target variable: 0 = Low Risk, 1 = High Risk | No missing, used as ML target |

**Dataset size:** 1000 rows × 9 columns

---

## 🧭 Project Workflow

The notebook is organized into three parts, matching the original project brief:

### Part A — Handling Missing Values

| Step | Technique | Column(s) Used On |
|---|---|---|
| 1 | Load dataset & inspect | — |
| 2 | Missing value summary report (count + %) | All columns |
| 3 | Simple Imputer (Numerical — mean) | `bmi`, `cholesterol` |
| 4 | Simple Imputer (Categorical — most frequent) | `region` |
| 5 | Most Frequent Imputation | `gender` |
| 6 | Missing Indicator + Random Sample Imputation | `glucose` |
| 7 | KNN Imputer (multivariate) | `age`, `bmi`, `cholesterol`, `glucose` |
| 8 | MICE Algorithm (Iterative Imputer / chained equations) | `age`, `bmi`, `cholesterol`, `glucose` (+ mode-fill for `gender`, `region`) |

### Part B — Handling Outliers

| Step | Technique | Approach |
|---|---|---|
| 9 | Z-score Method | Removes rows where any numeric column has \|z\| ≥ 3 |
| 10 | IQR Method | Removes rows outside Q1 − 1.5×IQR to Q3 + 1.5×IQR |
| 11 | Percentile Method | Caps values below the 1st and above the 99th percentile |
| 12 | Winsorization | Caps the most extreme 5% of values on each tail |

### Part C — Final Clean Dataset

| Step | Description |
|---|---|
| 13 | Combine the best techniques (**MICE** for missing values + **IQR** for outliers) into one final, clean dataset |
| — | Before vs after comparison (shape, mean, std, min/max) |
| — | Final written report / observations |

---

## ✅ Results Summary

- **Missing values:** Reduced from hundreds of missing entries across `age`, `gender`,
  `region`, `bmi`, `cholesterol`, and `glucose` down to **0 missing values**.
- **Outliers:** Extreme/erroneous BMI, blood pressure, cholesterol, and glucose readings
  were identified and removed using the IQR method after MICE imputation.
- **Final shape:** Reduced row count compared to the original 1000 rows (extreme outlier
  rows removed), with much tighter standard deviations across numeric columns — meaning
  more consistent, trustworthy data.
- **Target variable (`disease_risk`)** was preserved unchanged throughout, ready for use
  in a downstream classification model.

---

## 🏆 Which Methods Worked Best (and why)

**Best Imputation Method — MICE (Multiple Imputation by Chained Equations)**
MICE models each numeric column as a function of the other correlated columns
(age, bmi, blood pressure, cholesterol, glucose), so imputed values stay consistent
with a patient's overall health profile. This preserves relationships between variables
far better than simple mean/mode imputation, which imputes each column in isolation.

**Best Outlier Method — IQR (Interquartile Range)**
IQR doesn't assume a normal distribution, which makes it robust for slightly skewed
medical measurements like cholesterol and glucose. Unlike Winsorization or Percentile
capping (which keep every row but distort the tails), IQR cleanly removes genuinely
extreme/erroneous records while keeping the rest of the distribution intact.

**How Data Cleaning Improved Usability**
- Dataset now has **zero missing values** — works directly with any ML algorithm.
- Extreme/impossible readings (e.g. BMI > 60, glucose > 350) no longer distort feature
  scaling or distance-based models (KNN, SVM, etc.).
- Standard deviation dropped noticeably across numeric columns after cleaning —
  data is now tighter and more consistent.
- The dataset is fully **machine-learning ready** for predicting `disease_risk`.

---

## 🛠️ Tools & Libraries Used

- **Python 3**
- `pandas`, `numpy` — data handling
- `scikit-learn` — `SimpleImputer`, `KNNImputer`, `IterativeImputer` (MICE)
- `scipy` — `stats.zscore`, `mstats.winsorize`

---

## ▶️ How to Run

1. Keep `patient_health_records.csv` in the same folder as the notebook.
2. Open `healthcare_data_cleansing_final.ipynb` in Jupyter Notebook / JupyterLab / Google Colab.
3. Run all cells from top to bottom (**Cell → Run All**).
4. The final cleaned dataset will be saved as `cleaned_health_data.csv` in the same folder.

```bash
pip install pandas numpy scikit-learn scipy
jupyter notebook healthcare_data_cleansing_final.ipynb
```

---

## 📌 Notes

- All missing values and outliers in the raw dataset were **synthetically injected** to
  simulate realistic healthcare reporting/measurement errors, for the purpose of this
  data-cleaning exercise.
- Suitable assumptions (imputation strategy, outlier thresholds) were made in line with
  standard data-cleaning practice for healthcare datasets.
