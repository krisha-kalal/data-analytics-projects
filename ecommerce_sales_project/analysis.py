import pandas as pd

df = pd.read_csv(r"dataset\Amazon Sale Report.csv")

print(df.head())
print(df.info())

df = df.drop(columns=['index', 'Unnamed: 22'])

df['Date'] = pd.to_datetime(df['Date'], format='%m-%d-%y')

df = df.dropna(subset=['Amount','ship-city', 'ship-state', 'ship-country'])

df['Courier Status'] = df['Courier Status'].fillna('Unknown')
df['currency'] = df['currency'].fillna('INR')
df['fulfilled-by'] = df['fulfilled-by'].fillna('Not Specified')
df['promotion-ids'] = df['promotion-ids'].fillna('No Promotion')

df['ship-postal-code'] = df['ship-postal-code'].astype(str)

df = df.drop_duplicates()

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

print(df.info())
print(df.isnull().sum())

total_revenue = df['Amount'].sum()
print("Total Revenue:", total_revenue)

monthly_sales = df.groupby('Month')['Amount'].sum().sort_index()
print(monthly_sales)

category_sales = df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
print(category_sales)

state_sales = df.groupby('ship-state')['Amount'].sum().sort_values(ascending=False).head(10)
print(state_sales)

b2b_sales = df.groupby('B2B')['Amount'].sum()
print(b2b_sales)

status_counts = df['Status'].value_counts()
print(status_counts)

df.to_csv("dataset\Amazon Sale Report Cleaned.csv", index=False)