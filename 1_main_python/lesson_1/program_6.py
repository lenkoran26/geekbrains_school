dist = float(input("Введите начальную дистанцию - "))
rezult = float(input("Введите желаемый результат дистанции - "))
day = 1
while dist < rezult:
    dist += dist*0.1
    day += 1
    print(f'День - {day}, дистанция - {"%.2f" % dist}')
print(f'На {day}-й день спортсмен достиг результата не менее {rezult} км')