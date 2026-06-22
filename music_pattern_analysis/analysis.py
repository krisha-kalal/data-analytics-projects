import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('dataset.csv')

print(df.columns.tolist())
print(df.head())
print(df.describe())
print(df.info())

df = df.drop(columns=['Unnamed: 0','track_id'])

print("Total songs:", len(df))
print("Total Artists:", df['artists'].nunique())
print("Total Genres:", df['track_genre'].nunique())
print("Average Popularity:", df['popularity'].mean())

top_genres = df['track_genre'].value_counts().head(10)
top_genres.plot(kind='bar')
plt.title('Top 10 Genres')
plt.show()

plt.hist(df['popularity'], bins=20)
plt.title('Popularity Distribution')
plt.show()