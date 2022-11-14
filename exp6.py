dictionary = {}
while True:
    print("1. Create a key-value pair")
    print("2. Update/concatenate and delete the existing item ")
    print("3. Find a key and print its value")
    print("4. Map 2 list in dictionary")
    print("5. Exit")
    choice = int(input("Enter a choice: "))
    if choice == 1:
        key = input("Enter a key: ")
        value = input("Enter a value: ")
        dictionary.update({key: value})
        print(dictionary)
    elif choice == 2:
        print("1. Update")
        print("2. Concatenate")
        print("3. Delete")
        option = int(input("Choose an option: "))
        key = input("Enter the key: ")
        existing_value = dictionary.get(key, "Not_Found")
        if existing_value == "Not_Found":
            print("Key Not Found")
            continue

        if option == 1:
            updated_value = input("Enter new value: ")
            dictionary.update({key: updated_value})
        elif option == 2:
            updated_value = input("Concatenate the value: ")
            updated_value = existing_value + updated_value
            dictionary.update({key: updated_value})
        elif option == 3:
            del dictionary[key]
            print("Deleted")

    elif choice == 3:
        key = input("Enter the key: ")
        existing_value = dictionary.get(key, "Not_Found")
        if existing_value == "Not_Found":
            print("Key Not Found")
            continue
        print({key: existing_value})

    elif choice == 4:
        key_list = list(input("Enter list of keys: ").strip().split())
        value_list = list(input("Enter list of values: ").strip().split())
        pairs = dict(zip(key_list, value_list))
        dictionary.update(pairs)

    elif choice == 5:
        break
