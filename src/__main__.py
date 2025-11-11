from transform import transform_raw_data, save_processed_data
from pathlib import Path
from src.db import init_db
from src.extract import fetch_data
from src.load import load_processed_data

def main():

    init_db()
    fetch_data("https://api.fda.gov/drug/drugsfda.json", 100)

    base_dir = Path(__file__).parent
    raw_dir = base_dir / "data" / "raw"
    processed_dir = base_dir / "data" / "processed"
    json_files = list(raw_dir.glob("*.json"))

    if not json_files:
        print("No .json files found")
        return

    newest_filename = json_files[-1]
    raw_file = raw_dir / newest_filename

    if not raw_file.exists():
        print("No raw data found")
        return

    cleaned_data = transform_raw_data(raw_file)
    timestamp_raw_data = newest_filename.stem.replace("drugsfda_", "")
    output_filename = f"processed_drugsfda_{timestamp_raw_data}.json"
    save_processed_data(cleaned_data, output_filename)
    load_raw_path = processed_dir / output_filename

    load_processed_data(load_raw_path)

if __name__ == "__main__":
    main()