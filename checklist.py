import os # Clear terminal screen

checklist = list()

# CREATE
def create(item):
    checklist.append({"item": item, "checked": False})

# READ
def read(index):
    return checklist[index]

# UPDATE
def update(index, item):
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)

# LIST ALL ITEMS
def list_all_items():
    for index, item in enumerate(checklist):
        checked_status = "√" if item["checked"] else " "
        print(f"{index}: [{checked_status}] {item['item']}")

# MARK COMPLETED ITEM WITH √
def mark_completed(index):
    checklist[index] = '√' + checklist[index]

# UNCHECK ITEM
def uncheck(index):
    if not val_index(index):
        if checklist[index]["checked"]:
            checklist[index]["checked"] = False
            print(f"Unchecked: {checklist[index]['item']}")
        else:
            print("Item is already unchecked.")
    else:
        print("Invalid index! Please try again.")

# GET USER INPUT
def user_input(prompt):
    user_input = input(prompt)
    return user_input

# VALIDATE INDEX INPUT EXIST
def val_index(index):
    return index < 0 or index >= len(checklist)

# FUNCTION SELECTION
def select(function_code):
    # Convert the function code to lowercase
    function_code = function_code.lower()

    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Create item
    if function_code == "c":
        input_item = user_input("Input item: ")
        create(input_item)
        return True

    # Read item
    elif function_code == "r":
        item_index = int(user_input("Index number? "))
        try:
            if val_index(item_index):
                print("Invalid index! Please try again.")
            else:
                print(read(item_index))
        except ValueError:
            print("Invalid input. Please enter a valid index number.")
        return True

    # Update item
    elif function_code == "u":
        item_index = int(user_input("Index number? "))
        try:
            if val_index(item_index):
                print("Invalid index! Please try again.")
            else:
                updated_item = user_input("Input updated item: ")
                update(item_index, updated_item)
        except ValueError:
            print("Invalid input. Please enter a valid index number.")
        return True
    
    # Destroy item
    elif function_code == "d":
        item_index = int(user_input("Index number? "))
        try:
            if val_index(item_index):
                print("Invalid index! Please try again.")
            else:
                destroy(item_index)
        except ValueError:
            print("Invalid input. Please enter a valid index number.")
        return True
    
    # Uncheck item
    elif function_code == "X":
        item_index = int(user_input("Index number? "))
        try:
            uncheck(item_index)
        except ValueError:
            print("Invalid input. Please enter a valid index number.")
        return True

    # Print all items
    elif function_code == "p":
        list_all_items()
        return True

    # Stop the loop
    elif function_code == "q":
        return False

    # Catch all
    else:
        print("Unknown Option")
        return True  


# TEST
def test():
    create('purple sox')
    create('red cloak')

    print(read(0))
    print(read(1))

    update(0, 'purple socks')
    destroy(1)

    print(read(0))
    # print(read(1))

    list_all_items()

    # Call your new function with the appropriate value
    select("C")

    # View the results
    list_all_items()

    # Call function with new value
    select("R")

    # View results
    list_all_items()

# Run Tests
# test()

running = True
while running:
    selection = user_input("""
Press C to Add to checklist
Press R to Read from checklist
Press U to Update item in checklist
Press D to Delete item in checklist
Press P to Display checklist
Press X to Uncheck item
Press Q to Quit

➤ """)
    running = select(selection)