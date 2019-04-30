import numpy as np
import pandas as pd
import sys


def validate(file_name):
    df = pd.read_csv(file_name)
    df_correct = pd.read_csv('data.csv')
    try:
        if (np.any(df_correct.dtypes != df.dtypes)):
            raise ValueError()
    except (ValueError):
        print('Input DataFrame does not contain the correct data type.')
        exit()
    try:
        if (sorted(list(df)) != sorted(list(df_correct))):
            raise ValueError()
    except (ValueError):
        print('Input DataFrame does not contain the expected columns.')
        exit()
    try:
        if len(df.index) < 1:
            raise ValueError()
    except (ValueError):
        print("Input DataFrame does not have at least 1 row.")
        exit()
    print('Congratulations, input dataframe passes all checks.')

if __name__ == '__main__':
    validate(sys.argv[1])
