import glob
import pandas as pd
import numpy as np
import time

# ! This begs for OOP implementation.

class Csv(object):
    def __init__(self, input_dir, output_dir, pattern, *args, **kwargs):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.pattern = pattern
    

    def concat_csv(self):
        files = [f for f in glob.glob(f'{self.input_dir}\\{self.pattern}.csv')]
        print('Concatenating files:',
            files)

        df = pd.concat([pd.read_csv(f) for f in glob.glob(f'{self.input_dir}\\{self.pattern}.csv')],
                        ignore_index = True)

        return df


    def save_csv(self, df):
        df.to_csv(".\\{output_dir}\\{pattern}" 
                    + time.strftime("%Y%m%d%H%M") 
                    + ".csv",
                    index = False,
                    encoding = 'utf-8-sig')