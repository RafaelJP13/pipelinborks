import json
from pathlib import Path
from src.db import get_session
from src.models.product import Product

def load_processed_data(processed_file: Path):

    if not processed_file.exists():
        print("File not found {processed_file}")
        return

    with open(processed_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not data:
        print("No data found")
        return

    with get_session() as session:
        for item in data:
            ingredients = item.get("ingredients", [])

            for ing in ingredients:


                product = Product(

                    sponsor_name = item.get("sponsor_name"),
                    product_name = item.get("product_name"),
                    ingredient_name = ing.get("name"),
                    ingredient_strength = ing.get('strength'),
                )

                session.add(product)