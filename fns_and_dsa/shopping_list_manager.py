

def main():
    user_choice = 5

    shopping_list = []
    print("Shopping List Manager")

    while user_choice != 4:
        try:
            user_choice = int(
                input("1. Add Item\n2. Remove Item\n3. View List\n4. Exit\nChoose an option: "))
        except ValueError:
            print("Please enter a valid number (1-4).\n")
            continue
        match user_choice:
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
                print("Invalid choice")


main()
