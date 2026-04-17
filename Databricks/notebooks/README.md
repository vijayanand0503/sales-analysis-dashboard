# 📒 Databricks Notebooks

## 🔹 Overview

This folder contains PySpark notebooks used for data processing and analysis in Azure Databricks.

---

## 📂 Files

* **sales_notebook.py / .dbc**

  * Main notebook for data processing
  * Reads data from Azure Data Lake
  * Performs transformations
  * Executes SQL queries for analysis

---

## ⚙️ Processing Steps

### 1. Data Loading

* Data is loaded from Azure Data Lake Storage using PySpark
* CSV format with header enabled

### 2. Data Transformation

* Converted columns (Sales, Cost) to integer
* Created temporary view: `sales_table`

### 3. Data Analysis

* Total Sales by Category
* Orders by Region

### 4. Data Storage

* Data written in **Delta format**
* Saved to Data Lake and as table (`sales_table`)

---

## 🧠 Key Queries Used

```sql id="kbr0vp"
SELECT Category, SUM(Sales) AS Total_Sales
FROM sales_table
GROUP BY Category;
```

```sql id="w4t9nx"
SELECT Region, COUNT(*) AS Orders
FROM sales_table
GROUP BY Region;
```

---

## 📸 Output

The notebook generates:

* Data preview (df.show())
* Aggregated sales results
* Region-wise order counts

---

## 🚀 Notes

* Ensure correct Azure storage path before running
* Replace `<your-storage-account>` with actual value
* Notebook can be executed directly in Databricks workspace

---

## 👤 Author

Vijay Anand J
