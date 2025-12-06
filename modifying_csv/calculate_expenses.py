import pandas as pd
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument("file", type=str, help="specify csv file")
argparser.add_argument("column_name", type=str, help="specify column name file")
args = argparser.parse_args()

df = pd.read_csv(args.file)
column_name = args.column_name
# df = pd.read_csv('expenses.csv')
# pd.set_option('display.max_columns', 100)
# pd.set_option('display.max_rows', 100)

total_amount = round(df[column_name].sum(), 2)
max_amount = round(df[column_name].max(), 2)

print(f'Total amount:{total_amount}')
print(f'Highest amount:{max_amount}')