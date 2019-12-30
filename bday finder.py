dict={}
while True:
    print("________AAJ TO BHAI KA BDAY HAI_________")
    print("1.Show Birthday")
    print("2.Add to Birthday List")
    print("3.Exit")
    choice=int(input("Enter the choice: "))


    if choice==1:
        if len(dict.keys())==0:
            print("Nothing to show")
        else:
            name=input("Enter name who's bday u are looking for: ")
            birthday=dict.get(name,"No data found")
            print(birthday)


    elif choice==2:
        name=input("Enter friend's name: ")
        birthdate=input("Enter Birthdate: ")
        dict[name]=birthdate
        print("Birthday added")


    elif choice==3:
        break


    else:
        print("Choose a Valid Option")
        
        
        
