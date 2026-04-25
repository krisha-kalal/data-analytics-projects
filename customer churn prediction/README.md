# 📊 Customer Churn Analysis (Machine Learning + EDA)

## 📌 Overview

This project focuses on analyzing customer churn behavior using data analysis and machine learning techniques. The goal is to identify patterns, understand why customers leave, and build a predictive model to estimate churn.

---

## 🎯 Objectives

* Clean and preprocess real-world customer data
* Perform exploratory data analysis (EDA)
* Identify key factors affecting churn
* Build and evaluate machine learning models
* Generate business insights for customer retention

---

## 📂 Dataset

* Telco Customer Churn Dataset
* Contains customer demographics, services, billing details, and churn status

---

## 🧹 Data Preprocessing

* Removed unnecessary columns (`customerID`)
* Converted `TotalCharges` to numeric
* Handled missing values using `dropna()`
* Encoded categorical variables (binary mapping + one-hot encoding)
* Converted target variable `Churn` → (Yes = 1, No = 0)

---

## 📊 Exploratory Data Analysis (EDA)

The following visualizations were created:

* Churn Distribution (Count Plot)
* Churn by Contract Type
* Monthly Charges vs Churn (Box Plot)
* Tenure vs Churn (Box Plot)
* Payment Method vs Churn (Stacked Bar Chart)

---

## 🤖 Machine Learning Models

### 1. Logistic Regression

* Used for baseline prediction
* Accuracy: ~78%
* Good for interpretability

### 2. Random Forest Classifier

* Captures complex relationships
* Improved overall performance balance

---

## 📈 Model Evaluation

* Accuracy Score
* Confusion Matrix
* Precision, Recall, F1-Score

Key Observation:

* Model performs better at predicting **non-churn customers**
* Moderate performance in predicting **churn customers**

---

## 🔍 Key Insights

* Customers with **month-to-month contracts** have the highest churn
* **Higher monthly charges** are associated with higher churn
* Customers with **short tenure** are more likely to churn
* **Electronic check payment method** shows highest churn rate
* Long-term contracts significantly reduce churn

---

## 💡 Business Recommendations

* Offer discounts or incentives for long-term contracts
* Improve experience for electronic payment users
* Target high-charge customers with retention offers
* Focus on retaining new customers (low tenure segment)

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

---

## 📁 Project Structure

```
├──  WA_Fn-UseC_-Telco-Customer-Churn.csv
├── churn analysis charts.twbx
├── cleaned_churn_data.csv
├── churn analysis lr.py
├── churn analysis rfc.py
├── README.md
```

---

## 🚀 How to Run

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
python churn analysis lr.py
python churn analysis rfc.py
```

---

## 📌 Conclusion

This project demonstrates how data analysis and machine learning can be used to understand customer behavior and reduce churn. The insights derived can help businesses improve customer retention strategies and increase profitability.

---
