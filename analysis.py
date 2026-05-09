import pandas as pd

# Excel file load
df = pd.read_excel("Afficionado Coffee Roasters.xlsx")

# First 5 rows show
print(df.head())

# Columns check
print(df.columns)

# Revenue column add
df["revenue"] = df["transaction_qty"] * df["unit_price"]

# Check output
print(df[["transaction_qty", "unit_price", "revenue"]].head())

# Top selling products (by quantity)
top_products = df.groupby("product_detail")["transaction_qty"].sum().sort_values(ascending=False)

print("Top 10 Products by Sales Volume:")
print(top_products.head(10))

# Top products by revenue
top_revenue = df.groupby("product_detail")["revenue"].sum().sort_values(ascending=False)

print("\nTop 10 Products by Revenue:")
print(top_revenue.head(10))

total_revenue = df["revenue"].sum()

revenue_share = (df.groupby("product_detail")["revenue"].sum() / total_revenue) * 100

revenue_share = revenue_share.sort_values(ascending=False)

print("\nRevenue Contribution (%):")
print(revenue_share.head(10))

# Category-wise revenue
category_revenue = df.groupby("product_category")["revenue"].sum().sort_values(ascending=False)

print("\nCategory Revenue:")
print(category_revenue)

total_revenue = df["revenue"].sum()

category_pct = (category_revenue / total_revenue) * 100

print("\nCategory Revenue %:")
print(category_pct)

product_type_analysis = df.groupby(["product_category", "product_type"])["revenue"].sum().sort_values(ascending=False)

print("\nProduct Type Revenue:")
print(product_type_analysis.head(10))

pareto = df.groupby("product_detail")["revenue"].sum().sort_values(ascending=False)

pareto_df = pareto.reset_index()
pareto_df.columns = ["product", "revenue"]

pareto_df["cum_revenue"] = pareto_df["revenue"].cumsum()
pareto_df["cum_pct"] = pareto_df["cum_revenue"] / pareto_df["revenue"].sum() * 100

print(pareto_df.head(10))

