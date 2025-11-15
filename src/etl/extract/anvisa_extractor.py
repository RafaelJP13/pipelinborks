import requests
import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime

env_path = Path(__file__).resolve().parents[3] / '.env'
load_dotenv(env_path)

def download_anvisa_csv():

    url_anvisa_csv = os.getenv("API_ANVISA_URL")
    output_path = Path(__file__).resolve().parents[2] / 'data'/ 'anvisa' / 'raw'
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    print(f'Downloading {url_anvisa_csv}')
    resp = requests.get(url_anvisa_csv, verify=False)
    resp.raise_for_status()

    with open(output_path / f'anvisa.{timestamp}.csv', 'wb') as f:
        for chunk in resp.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    print(f'Downloaded {url_anvisa_csv}')


if __name__ == '__main__':
    download_anvisa_csv()