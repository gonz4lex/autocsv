import glob
import pandas as pd
import numpy as np
import time
import os


def concat_csv(input_dir, pattern = ''):
    files = [f for f in glob.glob(f'{input_dir}\\{pattern}.csv')]
    print('Concatenating files:')
    [print(f) for f in files]

    df = pd.concat([pd.read_csv(f) for f in glob.glob(f'{input_dir}\\{pattern}.csv')],
                    ignore_index = True)

    return df

def save_csv(df, output_dir = 'output', pattern = 'autocsv_'):
    df.to_csv(".\\{output_dir}\\{pattern}" 
                + time.strftime("%Y%m%d%H%M") 
                + ".csv",
                index = False,
                encoding = 'utf-8-sig')


def main():
    pattern = input("Specify the pattern of the files to concatenate. You can use regular expressions. > ")
    path = os.path.dirname(os.path.abspath(__file__))
    print(path + '\\input')
    df = concat_csv(path + '\\input', pattern)

    print(df)
    print('--------------------',
          '--------------------',
          '--------------------')
    
    save = input("Do you want to save the results to a file? (y/n) >")

    if save.lower() == 'y':
        save_csv(df, path, pattern)


if __name__ == "__main__":
    main()