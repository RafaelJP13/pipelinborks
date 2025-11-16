# Medication Data ETL Pipeline (OpenFDA + ANVISA → MySQL)

This project implements a structured ETL (Extract–Transform–Load) pipeline that retrieves regulatory drug data from two major public sources:

- **OpenFDA (USA)**
- **ANVISA — Brazilian Registered Medicines Dataset**

The system stores raw API responses for auditability, transforms and standardizes the information into a consistent schema, and loads the processed data into a MySQL database for analytics, reporting, and downstream applications.

# Structure

pipelinborks/
├── data/
│   ├── fda/
│   │   ├── raw/                 # Raw OpenFDA JSON files
│   │   └── processed/           # Cleaned and transformed FDA data
│   └── anvisa/
│       ├── raw/                 # Raw ANVISA CSV files
│       └── processed/           # Cleaned and transformed ANVISA data
├── docs/
├── src/
│   └── pipelinborks/
│       ├── __init__.py
│       ├── etl/
│       │   ├── extract/
│       │   │   └── anvisa_extractor.py
│       │   ├── transform/
│       │   │   └── anvisa_transform.py
│       │   └── load/
│       ├── pipelines/
│       ├── models/
│       │   └── medicament.py        
│       └── utils/
├── tests/
│   ├── extract/
│   ├── transform/
│   └── load/
├── .env.example                    # Template for required env vars
├── .gitignore
├── README.md

├── pyproject.toml                  # Modern project config (or requirements.txt)
└── main.py                         # Entrypoint to execute pipelines
