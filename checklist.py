checklist = list()

# CREATE
def create(item):
    checklist.append(item)

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
    index = 0
    for list_item in checklist:
        print(index + list_item)
        index += 1

# MARK COMPLETED ITEM WITH √
def mark_completed(index):
    checklist[index] = '√' + checklist[index]

# PROMPT USER INPUT
def user_input(prompt):
    user_input = input(prompt)
    return user_input

# VALIDATE INDEX INPUT EXIST
def val_index(index):
    if len(checklist) == 0:
        return True
    elif index >= len(checklist):
        return True
    else:
        return False

# FUNCTION SELECTION
def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item: ")
        create(input_item)
        return True

    # Read item
    elif function_code == "R":
        item_index = int(user_input("Index number? "))
        
        while val_index(item_index):
            print("Invalid index! Please try again.")
            item_index = int(user_input("Index number? "))

        print(read(item_index))
        return True

    elif function_code == "U":
        item_index = int(user_input("Index number? "))
        
        while val_index(item_index):
            print("Invalid index! Please try again.")
            item_index = int(user_input("Index number? "))
            
        updated_item = user_input("Input updated item: ")
        update(item_index, updated_item)
        return True
    
    elif function_code == "D":
        item_index = int(user_input("Index number? "))
        
        while val_index(item_index):
            print("Invalid index! Please try again.")
            item_index = int(user_input("Index number? "))
            
        destroy(item_index)
        return True     

    # Print all items
    elif function_code == "P":
        list_all_items()
        return True

    # Stop the loop
    elif function_code == "Q":
        return False

    # Catch all
    else:
        print("Unknown Option")



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
test()

running = True
while running:
    selection = user_input("""
Press C to Add to checklist
Press R to Read from checklist
Press U to Update item in checklist
Press D to Delete item in checklist
Press P to display checklist
Press Q to quit

---> """)
    running = select(selection)