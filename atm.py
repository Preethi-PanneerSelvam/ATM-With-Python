balance = 10000  

while True:
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Balance")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        amount = int(input("Enter the amount to withdraw: "))
        balance -= amount
        print("Balance:", balance)
    elif choice == 2:
        amount = int(input("Enter the amount to deposit: "))
        balance += amount
        print("Balance:", balance)
    elif choice == 3:
        print("Balance:", balance)
    elif choice == 4:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
    
print("Thank you for using ATM!")
