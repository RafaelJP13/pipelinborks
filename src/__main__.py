from extract import fetch_data
import json

def main():
    api_url = "https://api.fda.gov/drug/drugsfda.json"
    limit = 10
    data = fetch_data(api_url, limit)


    if data:
        print("Extracted data successfully.")

if __name__ == "__main__":
    main()