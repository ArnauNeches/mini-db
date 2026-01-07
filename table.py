# Table operations, edit, insert or delete. Functions take dictionaries as arguments, never read directly.
import pyperclip
import json
from pathlib import Path

def show_table_contents(table: dict):   
    """
    Show data and metadata of a table.
    """
    table_name = table["meta"]["name"]
    print("\n")

    print(f"Table {table_name} metadata: ")
    meta = json.dumps(table["meta"], indent=4, sort_keys=True, ensure_ascii=True)
    print(meta)

    print(f"Table {table_name} schema: ")
    schema = json.dumps(table["schema"], indent=4, sort_keys=True, ensure_ascii=True)
    print(schema)

    print(f"Table {table_name} data: ")
    data = json.dumps(table["data"], indent=4, sort_keys=True, ensure_ascii=True)
    print(data)


def split_contents(table: dict):
    """
    Returns the schema, metadata and data of a table as separate dictionaries.
    """
    return table["schema"], table["meta"], table["data"]

def delete_entry(table: dict, id: int):
    """
    Delete entry from table, return the table without the entry.
    """
    table["data"].pop(str(id))

def copy_to_clipboard(table: dict):
    """
    Copy a table's json to clipboard.
    """
    pyperclip.copy(json.dumps(table, sort_keys=True, indent=4, ensure_ascii=True))