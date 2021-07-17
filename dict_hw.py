'''Если посмотрите словари в питоне от похожи на словари из нашей жизни,
вам нужно сделать программу словарь которая будет переводить
слова из одного языка в другой сделать англо русский и Руско английский словарь,
программа должна быть бесконечным циклом которая всегда спрашивает инпут и переводит'''
while True:
    dictionary = {}
    n = int(input('Выберите язык: Eng-Rus(1) или Русс-Англ(2) или показать словарь(3)'))
    # for i in range(n):
    if n == 1:
        key1 = input('Enter a word: ')
        value1 = input('Enter translation: ')
            #dictionary[key1] = value1

    if n == 2:
        key2 = input('Введите слово: ')
        value2 = input('Введите перевод: ')
            # dictionary[key2] = value2

    if n == 3:
        dictionary[key1] = value1
        dictionary[key2] = value2
        print(dictionary)
