# Table operations, edit, insert or delete
import storage
import pyperclip

def show_table_contents(table: dict | None, table_name: str | None):   
    """
    Show data and metadata of a table.
    """
    if not table:
        table = storage.read_table(table_name)

    if not table:
        print("This table doesn't exist.")
    else:
        print(f"Table {table_name} metadata: ")
        print(table["meta"])
        print(f"Table {table_name} data: ")
        print(table["data"])

def table_contents(table: dict | None, table_name: str | None):
    """
    Returns the schema, metadata and data of a table as separate dictionaries.
    """
    if not table:
        table = storage.read_table(table_name)
    return table["schema"], table["meta"], table["data"]

def copy_to_clipboard(table: dict | None, table_name: str | None):
    """
    Copy a table json to clipboard.
    """
    #TODO