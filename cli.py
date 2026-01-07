# These will be wrapper functions for the command line behavior of the program
import database
import storage
import table
import utils

def index():
    """
    Initial app loop.
    """
    valid_actions = {"c", "e", "d"}
    print("\n")
    print("----- WELCOME TO MINI-DB -----")
    print("Author: Arnau Neches Vilà")

    while True:
        print("\n")
        utils.valid_actions_main()
        print("\n")

        while True:
            action = input("What do you want to do? (c, e, d): ")

            if action not in valid_actions:
                print("Invalid action, try again please.")
                utils.valid_actions_main()
            else:
                break
        
        if action == "c":
            create_table_cli()
        elif action == "d":
            delete_table_cli()
        elif action == "e":
            view_edit_tables_cli()



def create_table_cli():
    '''
    Create a table and stores it in data/ as a json file
    '''
    tables_names = database.tables_names()

    print(f"----- CREATE A TABLE -----")
    print("\n")

    while True:
        name = str(input("Table name? (Type b for going back): "))

        if name in tables_names:
            print(f"A table called {name} already exists in the database, try another name.")
            print("List of existing tables: ")
            print(tables_names)
        elif name == "b":
            print("Going back to main page.")
            return
        else:
            break
    
    print("\n")

    while True:
        user_input = input("Number of fields?: ")

        try:
            n_fields = int(user_input)

            if n_fields > 50:
                n_fields = 50
                print("Number of fields limit is 50, you will be asked only for a 50 fields.")

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

            else:
                break

        while True:
            field_type = input(f"{field_name} type? (Valid types are: {valid_types}): ")

            if field_type not in valid_types:
                print(f"Invalid type, valid types are: {valid_types}. Try again.")
            else:
                break
            
        schema[field_name] = field_type

    table = database.create_table(schema, name)
    storage.store_table(table)

    print("\n")
    print(f"The table {name} has been successfully created under the directory data/{name}.json ")

def delete_table_cli():
    """
    CLI instructions for deleting a table.
    """
    tables_names = database.tables_names()

    print("----- DELETE A TABLE -----")

    print("Your are now entering the delete table process.")
    if not utils.acknoledge_continue():
        return 
    
    print("Existing tables: ")
    for table_name in tables_names:
        print(table_name)
    
    table_name = input("Which table do you want to delete? (Type any invalid table if you want to leave the deleting process): ")
    if table_name not in tables_names:
        return
    
    print("This table's contents are: ")
    table_contents = storage.read_table(table_name)
    table.show_table_contents(table_contents)
    storage.delete_table(table_name)

def view_edit_tables_cli():
    """
    CLI function to orchestate the viewing and editing process.
    """
    tables_names = database.tables_names()

    print("----- VIEW/EDIT A TABLE -----") 
    print("You are now entering the view/edit process.")

    print("\n")

    print("Existing tables: ")
    for name in tables_names:
        print(name)

    while True:
        table_name = input("Enter a table's name: ")

        if table_name not in tables_names:
            print("This table doesn't exist. Try again.")
        else:
            break

    table_contents = storage.read_table(table_name)
    table.show_table_contents(table_contents)

    valid_actions = {"c", "e", "d", "cc", "b"}
    print("\n")
    utils.valid_actions_ve()
    while True:
        action = input("What do you want to do? (Valid actions are c, e, d, cc, b): ")

        if action not in valid_actions:
            print("Invalid action, try again please.")
            utils.valid_actions_ve()
        else:
            break
    
    if action == "b":
        return
    elif action == "c":
        create_table_entry_cli(table_contents)
    elif action == "e":
        edit_table_entry_cli(table_contents)
    elif action == "d":
        delete_table_entry_cli(table_contents)
    elif action == "cc":
        copy_clipboard_cli(table_contents)

def edit_table_entry_cli(table_contents: dict):
    """
    CLI function to edit a table's entry.
    """
    schema = table_contents["schema"]
    valid_ids = table_contents["data"].keys()

    while True:
        print("\n") 
        try:
            id = int(input("Which entry do you want to edit?: "))
        except ValueError:
            print("Please enter an integer. ")

        if str(id) not in set(valid_ids):
            print("Invalid id, try again please.")
            print("Valid ids are: ")
            print(valid_ids)
        else:
            break

    current_entry_value = table_contents["data"][str(id)]
    new_entry_data = {}

    for fn, t in schema.items():
        print("Click enter when editing any value if you want to keep it as it was.")
        while True:
            try:
                if t == "i":
                    print(f"Current value for {fn} is {current_entry_value[fn]}.")
                    new_value = input(f"Enter the value for {fn}, it must be an integer. : ")
                    if new_value == "":
                        new_value = current_entry_value[fn]
                    else:
                        new_value = int(new_value)
                    break
                elif t == "s":
                    print(f"Current value for {fn} is {current_entry_value[fn]}.")
                    new_value = input(f"Enter the value for {fn}, it must be a string: ")
                    if new_value == "":
                        new_value = current_entry_value[fn]
                    else:
                        new_value = str(new_value)
                    break
                elif t == "f":
                    print(f"Current value for {fn} is {current_entry_value[fn]}.")
                    new_value = input(f"Enter the value for {fn}, it must be a float: ")
                    if new_value == "":
                        new_value = current_entry_value[fn]
                    else:
                        new_value = float(new_value)
                    break
                elif t == "b":
                    print(f"Current value for {fn} is {current_entry_value[fn]}.")
                    new_value = input(f"Enter the value for {fn}, it must be a boolean: ")
                    if new_value == "":
                        new_value = current_entry_value[fn]
                    else:
                        new_value = bool(new_value)
                    break
                elif t == "l":
                    print(f"Current value for {fn} is {current_entry_value[fn]}.")
                    raw = input(f"Enter the value for {fn}, it must be a comma separated list: ")
                    if raw == "":
                        new_value = current_entry_value[fn]
                    else:
                        new_value = [item.strip() for item in raw.split(",")]
                    break
            except ValueError:
                print("\n")
                print("Incorrect type for the field. Try again please.")
        
        new_entry_data[fn] = new_value
    
    table_contents["data"][str(id)] = new_entry_data
    storage.store_table(table_contents)


def create_table_entry_cli(table_contents: dict):
    """
    CLI function to create a new entry on a table.
    """
    while True:
        try:
            new_entries = int(input("How many new entries do you want to create?: "))
            break
        except ValueError:
            print("Please enter an integer. ")

    schema = table_contents["schema"]
    for i in range(new_entries):
        print("\n")
        print(f"New entry number: {i}")
        new_entry_data = {}
        for fn, t in schema.items():

            while True:
                try:
                    if t == "i":
                        new_value = int(input(f"Enter the value for {fn}, it must be an integer: "))
                        break
                    elif t == "s":
                        new_value = str(input(f"Enter the value for {fn}, it must be a string: "))
                        break
                    elif t == "f":
                        new_value = float(input(f"Enter the value for {fn}, it must be a float: "))
                        break
                    elif t == "b":
                        new_value = bool(input(f"Enter the value for {fn}, it must be a boolean: "))
                        break
                    elif t == "l":
                        raw = input(f"Enter the value for {fn}, it must be a comma separated list: ")
                        new_value = [item.strip() for item in raw.split(",")]
                        break
                except ValueError:
                    print("\n")
                    print("Incorrect type for the field. Try again please.")
            
            new_entry_data[fn] = new_value
        current_id = table_contents["meta"]["last_id"]
        table_contents["data"][str(current_id)] = new_entry_data
        table_contents["meta"]["last_id"] = current_id + 1
    
    storage.store_table(table_contents)
    print("Entries created successfully. ")

def delete_table_entry_cli(table_contents: dict):
    """
    CLI function to delete a table's entry.
    """
    valid_ids = table_contents["data"].keys()
    while True:
        print("\n") 
        try:
            id = int(input("Which entry do you want to delete?: "))
        except ValueError:
            print("Please enter an integer. ")

        if str(id) not in set(valid_ids):
            print("Invalid id, try again please.")
            print("Valid ids are: ")
            print(valid_ids)
        else:
            break
    table.delete_entry(table_contents, id)
    storage.store_table(table_contents)
    print(f"Entry with id {id} successfully deleted. ")

def copy_clipboard_cli(table_contents: dict):
    """
    CLI function to copy to clipboard a table's contents.
    """
    print("\n")
    table.copy_to_clipboard(table_contents)
    print("Contents copied. ")

if __name__ == "__main__":
    index()
