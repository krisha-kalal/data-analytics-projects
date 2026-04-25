import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

df = pd.read_csv(r"WA_Fn-UseC_-Telco-Customer-Churn.csv")

print(df.head())
print(df.info())

df = df.drop(columns=['customerID'])

df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

df = df.dropna()

df['Churn'] = df['Churn'].map({'Yes':1, 'No':0})

binary_cols = ['Partner', 'Dependents', 'PhoneService', 'PaperlessBilling']
for col in binary_cols:
    df[col] = df[col].map({'Yes':1, 'No':0})

print(df.info())
print(df.isnull().sum())

print(df['Churn'].value_counts())

print(df['Churn'].value_counts(normalize=True))

print(df.groupby('Contract')['Churn'].value_counts(normalize=True))

print(df.groupby('Churn')['MonthlyCharges'].mean())

print(df.groupby('Churn')['tenure'].mean())

print(df.groupby('PaymentMethod')['Churn'].value_counts(normalize=True))

sns.countplot(x='Churn', data=df)
plt.title("Churn Distribution")
plt.show()

sns.countplot(x='Contract', hue='Churn', data=df)
plt.title("Churn by Contract Type")
plt.show()

sns.boxplot(x='Churn', y='MonthlyCharges', data=df)
plt.title("Monthly Charges vs Churn")
plt.show()

sns.boxplot(x='Churn', y='tenure', data=df)
plt.title("Tenure vs Churn")
plt.show()

df_encoded = pd.get_dummies(df, drop_first=True)

x = df_encoded.drop('Churn', axis=1)
y = df_encoded['Churn']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

scaler = StandardScaler()

x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

model = LogisticRegression(max_iter=2000, class_weight='balanced')
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

df.to_csv("cleaned_churn_data.csv", index=False)