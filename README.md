This system implements a structured ETL (Extract–Transform–Load) pipeline that retrieves regulatory drug data from the FDA’s public API, stores the raw responses for auditability, transforms and standardizes the information into a clean and consistent schema, and finally loads the processed data into a MySQL database.

The pipeline automates data ingestion, enforces data quality through transformation steps, maintains a historical raw data layer, and delivers a curated dataset optimized for querying, reporting, and downstream analytical workflows.
