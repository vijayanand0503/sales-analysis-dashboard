# Import libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create Spark session
spark = SparkSession.builder.appName("Sales Analysis").getOrCreate()

# Load data from Azure Data Lake
df = spark.read.format("csv") \
    .option("header", "true") \
    .load("abfss://sales-data@<your-storage-account>.dfs.core.windows.net/sales_data.csv")

# Display data
df.show()

# Convert data types
df = df.withColumn("Sales", col("Sales").cast("int")) \
       .withColumn("Cost", col("Cost").cast("int"))

# Create temp view
df.createOrReplaceTempView("sales_table")

# Total sales by category
category_sales = spark.sql("""
SELECT Category, SUM(Sales) AS Total_Sales
FROM sales_table
GROUP BY Category
""")

category_sales.show()

# Orders by region
region_orders = spark.sql("""
SELECT Region, COUNT(*) AS Orders
FROM sales_table
GROUP BY Region
""")

region_orders.show()

# Save processed data
df.write.format("delta") \
    .mode("overwrite") \
    .save("abfss://sales-data@<your-storage-account>.dfs.core.windows.net/processed-data")
