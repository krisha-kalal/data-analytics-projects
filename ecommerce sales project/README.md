# 📊 E-commerce Sales Analysis Dashboard

## 📌 Project Overview

This project focuses on analyzing an e-commerce sales dataset to uncover key business insights related to revenue trends, product performance, and regional sales distribution. The analysis was performed using Python (Pandas) for data cleaning and Tableau for interactive dashboard visualization.

---

## 🎯 Objectives

* Analyze sales data to identify revenue trends
* Determine top-performing product categories
* Evaluate regional sales performance
* Understand customer type contribution (B2B vs B2C)
* Detect operational issues like order cancellations

---

## 🛠️ Tools & Technologies

* Python (Pandas, NumPy)
* Tableau (Dashboard & Visualization)
* CSV Dataset

---

## 🧹 Data Cleaning Steps

* Removed unnecessary columns (`index`, `Unnamed: 22`)
* Converted `Date` column to datetime format
* Handled missing values:

  * Dropped rows with missing `Amount` and location data
  * Filled categorical null values (e.g., promotion, courier status)
* Converted postal codes to string format
* Removed duplicate records
* Created new features: `Year`, `Month`

---

## 📊 Key Insights

### 📈 Sales Trend

* Sales peaked in **April**, followed by a gradual decline in May and June
* Indicates possible seasonal demand pattern

### 🛍️ Product Performance

* **Set category** generated the highest revenue
* Traditional wear (Kurta, Sets) dominates sales

### 🌍 Regional Analysis

* **Maharashtra** and **Karnataka** are top-performing states
* Indicates strong demand in these regions

### 🧑‍🤝‍🧑 Customer Type

* Revenue is heavily driven by **B2C customers**
* Minimal contribution from B2B segment

### ⚠️ Operational Insight

* High number of **cancelled orders (~10K)**
* Suggests potential issues in delivery or customer experience

---

## 📊 Dashboard Features

* KPI Cards (Total Revenue, Total Orders)
* Monthly Sales Trend (Line Chart)
* Category-wise Sales (Bar Chart)
* State-wise Sales Distribution
* B2B vs B2C Revenue (Pie Chart)
* Order Status Analysis
* Interactive Filters (Category, State)

---

## 📂 Project Structure

```
Ecommerce-Sales-Analysis/
│
├── dataset
    ├── Amazon Sale Report Cleaned.csv
    ├── Amazon Sale Report.csv
├── amazon sales analysis.twbx
├── analysis.py
└── README.md
```

---

## 🚀 Conclusion

This project demonstrates how raw sales data can be transformed into meaningful insights that help businesses make informed decisions regarding inventory, marketing strategies, and operational improvements.

---

## 🔗 Author

Krisha Kalal
Data Analyst Inte | Python | SQL | Data Visualization

---
