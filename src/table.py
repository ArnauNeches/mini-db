# Table operations, edit, insert or delete. Functions take dictionaries as arguments, never read directly.
import pyperclip
import json
from datetime import date

def show_table_contents(table: dict) -> None:   
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

def delete_entry(table: dict, id: int) -> None:
    """
    Delete entry from table, return the table without the entry.
    """
    table["data"].pop(str(id))

def edit_entry(table_content: dict, new_data: dict, id: int) -> None:
    """
    Edits a table entry.
    """
    table_content["data"][str(id)] = new_data
    table_content["meta"]["last_modified"] = str(date.today())

def add_entry(table_content: dict, new_data: dict) -> None:
    """
    Create a new entry.
    """
    entry_id = table_content["meta"]["id_counter"]

    table_content["data"][str(entry_id)] = new_data
    table_content["meta"]["last_modified"] = str(date.today())
    table_content["meta"]["id_counter"] = entry_id + 1

def copy_to_clipboard(table: dict):
    """
    Copy a table's json to clipboard.
    """
    pyperclip.copy(json.dumps(table, sort_keys=True, indent=4, ensure_ascii=True))