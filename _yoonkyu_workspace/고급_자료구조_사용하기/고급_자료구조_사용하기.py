from collections import Counter
import nltk
from nltk.corpus import *
from nltk.tokenize import word_tokenize


text1 = """동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세. 
무궁화 삼천리 화려강산 
대한 사람, 대한으로 길이 보전하세

남산 위에 저 소나무, 철갑을 두른 듯 
바람서리 불변함은 우리 기상일세. 
무궁화 삼천리 화려강산 
대한 사람, 대한으로 길이 보전하세

가을 하늘 공활한데 높고 구름 없이 
밝은 달은 우리 가슴 일편단심일세. 
무궁화 삼천리 화려강산 
대한 사람, 대한으로 길이 보전하세

이 기상과 이 맘으로 충성을 다하여 
괴로우나 즐거우나 나라 사랑하세. 
무궁화 삼천리 화려강산 
대한 사람, 대한으로 길이 보전하세

무궁화""" 

def getCount(textData):
    words = nltk.word_tokenize(textData)
    words = [word for word in words if word.isalpha()]
    return words

def getFrequency(words):
    cnt = Counter()
    for word in words:
        cnt[word] += 1
    return print("단어들의 빈도수 >> ", cnt)
    #return print("단어들 중 최빈값 >> ", cnt.most_common(1))


with open('test.txt', 'r', encoding="utf-8") as file:
    textData = file.read()
words = getCount(textData)
getFrequency(words)
