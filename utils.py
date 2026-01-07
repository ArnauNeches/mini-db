# Some utilities used across all functions

def acknoledge_continue():
    cont = input("Are you sure you want to continue? (y/n): ")
    if cont == "n":
        print("Going back to index.")
        return False
    else:
        return True
    
def valid_actions_main():
    print("Actions you can do: ")
    print("Create a table (c)")
    print("Edit/View a table (e)")
    print("Delete a table (d)")

def valid_actions_ve():
    print("Actions you can do: ")
    print("Create an entry (c)")
    print("Edit an entry (e)")
    print("Delete an entry (d)")
    print("Copy table to clipboard (cc)")
    print("Go back to main page (b)")

def valid_actions_cc():
    print("Actions you can do: ")
    print("Copy table contents as a str (s)")
    print("Copy json file itself (f)")
