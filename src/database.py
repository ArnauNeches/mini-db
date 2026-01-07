# Main database functions, create a new table, show all tables or delete a existing table. Only works with dictionaries.
from datetime import date
from pathlib import Path

def create_table(schema: dict, name:str) -> dict:
    """
    Create a table given a dictionary with the field names and their types and a string with the table name.
    """
    new_table = {}
    new_table["meta"] = {"name": name, "created_at": str(date.today()), "last_modified": str(date.today()), "id_counter": 0}
    new_table["schema"] = schema
    new_table["data"] = {}

    return new_table

def join_table_contents(schema: dict, metadata: dict, data: dict) -> dict:
    """
    Given a table schema, data and metadata, joins them into a single unified dictionary.
    """
    table = {}
    table["schema"] = schema
    table["meta"] = metadata
    table["data"] = data

    return table

def tables_names() -> set[str]:
    """
    Return the name of all existing tables.
    """
    path = Path("data/")
    return {f.stem for f in path.glob("*.json")}
