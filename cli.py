# These will be wrapper functions for the command line behavior of the program
import database
import storage
import table
import utils
from pathlib import Path
from datetime import date

def index():
    """
    Initial app loop.
    """
    valid_actions = {"c", "e", "d"}
    print("----- WELCOME TO MINI-DB -----")
    print("Author: Arnau Neches Vilà")

    while True:
        utils.valid_actions()
        print("\n")

        while True:
            action = input("What do you want to do? (c, e, d): ")

            if action not in valid_actions:
                print("Invalid action, try again please.")
                utils.valid_actions()
            else:
                break
        
        if action == "c":
            create_table_cli()
        elif action == "d":
            delete_table_cli()
        elif action == "e":
            #TODO
            pass



def create_table_cli():
    '''
    Create a table and stores it in data/ as a json file
    '''
    data_dir = Path("data")
    tables = {f.stem for f in data_dir.glob("*.json")}

    print(f"----- CREATE A TABLE -----")
    print("\n")

    while True:
        name = str(input("Table name?: "))

        if name == "Back":
            print("Invalid name for a table, try another one (Note that Back is reserved).")
        elif name in tables:
            print(f"A table called {name} already exists in the database, try another name.")
        else:
            break
    
    print("\n")

    while True:
        user_input = input("Number of fields?: ")

        try:
            n_fields = int(user_input)

            if n_fields > 100:
                n_fields = 100
                print("Number of fields limit is 100, you will be asked only for a 100 fields.")

            break

        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    print("\n")

    print("Valid types for entries are: string (s), integer (i), float (f), boolean (b) and list (l)")
    schema = {}
    field_names = set()
    valid_types = {"s", "i", "f", "b", "l"}
    for i in range(n_fields):
        while True:
            field_name = input(f"Name of {i+1}-field?: ")

            if field_name in field_names:
                print("There already exist a field with that name, try again.")
                print("Created fields: ")
                print(field_names)

            elif field_name == "Back":
                print("Invalid field name, try another one (Note that Back is reserved).")

            else:
                break

        while True:
            field_type = input(f"{field_name} type? (Valid types are: {valid_types}): ")

            if field_type not in valid_types:
                print(f"Invalid type, valid types are: {valid_types}. Try again.")
            else:
                break
        
        if field_type == "l":
            while True:
                list_type = input("List type, what type are the list elements?: ")
            
                if list_type not in valid_types:
                    print(f"Invalid type, valid types are: {valid_types}. Try again.")
                else:
                    break
            
            schema[field_name] = {"type": field_type, "items": list_type}
        else:
            schema[field_name] = {"type": field_type}

    table = database.create_table(schema, name)
    storage.store_table(table)

def delete_table_cli():
    """
    CLI instructions for deleting a table.
    """
    data_dir = Path("data")
    table_names = {f.stem for f in data_dir.glob("*.json")}

    print("----- DELETE A TABLE -----")

    print("Your are now entering the delete table process.")
    if not utils.acknoledge_continue():
        return 
    
    print("Existing tables: ")
    for table_name in table_names:
        print(table_name)
    
    table_name = input("Which table do you want to delete? (Type any invalid table if you want to leave the deleting process): ")
    if table_name not in table_names:
        return
    
    print("This table's contents are: ")
    table.show_table_contents(table_name=table_name)
    
    storage.delete_table(table_name)

def view_edit_tables_cli():
    pass

def edit_table_entry_cli(table_name: str, entry_id: int):
    """
    CLI function to edit a table entry.
    """
    pass

def create_table_entry_cli(table_name: str):
    """
    Create a new entry on a table.
    """
    pass

if __name__ == "__main__":
    create_table_cli()
