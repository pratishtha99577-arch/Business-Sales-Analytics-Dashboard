import pandas as pd
raw=pd.read_csv("data/sales_data_raw.csv")
print("Shape:",raw.shape)
print("Missing values:\n",raw.isna().sum())
print("Duplicate rows:",raw.duplicated().sum())
df=raw.drop_duplicates().copy()
df["Customer_Type"]=df["Customer_Type"].fillna(df["Customer_Type"].mode()[0])
df["Order_Date"]=pd.to_datetime(df["Order_Date"])
df["Month"]=df["Order_Date"].dt.to_period("M").astype(str)
df["Year"]=df["Order_Date"].dt.year
df["Profit_Margin"]=(df["Profit"]/df["Sales"]).fillna(0)
df.to_csv("data/sales_data_cleaned.csv",index=False)
print("Saved cleaned dataset.")
