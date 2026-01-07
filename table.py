# Table operations, edit, insert or delete. Functions take dictionaries as arguments, never read directly.
import pyperclip
import json
from pathlib import Path

def show_table_contents(table: dict):   
    """
    Show data and metadata of a table.
    """
    table_name = table["meta"]["name"]
    print(f"Table {table_name} contents: ")
    print("\n")
    print(f"Table {table_name} metadata: ")
    print(table["meta"])
    print(f"Table {table_name} schema: ")
    print(table["schema"])
    print(f"Table {table_name} data: ")
    print(table["data"])


def table_contents(table: dict):
    """
    Returns the schema, metadata and data of a table as separate dictionaries.
    """
    return table["schema"], table["meta"], table["data"]

def copy_to_clipboard(table: dict, file: bool):
    """
    Copy a table json to clipboard.
    If file, it will copy the file, not just the str.
    """
    if file:
        path = Path(f"data/{table["metadata"]["name"]}.json").resolve()
        pyperclip.copy(str(path))
    else:
        pyperclip.copy(json.dumps(table, sort_keys=True, indent=4, ensure_ascii=False))