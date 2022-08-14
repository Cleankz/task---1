def  exponentiation(inp_num,extent):# первое задание
    if extent == 0:
        return 1
    if extent == 1:
        return inp_num
    return inp_num * exponentiation(inp_num,extent-1)

def sum_values_of_num(inp_num):# второе задание
    if inp_num == 0:
        return inp_num
    return inp_num % 10 + sum_values_of_num(inp_num // 10)
