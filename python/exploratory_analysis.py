import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("data/sales_data_cleaned.csv")
print("Total Sales:",round(df.Sales.sum(),2))
print("Total Profit:",round(df.Profit.sum(),2))
print("Total Orders:",df.Order_ID.nunique())
print("\nSales by Category:\n",df.groupby("Category").Sales.sum().sort_values(ascending=False))
print("\nProfit by Region:\n",df.groupby("Region").Profit.sum().sort_values(ascending=False))
print("\nTop Products:\n",df.groupby("Product").Sales.sum().sort_values(ascending=False).head(10))
monthly=df.groupby("Month").Sales.sum()
monthly.plot(kind="line",figsize=(10,5))
plt.title("Monthly Sales Trend"); plt.xticks(rotation=45); plt.tight_layout()
plt.savefig("visualizations/monthly_sales_trend.png",dpi=150); plt.show()
