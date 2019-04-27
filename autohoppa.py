import glob
import pandas as pd
import numpy as np
import time

df = pd.concat([pd.read_csv(f) for f in glob.glob('input\\idealista_csv_*.csv')],
                ignore_index = True)

df.to_csv(".\\output\\FULL_Idealista_" 
            + time.strftime("%Y%m%d%H%M") 
            + ".csv",
            index = False,
            encoding = 'utf-8-sig')