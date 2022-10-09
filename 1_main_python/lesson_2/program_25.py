my_list = [7,5,3,3,2]
j=0
print(my_list)

while True:
    n = int(input("Введите число 1-9 \n"))
    if not((n<1) | (n>9)):
       break

for i in my_list:
    if n < i:
        j+=1

my_list.insert(j,n)
print(my_list)
