import pandas as pd

df = pd.read_csv('sample_directory/expenses.csv')

# pd.set_option('display.max_columns', 100)
# pd.set_option('display.max_rows', 100)

total_amount = df['amount'].sum()
max_amount = df['amount'].max()

print(f'Total amount:{total_amount}')
print(f'Highest amount:{max_amount}')