# Speed up your data processes (Rob Mulla)
# https://www.youtube.com/watch?v=u4rsA5ZiTls

import pandas as pd
import numpy as np

def get_random_dataset(size):
    df = pd.DataFrame()
    df['id'] = np.arange(1, size + 1)
    
    df['size'] = np.random.choice(['big', 'medium', 'small'], size)
    df['size'] = df['size'].astype('category')

    df['age'] = np.random.randint(1, 50, size)
    df['age'] = df['age'].astype('int16')


    df['team'] = np.random.choice(['red', 'blue', 'yellow', 'green'], size)
    df['team'] = df['team'].astype('category')

    df['win'] = np.random.choice(['yes', 'no'], size)
    df['win'] = df['win'].map({'yes' : True, 'no' : False})

    dates = pd.date_range('2020-01-01', '2022-12-31')
    df['date'] = np.random.choice(dates, size)

    df['prob'] = np.random.uniform(0, 1, size)
    df['prob'] = df['prob'].astype('float')

    return df

df = get_random_dataset(1_000)

print(df.head())

