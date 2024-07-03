def reverse_string(user_input:str)-> str:

    #converting string to a list
    string_list = list(user_input)

    #using string manipulation, we are then printing all the elements
    #in the list in reverse
    reversed_list=string_list[::-1]

    return ''.join(reversed_list)


#

stop=0
while (stop==0):
    user_input=str(input("Please Enter A String To Reverse: "))
    print("Reversed String: ",reverse_string(user_input))
