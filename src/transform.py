import json
import pandas as pd
from pathlib import Path

def transform_raw_data(raw_file_path: Path):

    """Transforms raw data from API and get important fields"""

    with open(raw_file_path, "r", encoding = "utf-8") as raw_file:
        raw_data = json.load(raw_file)

    cleaned_raw_data = []

    for item in raw_data.get("results", []):
        sponsor_name = item.get("sponsor_name")

        products = item.get("products", [])

        for product in products:
            product_name = product.get("brand_name", None)

            active_ingredients = product.get("active_ingredients", [])

            ingredients_list = []

            for ingredient in active_ingredients:

                    ingredient_name = ingredient.get("name", 'Unknown')
                    ingredient_strength = ingredient.get("strength", 0)

                    ingredients_list.append({

                        "name": ingredient_name,
                        "strength": ingredient_strength,

                    })

            cleaned_raw_data.append({
                "sponsor_name": sponsor_name,
                "product_name": product_name,
                "ingredients": ingredients_list,

            })

    return cleaned_raw_data

def save_processed_data(data, output_name="processed_data.json"):
    """Saves processed data to Json file"""
    processed_dir = Path(__file__).parent / "data" / "processed"
    processed_dir.mkdir(parents=True, exist_ok=True)

    output_path = processed_dir / output_name

    with open(output_path, "w", encoding = "utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Saved processed data to {output_path}")