def get_balance(account_number:str)-> float:

    file = open("accounts.txt","r")
    document = file.readlines()
    
    for i in range (0,len(document)):
        split_attr = document[i].split(",")
        if (split_attr[0] == account_number):
            account_balance = split_attr[1]
            found_account = True
            break
    
    if (found_account):
        return account_balance
    else:
        return "Account does not exist"
    
get_balance("123456")