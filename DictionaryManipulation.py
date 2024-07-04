def sort_dict_by_values(d:dict)-> dict:

    #this stores the items in the dictionary as tuples
    dict = d.items()

    #line 11 will essentially map the variable "k" to a key in the tuple
    #and "v" to the corresponding value of this key and is surrounded by a "sorted"
    #function.

    #additionally, a key is provided to this "sorted" function that will sort the 
    #tuples based on the second value which is the value of the key.

    sorted_dict = {k:v for k,v in sorted(dict, key=lambda item: item[1])}

    return sorted_dict

print("Sorted dict values: ",sort_dict_by_values({"a":2,"b":1,"c":3}))    