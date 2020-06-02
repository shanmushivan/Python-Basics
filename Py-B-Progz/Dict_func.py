def main():
    print('\n########################################################\n')
 
    dict1 = {'India', 'Germany', 250, 4000, 'Australia', 5100}
    print(dict1)
 
    # len : This function gives the total length of the dictionary
    print("len : ", len(dict1))
 
    # str : This function prints dictionary as a String
    print("str : ", str(dict1))
 
    # copy : This function returns a shallow copy of dictionary dict
    dict2 = dict1.copy()
    print("copy : ", dict2)
 
    # clear: This method removes all elements of dictionary
    print("before clear : ", dict2)
    dict2.clear()
    print("after clear : ", dict2)
 
    # dict.fromkeys: This method creates a new dictionary with keys from
    # templist and values set to value.
    templist = ('India', 'Germany', 'Australia')
    dict3 = dict.fromkeys(templist, 100)
    print("formkeys : ", str(dict3))
 
    # dict.get(): This method returns the value for the specified key
    # if key is in dictionary.
    dict4 = {'John': 25, 'Mark': 45, 'Chinao': 29}
    print("dict.key: Mark ", dict4.get('Mark'))
 
    # items: This method returns a list of tuple pairs in sort order
    dict4 = {'John': 25, 'Mark': 45, 'Chinao': 29}
    print("items: ", dict4.items())
 
    # setdefault: This method returns the key value available in the dictionary
    # If given key is not available then it will return provided default value.
    print("setdefault: ", dict4.setdefault('Sam', 29))
    print("setdefault: ", dict4.setdefault('Rocky'))
    print("setdefault: ", dict4.setdefault('Musaad', None))
    print(dict4)
 
    # update: This method adds second dictionary key-values pairs into first.
    # This function does not return anything.
    dict5 = {'Henry': 16, 'Sophie': 27}
    dict4.update(dict5)
    print("update: ", dict4)
 
    # values: This method returns a list of all the values available
    # in a given dictionary.
    print("values: ", dict4.values())
 
    # pop: This method removes and returns an element from a dictionary
    # having the given key.
    dict4.pop('Rocky')
    dict4.pop('Musaad')
    dict4.pop('Sam')
    print("pop: ", dict4)
 
main()