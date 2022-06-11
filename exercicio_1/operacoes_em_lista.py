def find_similar_in_list(list, value_to_search):
    # Acha quantas vezes o valor aparece na lista
    values_found = 0
    for item in list:
        if item == value_to_search:
            values_found += 1 # Esse operador adiciona o valor seguinte a variável
            # Exemplo: se var é 0, var += 1 vai resultar em 1
            # se var é 0, var -= 1 vai resultar em -1
            # o mesmo pode ser feito para strings
    
    print("{value} appears {found} times in list".format(value=value_to_search, found=values_found))

def remove_one_ocurrence_from_list(list, value_to_remove):
    list.remove(value_to_remove) # Remove retira um valor igual ao passado da lista, caso exista
    print("List without value {value} : {list}".format(value=value_to_remove, list=list))

def concatenate_all_values(list):
    complete_string = ""
    for item in list:
        complete_string += item
    
    print(complete_string)

def sort_list(list):
    print(list.sort())

list_of_strings = ["oi", "boi", "sol", "oi"]
value_to_use = "oi"

find_similar_in_list(list_of_strings, value_to_use)
remove_one_ocurrence_from_list(list_of_strings, value_to_use)
concatenate_all_values(list_of_strings)
sort_list(list_of_strings)