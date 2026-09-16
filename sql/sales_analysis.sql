CREATE DATABASE IF NOT EXISTS business_sales;
USE business_sales;
-- Import sales_data_cleaned.csv as sales_data.
SELECT ROUND(SUM(Sales),2) AS total_sales FROM sales_data;
SELECT ROUND(SUM(Profit),2) AS total_profit FROM sales_data;
SELECT Category,ROUND(SUM(Sales),2) AS sales FROM sales_data GROUP BY Category ORDER BY sales DESC;
SELECT Region,ROUND(SUM(Profit),2) AS profit FROM sales_data GROUP BY Region ORDER BY profit DESC;
SELECT Product,ROUND(SUM(Sales),2) AS sales FROM sales_data GROUP BY Product ORDER BY sales DESC LIMIT 10;
SELECT Year,Month,ROUND(SUM(Sales),2) AS sales FROM sales_data GROUP BY Year,Month ORDER BY Year,Month;
SELECT Customer_Type,COUNT(DISTINCT Customer_ID) AS customers,ROUND(SUM(Sales),2) AS sales,
ROUND(SUM(Profit),2) AS profit FROM sales_data GROUP BY Customer_Type ORDER BY sales DESC;
SELECT Discount,ROUND(SUM(Sales),2) AS sales,ROUND(SUM(Profit),2) AS profit
FROM sales_data GROUP BY Discount ORDER BY Discount;
