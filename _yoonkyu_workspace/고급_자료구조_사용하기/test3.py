
from collections import OrderedDict

d = OrderedDict()

d = OrderedDict({'apple':3, 'banana':2, 'cherry':1})
d.update({'apple':3, 'banana':2})
d['cherry'] = 1
d[1] = 'one'
d[2] = 'two'
d.update({3: 'three'})
d[4] = 'four'
d.update({5: 'five'})
for key, value in d.items():
    print(key, value)




"""
import nltk
nltk.download('punkt')

with open('hamlet.txt', 'r', encoding="utf-8") as file:
    text = file.read()

print(text)
"""
