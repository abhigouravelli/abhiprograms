print("Welcome to this List Game")
print("Make List B be the same as List A")
alist = [4,5,6,8,798,15]
blist = [4,5,6,8,798,15,20]
print("A list: ", alist)
print("B list: ", blist)

def show_menu():
    print("1: Append")
    print('2: Remove')
    print("3: Insert")
    print("4: Print")
    print("6. DONE: Check resluts")

while True:
    show_menu()
    choice = input("Select an option: ")
    if choice == "1":
        value = int(input("Append what value: "))
        blist.append(value)
    elif choice == "2":
        value = int(input("Remove what valie: "))
        blist.remove(value)
    elif choice == "3":
        index = int(input("Insert what index: "))
        value = int(input("Insert what value: "))
        blist.insert(index,value)
    elif choice == "4":
        value = int(input("Pop what index: "))
        blist.pop(index)
    elif choice == "5":
        print(blist)
    elif choice == "6":
        if alist == blist:
            print("All mathed! You win!")
        else:
            print("No match, you lose")
            break
    else:
            print("Input not valid, please try again")

