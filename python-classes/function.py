#!/usr/bin/python3

def replace_in_list(my_list, idx, new_element):
    for i in range(len(my_list)):
        if ( i == idx ):
                my_list[idx] = new_element
                
    return my_list

def max_integer(my_list=[]):
    max = 0
    for i in range(len(my_list)):
        if my_list[idx] > max:
            max = my_list[idx]
    return max

def multiply_by_2(a_dictionnary):
    new_dict={}
    for key, value in a_dictionnary.items():
        new_dict[key] = value * 2
    return new_dict

dict_1 = {‘id’: 12, ‘first_name’: “John”}
dict_2 = {‘last_name’: “Bob”, ‘age’: 34}
def merge(dict_1, dict_2):
    return {**dict_1, **dict_2}
#print(merge(dict_1, dict_2))

def uniq_add(my_list):
    b=set(my_list)
    somme=0
    for x in b:
            somme = somme + x
    return somme
