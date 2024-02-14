import pandas as pd
import numpy as np

arr = np.arange(100,105)

print(arr)

s = pd.Series(arr, dtype='int64')
print(s)

s = pd.Series(arr, dtype='int32')
print(s)

s = pd.Series([91, 2.5, '스포츠', 4, 5.16])
print(s)

s = pd.Series(['부장', '차장', '대리', '사원', '인턴'])
print(s)

print(s.index)
print(s[0])

print(s[[1,3]])

print(s[np.arange(1,4,2)])

np.random.seed(0)
s = pd.Series(np.random.randint(10000,20000, size=(10,)))
print(s>15000)

s[s>15000]


s = pd.Series(['마케팅', '경영', '개발', '기획', '인사'])
print(s.index)

s.index = list('abcde')
print(s)

print(s.values)

print(s.ndim)

print(s.shape)

s = pd.Series(['선화', '강호', np.nan, '소정', '우영'])
print(s)
print(s.isnull())

print(s[s.isnull()])
print(s[s.notnull()])

s = pd.Series(np.arange(3,12,2), dtype="float32")
print(s)

print(pd.Series(list('가나다라마')))

sample = pd.Series(np.arange(10,60,10), dtype='int64', index=list('가나다라마'))
print(sample)

print(sample[['나','라']])

np.random.seed(20)
sample2 = pd.Series(np.random.randint(100,200, size=(15,)))
print(sample2)

print(sample2[sample2 <= 160])
print(sample2[(sample>=130)&(sample2 <= 170)])

print(pd.Series(['apple', np.nan, 'banana', 'kiwi', 'gubong'], index=list('가나다라마')))

sample = pd.Series(['IT서비스', np.nan, '반도체', np.nan, '바이오', '자율주행'])
print(sample)

print(sample[sample.isnull()])
print(sample[sample.notnull()])

np.random.seed(0)
sample = pd.Series(np.random.randint(100,200, size=(10,)))
print(sample)

print(sample[2:7])

np.random.seed(0)
sample2 = pd.Series(np.random.randint(100,200,size=(10,)), index=list('가나다라마바사아자차'))
print(sample2)
print(sample2['바':])
print(sample2[:'다'])
print(sample2['나':'바'])
