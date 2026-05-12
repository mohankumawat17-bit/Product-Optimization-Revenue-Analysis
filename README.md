# ☕ Product Optimization & Revenue Contribution Analysis

## 📌 Project Overview
This project analyzes retail transaction data for Afficionado Coffee Roasters to understand product performance, revenue contribution, and menu optimization opportunities.

The objective is to identify top-performing products, measure category-wise revenue contribution, and highlight low-performing items that may require review or removal.

---

## 🎯 Business Problem
Afficionado Coffee Roasters has detailed transaction-level data but lacks clear visibility into:

- Which products generate the highest revenue
- Which products sell frequently but contribute little revenue
- Which categories drive overall business performance
- Which products have minimal business impact

This analysis helps support data-driven decisions for menu optimization and profitability improvement.

---

## 🎯 Project Objectives

### Primary Objectives
- Identify top-selling and least-selling products
- Calculate revenue contribution by product and category
- Measure revenue concentration using Pareto analysis

### Secondary Objectives
- Identify hero products
- Highlight underperforming products
- Support menu simplification and optimization

---

## 📂 Dataset Information
The dataset contains transaction-level sales data with the following key columns:

- `transaction_id`
- `transaction_time`
- `transaction_qty`
- `unit_price`
- `store_location`
- `product_category`
- `product_type`
- `product_detail`

---

## 🛠 Tools & Technologies Used
- Python
- Pandas
- Streamlit
- Plotly
- Excel

---

## 📊 Analysis Performed
- Data loading and validation
- Revenue calculation (`transaction_qty × unit_price`)
- Top-selling product analysis
- Revenue contribution analysis
- Category-wise revenue analysis
- Product type analysis
- Pareto (80/20) analysis

---

## 📈 Key Insights
- Coffee and Tea contribute approximately **66%** of total revenue.
- Premium products generate high revenue despite moderate sales volume.
- A small number of products drive a significant share of total revenue.
- Low-performing categories include:
  - Flavours
  - Loose Tea
  - Packaged Chocolate

---

## 💡 Recommendations
- Focus on high-revenue products.
- Review or remove low-performing products.
- Simplify the menu to improve operational efficiency.
- Introduce combo offers for top-performing products.

---

## 📊 Streamlit Dashboard Features
- KPI cards (Total Revenue, Total Quantity Sold)
- Category filter
- Store location filter
- Top products by revenue chart
- Category revenue distribution
- Sales vs Revenue scatter plot
- Detailed product data table

---

## 🚀 Live Dashboard
https://mohankumawat17-bit-product-optimization-revenue-anal-app-l86tlz.streamlit.app/

---

## 📁 Project Structure
```text
Product-Optimization-Revenue-Analysis/
│── app.py
│── analysis.py
│── Afficionado Coffee Roasters.xlsx
│── Research_Paper.pdf
│── Executive_Summary.pdf
│── README.md
│── requirements.txt
