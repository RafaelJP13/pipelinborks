import json
from unittest.mock import patch, MagicMock
from pathlib import Path
from src.extract import fetch_data

def test_fetch_data_create_files(tmp_path):

    mock_data = {
        "results": [
            {
                "sponsor_name": "Pfizer Inc.",
                "product_name": "LIPITOR",
                "active_ingredients": [
                  {"name": "MICONAZOLE NITRATE", "strength": "2%,4%"}
                ]
            },
        ]
    }

    with patch("src.extract.requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = mock_data
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        api_url = "https://api.fake-url.com/drugsfda"
        result = fetch_data(api_url, 10)

        #FIX

        assert result == mock_data

    created_file = list(tmp_path.glob("drugsfda_*.json"))
    assert len(created_file) == 1
