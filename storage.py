# Main storage functions, read/write json files.
import json
import os
import utils

def store_table(table: dict):
    """
    Gets a table in dictionary format and stores it as a json file.
    """

    table_name = table["meta"]["name"]

    with open(f"data/{table_name}.json", "w", encoding="utf-8") as out_file:
        json.dump(table, out_file, sort_keys=True, indent=4, ensure_ascii=False)

def read_table(table_name: str) -> dict:
    """
    Returns a dictionary from a read json table given the name of it.
    """
    try:
        with open(f"data/{table_name}.json", "r") as input_file:
            return json.load(input_file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}
    
def delete_table(table_name: str):
    """
    Delete a table given its name.
    """
    print(f"You are about to delete the table {table_name}. You will lose all its contents.")
    if not utils.acknoledge_continue():
        return 
    
    os.remove(f"data/{table_name}.json")
    