def sort_dict_by_values(d:dict)-> dict:

    #taking parameter d and stripping it to just the values of the keys.
    x = d.values()

    #converting the dictionary to a list to apply operations.
    value_list = list(x)

    #the list is then sorted via a built-in function in ascending order.
    sorted_value_list = sorted(value_list)

    dict = d.items()

    sorted_dict = {k:v for k,v in sorted(dict.items(), key=lambda item: item[1])}

    print("sorted dict",sorted_dict)

print("Sorted dict values: ",sort_dict_by_values({"a":2,"b":1,"c":3}))    