import dash
from dash import dcc, html

dash.register_page(__name__)

dataset1 = ["""
The original dataset can be found at""", html.A(' this link. ', href='https://www.kaggle.com/datasets/paradisejoy/top-hits-spotify-from-20002019', className='how-text'),"""It defined as the union of the top100 songs of each year from 2000 to 2019. 
I picked this dataset, because I always wanted to explore music data. I am a very big fan of Spotify, and use the app on a daily basis. Not only the music intrigues me, but also the functional algorithms and machine learning algorithms behind the app 
spark my curiosity. 
Though, after the ETL process, I came to the conclusion that it was not the best dataset to use. It had duplicates and strange values which I had to remove. Additionally, some properties of specific songs seem awfully defined. In particular,
how can """, html.A("Feel the love", href="https://www.youtube.com/watch?v=oABEGc8Dus0&ab_channel=Rudimental", className="how-text"), """ by Rudimental and John Newman have a dancability score of only 0.389? 
"""]

dataset11 = """
I manually downloaded the dataset from the website. I could have used the requests package or the kaggle API to do this, but downloading was easier. I unzipped the file in the folder 
and loaded the csv file using Pandas. The fields or columns in this dataset are:"""

datasetcolumns = """['Artist',
     'Song Name',
     'Duration (Milliseconds)',
     'Explicit',
     'Release Year',
     'Popularity',
     'Danceability',
     'Energy',
     'Key',
     'Loudness (Db)',
     'Mode',
     'Speechiness',
     'Acousticness',
     'Instrumentalness',
     'Liveness',
     'Valence',
     'Tempo (BPM)',
     'Genre']"""


dataset12 = """'Explicit' is a binary value which indicates if a song has curse words, energy is a measure of intensity and activity, key indicates in which key a track is in. E.g. C=0,
mode is a binary value representing the modality of a track where major is 1, speechiness is a measure of presence of spoken words, liveness is a measure of an audience in the recording, valence is a measure of musical positiveness in the song. For more information, see the website linked above. 
After using some exploratory methods built in Pandas like .describe() and .info(). I went on to check for NULL values, duplicates and ordinary classes. 
The thought of preprocessing certain songs which have multiple genres crossed my mind, but I felt that this would generalize the genres too much. I used Matplotlib to draw the first scatter plots.
Additionally, I used seaborn to draw the first correlation plot. I performed some EDA on both, you can find these comments in the Jupyter Notebook. 
"""

dataset2 = """
The second and third datasets were created by using the SQLite library. After creating the database 'spotify.db', I wrote SQL queries to define two new SQL tables and immediately converted them to Pandas
DataFrame objects. I know that Pandas also has a 'group by' method, however SQL is much more easy to use. After obtaining both dataframes, I performed ETL in order to see if the data quality and balance was still maintained.
By looking at the dataset grouped by release year, I saw a small number of songs coming from 1998 and 2020. Since this was totally unbalanced with the rest of the dataset, I removed them. Looking at the genre dataset, I left in the combination-genres ['Pop, Rock, Hip Hop', 'Metal, Pop, Rock'] 
in the dataset. But these genres only had one or two songs present in the dataset, so I also removed these. Initially, I wanted to make the dashboard in Jupyter Notebook, but there was a compability issue, so I made the dashboard in Virtual Studio Code on a .py file. 
"""

layout = html.Div([html.H1('Original dataset', className='H1-1'),
                  html.H1(dataset1, className='H1-2'),
                  html.H1(dataset11, className='H1-2'),
                  html.H1(datasetcolumns, className='H1-2'),
                  html.H1(dataset12, className='H1-2'),
                  html.H1('Two additional datasets', className='H1-1'),
                  html.H1(dataset2, className='H1-2'),], className='how-container')
