def func_count(num, even=0, odd=0):
    if num == 0:
        return even, odd
    if (num % 10) % 2 == 0:
        even += 1
    else:
        odd += 1
    return func_count(num // 10, even, odd)


number = 123456788
even, odd = func_count(number)
print(f'In the number {number} - {even} even, {odd} odd')