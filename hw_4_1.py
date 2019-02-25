def input_text():
    print('Введите текст (пустая строка - прекратить ввод):')
    my_list = list()
    while True:
        text = input()
        if text == '':
            return my_list
        else:
            my_list.append(text)


def text_stat(text):
    my_dict = {}
    my_dict['input'] = text
    my_dict['lines'] = len(text)
    # общее количество цифр
    my_dict['digits'] = 0
    # словарь слов
    my_dict['words_stat'] = {}
    # словарь символов
    my_dict['chars_stat'] = {}
    for i in text:
        for y in list(i):
            if y.isdigit():
                my_dict['digits'] += 1
            my_dict['chars_stat'].setdefault(y, 0)
            my_dict['chars_stat'][y] += 1
        tmp_list = i.split()
        for y in tmp_list:
            my_dict['words_stat'].setdefault(y.lower(), 0)
            my_dict['words_stat'][y.lower()] += 1
    return my_dict

def show_stat(dict):
    print('Был использован следующий текст:')
    print('<--- Текст ---')
    for i in dict['input']:
        print(i)
    print('--- Текст --->', end='\n\n')
    print('Всего строк =', dict['lines'], end='\n\n')
    print('Всего цифр =', dict['digits'], end='\n\n')
    print('<--- Статистика символов ---')
    tab = "\t"
    for i in dict['chars_stat']:
        print(('\'{}\' = {}').format(i, dict['chars_stat'][i])) if i != tab else print(('{} = {}').format(repr(tab), dict['chars_stat'][i]))
    print('--- Статистика символов --->', end='\n\n')
    print('<--- Статистика слов ---')
    for i in dict['words_stat']:
        print(('\'{}\' = {}').format(i, dict['words_stat'][i]))
    print('--- Статистика слов --->')


show_stat(text_stat(input_text()))
