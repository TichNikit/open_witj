my_name = 'open_t.txt'

with open(my_name, mode = 'r', encoding= 'UTF-8') as file:
    for line in file:
        print(line, end = '')


