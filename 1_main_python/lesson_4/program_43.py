#Task_4_3

def my_func(l_b, h_b):
    list_numb = (num for num in range(l_b, h_b) if (num % 20 == 0) | (num % 21 == 0))
    for i in list_numb:
        yield i

lower_border = 20
high_border = 240
for i in my_func(lower_border,high_border):
    print(i,end=' ')