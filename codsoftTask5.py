contacts=[]

while True:
    print("1. Add contact")
    print("2. View contact")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")
    choice=int(input("Enter choice (1-6): "))
    if choice==1:
        name=input("Enter name: ")
        phone=input("Enter phone no.: ")
        email=input("Enter email: ")
        address=input("Enter address: ")
        contact={'Name':name,'Phone':phone,'Email':email,'Address':address}
        contacts.append(contact)
    elif choice==2:
        if len(contacts)==0:
            print("No contacts yet!")
        else:
            print("Contact Book: ")
            for i,contact in enumerate(contacts):
                print(i,"-",contact)
    elif choice==3:
        search=input("Enter name or phone to search: ")
        for c in contacts:
            if search in c['Name'] or search in c['Phone']:
                print(c)
    elif choice==4:
        try:
            index=int(input("Enter index: "))
            name=input("Enter name: ")
            phone=input("Enter phone no.: ")
            email=input("Enter email: ")
            address=input("Enter address: ")
            contact={'Name':name,'Phone':phone,'Email':email,'Address':address}
            contacts[index]=contact
        except (IndexError,ValueError):
            print("Invalid index, Please check contact book for index!")
    elif choice==5:
        try:
            index=int(input("Enter index: "))
            del contacts[index]
        except (IndexError,ValueError):
            print("Invalid index, Please check contact book for index!")
    elif choice==6:
        break
    else:
        print("Invalid choice, Please check!")