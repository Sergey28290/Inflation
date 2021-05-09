from django.shortcuts import render
from django.conf import settings
import csv


def inflation_view(request):
    readers_keys = []  # массив для шапки таблицы
    readers_items = []  # создаем массив для значений инфляции
    dir = settings.BASE_DIR + '/inflation_russia.csv'  # переходим в корневую папку и находим там файл
    # dir = 'C:/Users/serge/Documents/PYTHON/Django/Inflation/inflation_russia.csv'
    with open(dir, encoding='utf-8') as csvfile:  # и открываем файл на чтение с кодировкой, т.к. текст русский
        reader = csv.DictReader(csvfile,
                                delimiter=';')  # записываем результат в виде множества словарей { {'...': ...} }
        for row in reader:  # перебираем его
            reader_keys_key = []
            readers_items_item = []  # список для занесения значений инфляции
            for keys, item in row.items():  # перебираем словари, метода items(), возвращает список пар «ключ—значение»
                reader_keys_key.append(keys)  # добавляем в список шапку таблицы
                try:  # пытаемся добавить в этот список значение, приобразованное в int
                    readers_items_item.append(int(item))  # передаем года, т.к. они типа int
                except ValueError:
                    try:  # пытаемся добавить в список значение приобразованное в float
                        readers_items_item.append(float(item))  # передаем значение инфляции, т.к. они типа float
                    except ValueError:
                        readers_items_item.append("")  # и пустые значение оставляем пустыми
            readers_items.append(readers_items_item)  # добавляем это все в общий список
            readers_keys.append(reader_keys_key)
    template_name = 'inflation.html'
    # чтение csv-файла и заполнение контекста
    context = {
        'csv_reader_keys': readers_keys,
        'csv_reader_items': readers_items
    }
    return render(request, template_name, context)
