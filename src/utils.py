import json
import os
from pathlib import Path


def json_to_list(file_path):
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {path.absolute()}")

    with path.open(encoding="utf-8") as f:
        if os.path.getsize(file_path) > 0:
            return json.load(f)
        else:
            return []


# print(json_to_list("../data/test_operations.json"))
