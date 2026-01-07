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
    print("----- WELCOME TO MINI-DB -----")
    print("Author: Arnau Neches Vilà")

    while True:
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
    pass

def create_table_entry_cli(table_contents: dict):
    """
    CLI function to create a new entry on a table.
    """
    pass

def delete_table_entry_cli(table_contents: dict):
    """
    CLI function to delete a table's entry.
    """
    pass

def copy_clipboard_cli(table_contents: dict):
    """
    CLI function to copy to clipboard a table's contents.
    """

if __name__ == "__main__":
    index()
