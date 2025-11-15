# Drug Data ETL Pipeline (OpenFDA + ANVISA → MySQL)

This project implements a structured ETL (Extract–Transform–Load) pipeline that retrieves regulatory drug data from two major public sources:

- **OpenFDA (USA)**
- **ANVISA — Brazilian Registered Medicines Dataset**

The system stores raw API responses for auditability, transforms and standardizes the information into a consistent schema, and loads the processed data into a MySQL database for analytics, reporting, and downstream applications.
