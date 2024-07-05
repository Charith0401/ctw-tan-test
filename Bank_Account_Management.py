def get_balance(account_number : str) -> float:
    
    #data stored in accounts text file in account_number,balance format

    #opening the respective file in append mode
    file = open("accounts.txt","r")

    #reading entire document in the form of a list full of strings
    #in each line of the document.
    document = file.readlines()

    #this will flag True if the parameter account_number passed 
    #actually exists in the accounts.txt file
    found_account = False

    for i in range (0,len(document)):
        split_attr = document[i].split(",")
        if (split_attr[0] == account_number):
            account_balance = split_attr[1]
            found_account = True
            break

    file.close()

    if (found_account):
        return account_balance
    else:
        return "Account does not exist"

def deposit(account_number : str, amount : float) -> str|int:
    
    #opening the respective file in read mode first to get all the 
    #accounts.
    file = open("accounts.txt","r")

    #reading entire document in the form of a list full of strings
    #in each line of the document.
    document = file.readlines()

    #as good practice, to mark that the operation is done, the file
    #is then closed
    file.close()

    #this will flag True if the parameter account_number passed 
    #actually exists in the accounts.txt file
    found_account = False

    #this will store the index (line number) that the account number
    #was found on in the accounts.txt file
    account_index = -1

    #this for loop goes through every line of the accounts.txt 
    #document and will split/parse the attributes from "account number,amount" to
    #[account_number,amount] to be dealt with and compared afterwards.
    #split_attr[0] would be the account number and split_attr[1] would be the balance
    #of that account
    for i in range (0,len(document)):
        split_attr = document[i].split(",")
        if (split_attr[0] == account_number):
            account_balance = split_attr[1]
            account_index = i
            found_account = True
            break
    
    #if the account is found the amount is parsed into its integer form
    #and the new amount is deposited and the user's account balance
    #is then updated in the file
    if (found_account):
    
        updated_balance = float(account_balance) + amount
        updated_account = [str(account_number), str(updated_balance), "\n"]

        document[account_index] = ",".join(updated_account)

        file = open("accounts.txt", "w")
        file.writelines(document)

        print("Deposited", amount, "to account number", account_number)

        return updated_balance
    else:
        return "Account does not exist"

def withdraw(account_number : str, amount : float)-> str|int:

    #opening the respective file in read mode first to get all the 
    #accounts.
    file = open("accounts.txt","r")

    #reading entire document in the form of a list full of strings
    #in each line of the document.
    document = file.readlines()

    #as good practice, to mark that the operation is done, the file
    #is then closed
    file.close()

    #this will flag True if the parameter account_number passed 
    #actually exists in the accounts.txt file
    found_account=False

    #this will store the index (line number) that the account number
    #was found on in the accounts.txt file
    account_index=-1

    #this for loop goes through every line of the accounts.txt 
    #document and will split/parse the attributes from "account number,amount" to
    #[account_number,amount] to be dealt with and compared afterwards.
    #split_attr[0] would be the account number and split_attr[1] would be the balance
    #of that account
    for i in range (0,len(document)):
        split_attr = document[i].split(",")
        if (split_attr[0] == account_number):
            account_balance = split_attr[1]
            account_index = i
            found_account = True
            break
    
    #if the account is found the amount is parsed into its integer form
    #and the amount is withdrawn and the user's account balance
    #is then updated in the file IF the user has sufficient funds for the withdrawal.
    if (found_account):
    
        updated_balance = float(account_balance) - amount

        if (updated_balance>=0):

            updated_account = [str(account_number), str(updated_balance), "\n"]

            document[account_index] = ",".join(updated_account)

            file = open("accounts.txt", "w")
            file.writelines(document)

            print("Withdrew", amount, "from account number", account_number,"\n")

            return updated_balance
        else:
            return "Insufficient account funds"
    else:
        return "Account does not exist"

def update_account(account_number: str, balance: float) -> str|int:
    #opening the respective file in read mode first to get all the 
    #accounts.
    file = open("accounts.txt","r")

    #reading entire document in the form of a list full of strings
    #in each line of the document.
    document = file.readlines()

    #as good practice, to mark that the operation is done, the file
    #is then closed
    file.close()

    #this will flag True if the parameter account_number passed 
    #actually exists in the accounts.txt file
    found_account=False

    #this will store the index (line number) that the account number
    #was found on in the accounts.txt file
    account_index=-1

    #this for loop goes through every line of the accounts.txt 
    #document and will split/parse the attributes from "account number,amount" to
    #[account_number,amount] to be dealt with and compared afterwards.
    #split_attr[0] would be the account number and split_attr[1] would be the balance
    #of that account
    for i in range (0,len(document)):
        split_attr = document[i].split(",")
        if (split_attr[0] == account_number):
            account_balance = split_attr[1]
            account_index = i
            found_account = True
            break
    
    #if the account is found the amount is parsed into its integer form
    #and the amount is withdrawn and the user's account balance
    #is then updated in the file IF the user has sufficient funds for the withdrawal.
    if (found_account):

        if (balance>=0):

            updated_account = [str(account_number), str(balance), "\n"]

            document[account_index] = ",".join(updated_account)

            file = open("accounts.txt", "w")
            file.writelines(document)

            print("Account number", account_number, "now has a balance of", balance, "\n")

            return balance
        else:
            return "Please enter a positive integer value"
    else:
        return "Account does not exist"
    

#this loop was created for debugging and presentation purposes (allowing users to select options
#easily and values need to be entered appropriately in digit form and the result will be output
stop = 0
while (stop == 0):
    try:
        option = int(input("Options Available:\n1.Get Balance\n2.Deposit\n3.Withdraw\n4.Update Account\nEnter an option number: "))
        account_number = str(input("Please enter your account number: "))

        if (option == 1):
            print("Balance: ",get_balance(account_number),"\n")

        elif (option == 2):
            amount = float(input("Please enter the amount to deposit: "))
            print("Updated balance after deposit: ", deposit(account_number,amount),"\n")

        elif (option == 3):
            amount = float(input("Please enter the amount to withdraw: "))
            print("Updated balance after deposit: ",withdraw(account_number,amount),"\n")

        elif (option == 4):
            new_balance = float(input("Please enter the new balance: "))
            print("New balance: ",update_account(account_number,new_balance),"\n")
    except:
        print("ERROR: INVALID SYNTAX\n")