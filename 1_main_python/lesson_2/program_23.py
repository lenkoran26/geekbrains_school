#========================================METHOD DICT===================================
calend = {
    'Зима':['12','1','2'],
    'Весна':['3','4','5'],
    'Лето':['6','7','8'],
    'Осень':['9','10','11']
}
while True:
    mnt = input('Введите номер месяца - ')
    if (int(mnt) < 1) | (int(mnt) > 12):
        print("Введите число 1-12")
    else: break

for key, value in calend.items():
    if mnt in value:
        print(key)
#========================================METHOD LIST===================================
winter = ['12','1','2']
spring = ['3','4','5']
summer = ['6','7','8']
autumn = ['9','10','11']

print("=========METHOD LIST===========")

while True:
    mnt = input('Введите номер месяца - ')
    if (int(mnt) < 1) | (int(mnt) > 12):
        print("Введите число 1-12")
    else: break

if mnt in winter:
    print ('Зима')
elif mnt in spring:
    print ('Весна')
elif mnt in summer:
    print ('Лето')
elif mnt in autumn:
    print ('Осень')


