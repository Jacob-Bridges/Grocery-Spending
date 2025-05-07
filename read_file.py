import os
import pandas as pd
pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 216)

#This program reads csv files containing transaction data

#Use Try/Except to handle FileError issues
try:
    df = pd.read_csv('all_purchases_0524_0525.csv', parse_dates=['Transaction Date'])
except FileNotFoundError:
    print('Program cannot find file.')



#get_groceries returns a new dataframe containing records with the string HARRIS TEETER in the Description column
def get_groceries():
    mask = df.apply(lambda x: x.astype(str).str.contains('HARRIS TEETER')).any(axis=1)
    result = df[mask]
    new_df = result.drop(columns=['Posted Date', 'Card No.', 'Credit'])
    sorted_df = new_df.sort_values(by ='Transaction Date', ascending=False)
    

    return sorted_df








