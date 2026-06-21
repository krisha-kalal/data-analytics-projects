# Retail Business Analysis using Python and Oracle SQL

## Project Overview

This project analyzes retail sales data from a Superstore dataset containing nearly 10,000 transactions. The goal is to identify business insights related to sales performance, profitability, customer behavior, regional trends, product categories, and discount impact.

The project combines Python for data analysis and visualization with Oracle SQL for business query analysis.

---

## Tools and Technologies

- Python
- Pandas
- Matplotlib
- Jupyter Notebook
- Oracle SQL
- Oracle SQL Developer

---

## Dataset Information

- Dataset: Superstore Sales Dataset
- Total Records: 9,994
- Features: 21 Columns
- Data Type: Retail Sales Transactions

Key columns include:

- Order Date
- Customer Name
- Category
- Sub-Category
- Region
- Sales
- Profit
- Discount
- Quantity

---

## Data Preparation

### Python

- Loaded dataset using Pandas
- Handled encoding issues
- Converted date columns into datetime format
- Created Year and Month features
- Renamed columns for Oracle SQL compatibility
- Exported cleaned dataset for database import

### Oracle SQL

- Imported cleaned dataset into Oracle Database
- Performed business analysis using SQL queries

---

## SQL Analysis Performed

### Total Records
### Total Sales
### Total Profit
### Category-wise Sales
### Category-wise Profit
### Region-wise Sales
### Region-wise Profit
### Top 10 Customers by Sales
### Top 10 Products by Profit
### Monthly Sales Trend
### Discount Impact on Profit
### Discounts Resulting in Losses

---

## Key Findings

### Overall Business Performance

- Total Sales: $2.29 Million
- Total Profit: $286,397

### Category Performance

- Technology generated the highest sales.
- Technology also produced the highest profit.
- Furniture generated high sales but relatively low profit.

### Regional Performance

- West region recorded the highest sales.
- West region also generated the highest profit.

### Customer Insights

- A small group of customers contributed significantly to total revenue.
- Identifying top customers can help improve retention strategies.

### Product Insights

- Several products generated exceptionally high profits.
- Product profitability varies significantly across categories.

### Discount Analysis

- Discounts between 0% and 20% remained profitable on average.
- Discounts above 30% frequently resulted in negative profits.
- Excessive discounting reduced business profitability.

---

## Visualizations Created

### Sales by Category
- Bar Chart

### Profit by Category
- Bar Chart

### Sales by Region
- Bar Chart

### Profit by Region
- Bar Chart

### Monthly Sales Trend
- Line Chart

### Discount vs Average Profit
- Line Chart

---

## Business Recommendations

- Focus on Technology products for revenue growth.
- Review Furniture pricing and cost strategies.
- Prioritize West region expansion opportunities.
- Reduce excessive discount campaigns.
- Develop loyalty programs for top customers.

---

## Project Structure

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

## Author

Krisha Kalal
