#Task_5_2
try:
    with open('textfile_52.txt', 'r') as f_text:
        text = f_text.readlines()
    print(f'В текстовом файле - {len(text)} строк')
    word = 0
    num_line = 1
    for line in text:
        word = len(line.split())
        print(f'В строке {num_line} - {word} слов(а)')
        num_line += 1
except FileNotFoundError:
    print('Файл не найден')