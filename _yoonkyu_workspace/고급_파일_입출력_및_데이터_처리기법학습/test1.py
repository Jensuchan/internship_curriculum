"""
Pandas
    > 데이터 처리와 분석을 위한 라이브러리
    > 행과 열로 이루어지 데이터 객체를 만들어 다룰 수 있음(table 등)
    > 대용량의 데이터들을 처리하는데 매우 편리
    > 자료구조
        >> 1차원 : Series
        >> 2차원 : DataFrame
        >> 3차원 : Panel
    > pandas 로딩
        import numpy as np # 보통 numpy와 함께 import함
        import pandas as pd
"""

import pandas as pd
pd
"""
data = {
    'year': [2016, 2017, 2018],
    'GDP rate': [2.8, 3.1, 3.0],
    'GDP': ['1.637M', '1.73M', '1.83M']
}

df = pd.DataFrame(data, index=data['year'])
print(df)
"""
print("pandas 모듈 >> ",pd)

print("pandas버젼 >> ",pd.__version__)



