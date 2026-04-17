df = spark.read.format("csv") \
    .option("header", "true") \
    .load("abfss://sales-data@salesdatastore1234.dfs.core.windows.net/sales_data.csv")

df.show()
df.write.format("delta") \
.mode("overwrite") \
.save("abfss://sales-data@salesdatastore1234.dfs.core.windows.net/sales-data")
df.write.format("delta") \
.mode("overwrite") \
.saveAsTable("sales_table")
spark.sql("""
SELECT * FROM sales_table""").show()
spark.sql("""
SELECT Category, SUM(Sales) AS Total_Sales
FROM sales_table
GROUP BY Category""").show()
spark.sql("""
SELECT Region, COUNT(*) AS Orders
FROM sales_table
GROUP BY Region""").show() 
