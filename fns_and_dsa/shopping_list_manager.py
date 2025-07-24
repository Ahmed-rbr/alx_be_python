
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():

    shopping_list = []
    display_menu()
    choice = input("Enter your choice: ")
    while True:
        match choice:
            case 1:
                item = input('enter item name to add: ')
                shopping_list.append(item)
                print(f"{item} was added\n")
            case 2:
                item = input('enter item name to remove: ')
                if item not in shopping_list:
                    print('no  item whit this name was found \n')

                else:
                    shopping_list.remove(item)
                    print(f"{item} was removed\n")
            case 3:
                print("Shopping list:")
                for item in shopping_list:
                    print(f"{item}\n")

            case 4:
                print('good bay')
                break
            case _:
                print("Invalid choice. Please try again.")


main()
