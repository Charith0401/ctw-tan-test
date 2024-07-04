def square_evens(numbers:list)->list:

    square_array=[]

    for i in range(0,len(numbers)):
        if (numbers[i]%2==0):
            square_array.append(numbers[i]**2)
            
    return square_array

stop=0

#this variable will keep track of when the user has finished 
#entering the elements in the array
ready=False

numbers=[]
while (stop==0):
    print("Please enter -1 to view squares of the values provided")
    while (ready==False): 
        number_to_append=int(input("Please enter a number to add to the array: "))
        if (number_to_append==-1):
            ready=True
            break
        else:
            numbers.append(number_to_append)
        
    print("Even Squares: ",square_evens(numbers))
    ready=False
    numbers=[]