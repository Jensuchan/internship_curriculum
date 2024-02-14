import nltk
from nltk.corpus import stopwords
nltk.download('punkt')

from collections import *
from nltk import *
#from nltk.corpus import word_tokenize

cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1

print(cnt)
    
"""
import re

words = re.findall(r'\w+', open('hamlet.txt').read().lower())
#print(Counter(words).most_common(10))

hamlet_text = open('hamlet.txt', 'r', encoding="utf-8")
text = hamlet_text.read()
#print(text)
words = word_tokenize(text)
count = Counter()
#print(words)
for word in words:
    count[word] += 1

print(count.most_common(5))


"""
"""
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from collections import *

with open('hamlet.txt') as file:
    text = file.read()

words = word_tokenize(text)

stopwords = set(nltk.corpus.stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stopwords]

nouns = [word for word in words if wordnet.synsets(word)[0].pos() == 'n']

noun_count = Counter(nouns)

for noun, freq in noun_count.most_common(10):
    print(noun, freq)
"""