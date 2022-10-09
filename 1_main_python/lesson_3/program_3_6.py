def int_func(line):
    list_word = line.split()
    new_list = list()

    for word in list_word:
        if ord(word[0]) > 90:                       #если буква прописная
            first_simv = chr(ord(word[0])-32)       #получаем такой же строчной символ
            new_word = first_simv + word[1:]        #новое слово = строчная буква + часть слова со 2 буквы
            new_list.append(new_word)               #добавляем слово в новый список
        else:                                       #если буква строчная
            new_list.append(word)

    return new_list

line_str = input("Введите строку \n")
print(int_func(line_str))