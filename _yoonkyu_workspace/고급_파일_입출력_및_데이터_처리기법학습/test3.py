import pandas as pd

df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
print(df)

df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns=['가', '나', '다'])
print(df)


data = {
    'name': ['김', '이', '박'],
    'age': [24, 27, 34],
    'children': [2,1,3]
}

print(pd.DataFrame(data))

print(df.index)

print(pd.DataFrame(data).columns)

print(pd.DataFrame(data).values)

print(pd.DataFrame(data).dtypes)

print(pd.DataFrame(data).T)

df = pd.DataFrame(data)
df.index = list('abc')
print(df)