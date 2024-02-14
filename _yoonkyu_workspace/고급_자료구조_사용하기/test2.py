from collections import *

d = defaultdict(int)

d = defaultdict(int, {'apple':3, 'banana':2, 'cherry':1})
print("d['apple'] 의 값 : ",d['apple'])
print("d['orange'] 의 값 : ",d['orange'])

d['orange'] = 4
print("d['orange'] 의 값 : ", d['orange'])








"""
import nltk
import pickle
from nltk.corpus import stopwords
import re
from collections import *
nltk.download('punkt')


nltk.download('stopwords')

with open('hamlet.txt', 'r', encoding="utf-8") as file:
    text = file.read()

#print(text)

filtered_content = text.replace('!', '').replace(',','').replace('.','').replace('“','').replace('”','').replace('\n','').replace('’','')
#print("필터먹은 문장들 >>",filtered_content)
filtered_content = filtered_content.lower()


stopwords_list = stopwords.words('english')
print('stopwords : ', len(stopwords_list))
print(stopwords_list)

word_tokens = nltk.word_tokenize(filtered_content)
#print("단어들 >>",word_tokens)

tokens_pos = nltk.pos_tag(word_tokens)
#print(tokens_pos)

NN_words = []
cnt = Counter()
for word, pos in tokens_pos:
    if 'NN' in pos:
        NN_words.append(word)
#print(NN_words)

for word in NN_words:
    cnt[word] += 1

#print(cnt.most_common(5))

ham_count = Counter()

for word in NN_words:
    ham_count['ham.'] += 1

print(ham_count)

for word in NN_words:
    if word.endswith('let'):
        ham_count['hamlet'] += 1
#print('햄카운트 >> ', ham_count)
"""