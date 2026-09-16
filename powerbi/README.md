# Power BI Dashboard Guide
1. Open Power BI Desktop.
2. Get Data → Text/CSV → `data/sales_data_cleaned.csv`.
3. Create an Executive Overview page with cards for Total Sales, Total Profit, Total Orders and Average Order Value.
4. Add a monthly Sales Trend line chart, Sales by Category column chart, Sales by Region bar chart, Top 10 Products bar chart and Customer Type chart.
5. Add Year and Region slicers.

Useful DAX:
Total Sales = SUM(sales_data_cleaned[Sales])
Total Profit = SUM(sales_data_cleaned[Profit])
Total Orders = DISTINCTCOUNT(sales_data_cleaned[Order_ID])
Average Order Value = DIVIDE([Total Sales],[Total Orders])
Profit Margin = DIVIDE([Total Profit],[Total Sales])
