import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("Coffee Product Analysis Dashboard")

# Load Data
df = pd.read_excel("Afficionado Coffee Roasters.xlsx")

# Revenue column
df["revenue"] = df["transaction_qty"] * df["unit_price"]

# Sidebar filters
st.sidebar.header("Filters")

category = st.sidebar.selectbox("Select Category", df["product_category"].unique())
store = st.sidebar.selectbox("Select Store Location", df["store_location"].unique())

filtered_df = df[
    (df["product_category"] == category) &
    (df["store_location"] == store)
]

# KPI Section
total_revenue = filtered_df["revenue"].sum()
total_qty = filtered_df["transaction_qty"].sum()

st.metric("Total Revenue", round(total_revenue, 2))
st.metric("Total Quantity Sold", int(total_qty))

# Top Products Chart
top_products = (
    filtered_df.groupby("product_detail")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig1 = px.bar(top_products, x="product_detail", y="revenue", title="Top Products by Revenue")
st.plotly_chart(fig1)

# Category Distribution
category_rev = df.groupby("product_category")["revenue"].sum().reset_index()

fig2 = px.pie(category_rev, names="product_category", values="revenue", title="Category Revenue Share")
st.plotly_chart(fig2)

# Scatter Plot (Volume vs Revenue)
scatter = df.groupby("product_detail").agg({
    "transaction_qty": "sum",
    "revenue": "sum"
}).reset_index()

fig3 = px.scatter(scatter, x="transaction_qty", y="revenue",
                  title="Sales vs Revenue",
                  hover_data=["product_detail"])

st.plotly_chart(fig3)

# Table
st.subheader("Product Data")
st.dataframe(filtered_df)