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

def list_of_ocurrences(list, value_to_find):
    # Retorna todos valores iguais a value_to_find
    list_of_desired_values = []
    for value in list:
        if value == value_to_find:
            list_of_desired_values.append(value) # Adiciona item na lista

    print(list_of_desired_values)


def concatenate_all_values(list):
    complete_string = ""
    for item in list:
        complete_string += item
    
    print(complete_string)

def sort_list(list):
    sorted_list = sorted(list)
    print(sorted_list)

def invert_list(list):
    inverted_list = list[::-1] # Isso representa como se fosse um for dentro da lista invertendo ela
    print(inverted_list)

list_of_strings = ["oi", "boi", "sol", "oi"]
value_to_use = "oi"

find_similar_in_list(list_of_strings, value_to_use)
list_of_ocurrences(list_of_strings, value_to_use)
concatenate_all_values(list_of_strings)
sort_list(list_of_strings)
invert_list(list_of_strings)