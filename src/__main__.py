from transform import transform_raw_data, save_processed_data
from pathlib import Path

def main():
    raw_dir = Path(__file__).parent / "data" / "raw"
    raw_file = raw_dir / "drugsfda_08112025153540.json"

    if not raw_file.exists():
        print("No raw data found")
        return

    cleaned_data = transform_raw_data(raw_file)
    save_processed_data(cleaned_data, "processed_drugsfda_08112025153540.json")

if __name__ == "__main__":
    main()