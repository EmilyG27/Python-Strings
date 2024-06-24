    
while True:
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")

    if len(first) > 2 and len(last) > 2:
        print(first, last)
    else:
        print("Enter more than 2 letters for your first AND last name.")

