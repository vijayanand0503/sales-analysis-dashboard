# ADF Pipelines

This folder contains Azure Data Factory pipeline JSON files used in the project.

## Pipeline Details

- **sales-pipeline.json**
  - Orchestrates the complete data workflow
  - Steps involved:
    1. Copy data from source (CSV in Blob Storage)
    2. Transform data using Data Flow
    3. Process data using Databricks Notebook

## Purpose

The pipeline automates the end-to-end data movement and transformation process, enabling data to be prepared for analysis in Power BI.
