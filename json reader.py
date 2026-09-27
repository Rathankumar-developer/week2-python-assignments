"""
Assignment 3: JSON File Reader
Load JSON data & print formatted output.
"""

import json
import os


def create_sample_json(filepath):
    sample_data = {
        "students": [
            {"name": "Asha Rao", "roll_number": 101, "marks": 88},
            {"name": "Vikram Singh", "roll_number": 102, "marks": 92},
            {"name": "Meera Iyer", "roll_number": 103, "marks": 79},
        ]
    }
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(sample_data, f, indent=4)
    print(f"Sample JSON file created at '{filepath}'.")


def load_json(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def print_formatted(data, indent=0):
    prefix = "  " * indent
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                print(f"{prefix}{key}:")
                print_formatted(value, indent + 1)
            else:
                print(f"{prefix}{key}: {value}")
    elif isinstance(data, list):
        for i, item in enumerate(data, start=1):
            print(f"{prefix}Item {i}:")
            print_formatted(item, indent + 1)
    else:
        print(f"{prefix}{data}")


def main():
    filepath = input("Enter the path of the JSON file: ").strip()

    if not os.path.exists(filepath):
        print(f"File '{filepath}' not found.")
        create_sample = input("Create a sample JSON file at this path? (y/n): ").strip().lower()
        if create_sample == "y":
            create_sample_json(filepath)
        else:
            print("Exiting without processing.")
            return

    try:
        data = load_json(filepath)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON file. {e}")
        return

    print("\n--- Formatted JSON Output ---")
    print_formatted(data)


if __name__ == "__main__":
    main()
