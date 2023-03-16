#ETL on spotify data

#Downloaded data from spotify manually, couldve done it with kaggle API

#extracting archive.zip
from zipfile import ZipFile
with ZipFile("data/archive.zip", 'r') as zObject:
    zObject.extractall(path='data/')

#data preprocessing
import pandas as pd

#saving the csv file extracted to a DataFrame object
df=pd.read_csv('data/songs_normalize.csv')

#dropping duplicates
df.drop_duplicates(inplace=True)

#removing values which have genre=set()
df = df[df['genre'] != 'set()']

#saving the dataframe to a csv file
df.to_csv('data/df.csv', index=False)

#importing sqlite3 to perform SQL statements on df in order to obtain new dataframes
import sqlite3

#connecting to database
con = sqlite3.connect("spotify.db")
cur = con.cursor()

#deploying df in this database
df.to_sql("spotify_data", con, if_exists='replace', index=False)  

#since the data is inbalanced for the release years 1998 and 2020, we delete these songs.
cur.execute('DELETE FROM spotify_data WHERE year == 1998 OR year == 2020')

#generating new dataframes
df_year = pd.read_sql_query("""

SELECT year, COUNT(year) as Number_of_releases, 
AVG(duration_ms) as Average_duration, 
AVG(explicit) as Explicit_ratio,
AVG(danceability) as Average_danceability, 
AVG(energy) as Average_energy, 
AVG(loudness) as Average_loudness, 
AVG(speechiness) as Average_speechiness,
AVG(acousticness) as Average_acousticness, 
AVG(instrumentalness) as Average_instrumentalness,
AVG(liveness) as Average_liveness, 
AVG(valence) as Average_valence, 
AVG(tempo) as Average_tempo FROM spotify_data GROUP BY year

""", con)

df_genre = pd.read_sql_query("""

SELECT genre, COUNT(genre) as Number_of_songs, 
AVG(duration_ms) as Average_duration, 
AVG(explicit) as Explicit_ratio,
AVG(danceability) as Average_danceability, 
AVG(energy) as Average_energy, 
AVG(loudness) as Average_loudness, 
AVG(speechiness) as Average_speechiness,
AVG(acousticness) as Average_acousticness, 
AVG(instrumentalness) as Average_instrumentalness,
AVG(liveness) as Average_liveness, 
AVG(valence) as Average_valence, 
AVG(tempo) as Average_tempo FROM spotify_data GROUP BY genre

""", con)

#changing the release year datatype to str on df_year
df_year['year'] = df_year['year'].values.astype('str')

#removing some imbalancies
df_genre = df_genre[df_genre['Number_of_songs'] > 3]
df_genre.reset_index().drop(['index'], axis=1)

#saving the dataframes to csv
df_year.to_csv('data/df_year.csv', index=False)
df_genre.to_csv('data/df_genre.csv', index=False)
