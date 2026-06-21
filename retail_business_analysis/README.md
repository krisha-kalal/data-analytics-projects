# 🏪 Retail Business Analysis (Python + Oracle SQL)

## 📌 Overview

This project focuses on analyzing retail sales and profit data to uncover business insights using Python and Oracle SQL. The analysis helps identify top-performing categories, regions, customers, and products while understanding the impact of discounts on profitability.

---

## 🎯 Objectives

* Clean and preprocess retail sales data
* Perform exploratory data analysis (EDA)
* Analyze sales and profit trends
* Execute SQL queries for business insights
* Visualize key business metrics
* Generate actionable recommendations

---

## 📂 Dataset

**Sample Superstore Dataset**

Contains:

* Customer information
* Product details
* Sales transactions
* Profit data
* Regional information
* Discounts and quantities

---

## 🧹 Data Preprocessing

* Loaded dataset using Pandas
* Handled encoding issues during import
* Checked for missing values
* Verified data types
* Converted date columns to datetime format
* Created additional Year and Month columns
* Cleaned column names for Oracle SQL compatibility

---

## 📊 Exploratory Data Analysis (EDA)

The following visualizations were created:

### 1. Sales by Category

Compares revenue generated across product categories.

### 2. Profit by Category

Identifies the most profitable product categories.

### 3. Sales by Region

Shows revenue distribution across regions.

### 4. Profit by Region

Highlights regional profitability performance.

### 5. Monthly Sales Trend

Analyzes sales performance over time.

### 6. Discount vs Average Profit

Examines how discounts affect profitability.

---

## 🗄️ SQL Analysis

The following business queries were executed using Oracle SQL:

- 1. Total Number of Records
```sql
SELECT COUNT(*) FROM SUPERSTORE;
```
- 2. Total Sales
```sql
SELECT SUM(SALES) FROM SUPERSTORE;
```
- 3. Total Profit
```sql
SELECT SUM(PROFIT) FROM SUPERSTORE;
```
- 4. Sales by Category
- 5. Profit by Category
- 6. Sales by Region
- 7. Profit by Region
- 8. Top 10 Customers by Sales
- 9. Top 10 Products by Profit
- 10. Monthly Sales Trend
- 11. Discount Impact on Profit

---

## 🔍 Key Insights

* Technology generated the highest sales revenue.
* Technology was also the most profitable category.
* The West region recorded the highest sales and profit.
* Furniture generated high sales but comparatively lower profit.
* Heavy discounts often resulted in negative profits.
* A small group of customers contributed significantly to overall sales.
* Certain products consistently generated higher profits than others.
* Sales fluctuated across months, indicating seasonal purchasing patterns.

---

## 💡 Business Recommendations

* Increase focus on high-performing Technology products.
* Review discount strategies to prevent profit loss.
* Expand successful sales strategies used in the West region.
* Promote high-profit products more aggressively.
* Monitor low-profit categories and optimize pricing strategies.
* Use customer purchasing behavior to improve targeted marketing.

---

## 🛠️ Technologies Used

### Python

* Pandas
* NumPy
* Matplotlib

### Database

* Oracle SQL Developer
* Oracle XE

### Development Environment

* Jupyter Notebook
* Visual Studio Code

---

## 📁 Project Structure

```text
retail_business_analysis/
│
├── dataset/
│   └── superstore.csv
│
├── retail_analysis.ipynb
├── sql_queries.sql
├── superstore_clean.csv
└── README.md
```

---

## 🚀 How to Run

### Install Dependencies

```bash
pip install pandas numpy matplotlib
```

### Run Notebook

```bash
jupyter notebook retail_analysis.ipynb
```

### Run SQL Queries

1. Open Oracle SQL Developer
2. Import `superstore_clean.csv`
3. Execute queries from `sql_queries.sql`

---

## 📌 Conclusion

This project demonstrates how Python and Oracle SQL can be combined to analyze retail business performance. Through data cleaning, visualization, and SQL-based analysis, meaningful insights were generated to support better business decisions related to sales, profitability, customer behavior, and discount strategies.
