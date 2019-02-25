def input_text():
    print('Введите текст (пустая строка - прекратить ввод):')
    my_list = list()
    while True:
        text = input()
        if text == '':
            return my_list
        else:
            my_list.append(text)


def text_stat(text, *args):
    my_dict = {}
    my_dict['input'] = text
    my_dict['lines'] = len(text)
    # общее количество цифр
    my_dict['digits'] = 0
    # словарь слов
    my_dict['words_stat'] = {}
    # словарь символов
    my_dict['chars_stat'] = {}

# формирования списка для валидации
    validate = []
    for n in args:
        if type(n) == str:
            validate.append(n)
        elif type(n) == list:
            validate.extend(n)
        elif type(n) == dict:
            for i in n.values():
                validate.append(i)
        else:
            for i in n:
                validate.append(i)

    validated_text = []
    for i in text:
        for x in validate:
            if x.lower() in i.lower():
                i = i.lower()
                i = i.replace(x.lower(), '')
        validated_text.append(i)

    for i in validated_text:
        for y in list(i):
            if y.isdigit():
                my_dict['digits'] += 1
            my_dict['chars_stat'].setdefault(y.lower(), 0)
            my_dict['chars_stat'][y.lower()] += 1
        tmp_list = i.split()
        for y in tmp_list:
            if y not in validate:
                my_dict['words_stat'].setdefault(y.lower(), 0)
                my_dict['words_stat'][y.lower()] += 1

    # Сортировка
    tmp_dict = {}
    for i in sorted(my_dict['chars_stat'].keys()):
        tmp_dict[i] = my_dict['chars_stat'][i]
    del my_dict['chars_stat']
    my_dict['chars_stat'] = tmp_dict
    tmp_dict = {}
    for i in sorted(my_dict['words_stat'].keys()):
        tmp_dict[i] = my_dict['words_stat'][i]
    del my_dict['words_stat']
    my_dict['words_stat'] = tmp_dict
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
        print(('\'{}\' = {}').format(i, dict['chars_stat'][i])) if i != tab else print(
            ('{} = {}').format(repr(tab), dict['chars_stat'][i]))
    print('--- Статистика символов --->', end='\n\n')
    print('<--- Статистика слов ---')
    for i in dict['words_stat']:
        print(('\'{}\' = {}').format(i, dict['words_stat'][i]))
    print('--- Статистика слов --->')


show_stat(text_stat(input_text(), ['понедельник','суббота'], 'вторник', {0:'среда',4:'четвер'}))
