import pandas as pd
import os
from datetime import datetime

# Checks for existing data

if os.path.exists('expenses.scv'):
    df = pd.read_csv('expenses.csv')
    print(f"Loaded existing expense: {len(df)} rows")
    print("Here's what's loaded")
    print(df)
    print(f"DataFrame info: {df.shape}")

else: 
    # Creates empty DataFrame with columns
    df = pd.DataFrame(columns = ['date', 'category', 'amount', 'description'])
    print("Created new expense tracker")

# Print current expenses
print("\nCurrent expenses: ")
print(df)

# Add a new expense
new_expense = pd.DataFrame([{
    'date': datetime.now().strftime('%Y-%m-%d'),
    'category':'Food',
    'amount': 15.50,
    'description': 'Lunch'
    }])

# df = pd.concat([df, new_expense], ignore_index=True)

print("\nCurrent expenses AFTER adding: ")
print(df)
print(f"Number of rows: {len(df)}")

# Save it
df.to_csv('expense.csv', index=False)
print("\nExpense added!")
print(df)

