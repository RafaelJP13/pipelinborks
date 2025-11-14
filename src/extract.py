import requests
import json
from pathlib import Path
from datetime import datetime

def fetch_data(api_url: str, limit: int, output_dir: Path | None = None):
    """Fetches data from API and saves it in a JSON file"""

    timestamp = datetime.now().strftime("%d%m%Y%H%M%S")

    raw_dir = output_dir or (Path(__file__).parent / "data" / "raw")
    raw_dir.mkdir(parents=True, exist_ok=True)
    output_file = raw_dir / f"drugsfda_{timestamp}.json"

    params = {"limit": limit}

    try:
        print(f"Fetching data from {api_url}")
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        data = response.json()

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(
                    data,
                    f,
                    indent=2,
                    ensure_ascii=False
            )

        print(f"Data saved to {output_file}")
        return data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {api_url} | {e}")
        return None

