import csv
import os
import argparse

parser = argparse.ArgumentParser(description='csv file')
parser.add_argument('-f', '--file', dest='csv', type=str, required=True)

args = parser.parse_args()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meta.settings')

import django

django.setup()



from core.models import Psychoterapist, Method, Data

with open(args.csv, newline='', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    count = 0
    text = ''
    for row in spamreader:
        text += ','.join(row) + '\n'
        if count != 0:
            name = row[0]
            photo = row[1].split(' ')[1][1:-1]
            methods = row[2].split(',')

            if Psychoterapist.objects.filter(name=name).exists():
                p = Psychoterapist.objects.get(name=name)
                if not Psychoterapist.objects.filter(name=name, photo=photo).exists():
                    p.photo = photo
                    p.save()
                for method in methods:
                    try:
                        m = Method.objects.get(name=method)
                    except:
                        m = Method.objects.create(name=method)
                    if not p.methods.filter(pk=m.pk).exists():
                        p.methods.add(m)

                ms = Method.objects.filter(psychoterapist__name=name).exclude(name__in=methods)
                for item in ms:
                    p.methods.remove(item)
                    
            else:
                p = Psychoterapist(name=name, photo=photo)
                p.save()
                for method in methods:
                    try:
                        m = Method.objects.get(name=method)
                    except:
                        m = Method.objects.create(name=method)
                    p.methods.add(m)
        count += 1  
    Data.objects.create(data=text)