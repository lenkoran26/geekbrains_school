def translate(numb):
    en_numbers = ['One', 'Two', 'Three', 'Four']
    ru_numbers = ['Один', 'Два', 'Три', 'Четыре']
    index_en_word = en_numbers.index(numb)
    new_word = ru_numbers[index_en_word]
    return new_word
try:
    with open('textfile_54.txt', 'r') as en_numb:
        with open('textfile_54_2.txt','a') as ru_numb:
            text = en_numb.readlines()
            for line in text:
                word = line.split()
                new_word = translate(word[0]) + ' ' + word[1] + ' ' + word[2]
                ru_numb.writelines(new_word + '\n')
except FileNotFoundError:
    print('Файл не найден')