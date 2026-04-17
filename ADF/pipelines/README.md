# ADF Pipelines

This folder contains Azure Data Factory pipeline JSON files used in the project.

## 📌 Pipeline: sales-pipeline.json

This pipeline orchestrates the complete end-to-end data workflow.

### 🔄 Workflow Steps
1. **Copy Data**
   - Ingests raw sales data from Azure Blob Storage (CSV)

2. **Data Flow**
   - Cleans and transforms data (filtering, formatting, aggregation)

3. **Databricks Notebook**
   - Performs advanced processing using PySpark
   - Stores processed data in Delta format

### 🎯 Purpose
This pipeline automates the data ingestion, transformation, and processing workflow, preparing data for visualization in Power BI.
