sek = int(input("Введите время в секундах \n"))
hours = sek // 3600
minutes = (sek - hours*3600) // 60
sekonds = sek - (3600*hours) - 60*minutes

print(f'{hours:02}:{minutes:02}:{sekonds:02}')