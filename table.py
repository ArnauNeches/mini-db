# Table operations, edit, insert or delete
import storage

def show_table_contents(table_name: str):   
    table = storage.read_table(table_name)

    if not table:
        print("This table doesn't exist.")
    else:
        print(f"Table {table_name} metadata: ")
        print(table["meta"])
        print(f"Table {table_name} data: ")
        print(table["data"])