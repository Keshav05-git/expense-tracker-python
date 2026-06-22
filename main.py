#Expense Tracker-

expense_list=[] #List carry all time expenses

print("----------------------------------")
print("WELCOME TO EXPENSE TRACKER💸")
print("----------------------------------")

print("==================MENU========================")

print("[1] Add Expense")
print("[2] View All Records")
print("[3] Your Total Spending Till Now")
print("[4] EXIT")
print("==============================================")


while True: #Infinite loop, ends with only "break" condition

    n=int(input("Choose what you want from [1-4]: ")) #Entring user's choice
    print("-----------------------------------------")
#Add Expense-    

    if(n==1):
        date=input("Enter Date please (DD/MM/YY): ")
        category=input("Tell the kind of Expenditure (Eg-Car, Clothes, Food, etc...): ")
        description=input("Description of your expense please: ")
        amount=float(input("Enter amount of your expenditure Rs: "))

        expense={
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }
        expense_list.append(expense)
        print("----------------------------------")
        print("This expenditure is stored✅")
        print("----------------------------------")

#View All Records

    elif(n==2):
        if(len(expense_list)==0):
            print("You have no expense till now")
        else:
            print("Your Expenses📝:\n")
            count=1
            for  items in expense_list:
                print(f"Expense No.{count} ➡️ \n{items} ")
                count+=1
                print("----------------------------------")

#Your Total Spending Till Now

    elif(n==3):
        total=0
        for item in expense_list:
            total=total+ item["amount"]
        print("Your Total Spending Till Now💰:", total)
        print("----------------------------------")

#EXIT"        

    elif (n==4):
        print("Your are Exited🔚\nThankyou To Use Our System😊")
        break

    else:
        print("Invalid Option Choosed❌")
        print("Choose again😊")


       
            


    



