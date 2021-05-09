from django.shortcuts import render
from django.conf import settings
import csv


def inflation_view(request):
    readers_keys = []  
    readers_items = []  
    dir = settings.BASE_DIR + '/inflation_russia.csv'  
    with open(dir, encoding='utf-8') as csvfile: 
        reader = csv.DictReader(csvfile,
                                delimiter=';') 
        for row in reader: 
            reader_keys_key = []
            readers_items_item = []  
            for keys, item in row.items():  
                reader_keys_key.append(keys)  
                try:  
                    readers_items_item.append(int(item))  
                except ValueError:
                    try:  
                        readers_items_item.append(float(item))  
                    except ValueError:
                        readers_items_item.append("")  
            readers_items.append(readers_items_item)  
            readers_keys.append(reader_keys_key)
    template_name = 'inflation.html'
    context = {
        'csv_reader_keys': readers_keys,
        'csv_reader_items': readers_items
    }
    return render(request, template_name, context)
