def revers_num(num, rev_num = ''):
    if num == 0:
        return rev_num
    else:
        rev_num += str(num % 10)
    return revers_num(num//10, rev_num)

num = 1230
print(revers_num(num))