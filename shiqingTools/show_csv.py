'''
date:2020-11-24
author:shiqing
'''

import pandas as pd 
import argparse 



def show_csv(file):
    
    df = pd.read_csv(file)
    print("=============================Headlines=====================")
    print(df.head())

    print("===========================Columns=========================")
    print(df.columns)




if __name__ =="__main__":

    parser = argparse.ArgumentParser(description="Print csv head lines.")
    parser.add_argument('-f','--file',required=True)

    args = parser.parse_args()
    show_csv(args.file)