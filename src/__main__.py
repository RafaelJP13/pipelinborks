from extract import fetch_data

def main():
    api_url = "https://api.fda.gov/drug/drugsfda.json"
    data = fetch_data(api_url, 10)

    if data:
        print("Extracted data successfully.")

if __name__ == "__main__":
    main()