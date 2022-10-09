text = input("Введите текст \n")
text = text.split()

for el in text:
    if len(el) > 10:
        print(text.index(el), el[0:10])
    else: print(text.index(el), el)
