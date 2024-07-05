def get_balance(account_number:str)-> float:
    
    #data stored in accounts text file in account_number,balance format

    #opening the respective file in append mode
    file = open("accounts.txt","r")

    #reading entire document in the form of a list full of strings
    #in each line of the document.
    document = file.readlines()

    #this will flag True if the parameter account_number passed 
    #actually exists in the accounts.txt file
    found_account=False

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

def deposit(account_number:str,amount:float):
    
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
            account_index=i
            found_account = True
            break
    
    #if the account is found the amount is parsed into its integer form
    #and the new amount is deposited and the user's account balance
    #is then updated in the file
    if (found_account):
        print("Deposited",amount,"to account number",account_number)
        updated_balance=int(account_balance)+amount
        temp=[str(account_number),str(updated_balance),"\n"]
        document[account_index]=",".join(temp)
        print("final",document)
        file=open("accounts.txt","w")
        file.writelines(document)

        # file.writelines()
        return updated_balance
    else:
        return "Account does not exist"

def withdraw(account_number:str, amount:float)
print("Updated Balance:",deposit("234567",1500))