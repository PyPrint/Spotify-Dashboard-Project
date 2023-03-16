import dash
from dash import dcc, html

dash.register_page(__name__, path='/', name='How')

intro1 = ["""
Hello everyone, my name is Jurriaan Engels. I am 25 years old and live in the vicinity of Amsterdam in the Netherlands. I have a master's degree in pure mathematics from the University of Amsterdam
and am now on the road to becoming a Junior Data Scientist or Junior Data Analyst. This highly-interactive dashboard will be the first in a series of portfolio projects that I will present on my resumé, post on my """, html.A('Github', href="https://github.com/PyPrint", className="how-text"), " and ", html.A("LinkedIn.", href="https://www.linkedin.com/in/jurriaan-engels-9ab6b3113/", className="how-text"),  
"""Thereby showing all the programming, analytical, mathematical, machine learning and storytelling skills I have gathered over the years. These projects will be 100 percent original, because I believe that you will only learn true data science
by actually doing it, instead of repeating the lines of code that someone has already made for you.
"""]

how1 = f"""
In this highly-interactive Spotify Music Knowledge Dashboard, made with Plotly Dash, HTML and CSS, you are able to visualize three datasets using scatterplots, histogram charts, correlation heatmaps and more. 
The three datasets are based on a Spotify dataset taken from Kaggle. There are four sections to this dashboard. You are now in the first section. It contains this introductory page, 
a page with information of the three datasets and a hyperlink to the Github repository where you can find all of the files used for this dashboard and an additional Jupyter Notebook 
filled with many more insights and EDA. 
"""

how3 ="""
In the second section, there is an overview of the original dataset that has undergone ETL, 
a 3D-color-scatter plot of the fields present in the dataset, a correlation plot and a four-histogram-grid which shows the distributions and the medians.
"""

how4 ="""
The third section contains the dataset that has been grouped by release year, a correlation- and line plot of the averaged numerical values of the fields corresponding to a release year. 
"""

how5 ="""
The last section accomodates a view of the dataset grouped by music genre, a scatter- and correlation plot of the averaged numerical field values corresponding to a specific music genre. 
"""

how6 = """
To make the dashboard active and usable, it is uploaded to Render. Render is a service that hosts any plotly dash application for free online. 
"""

layout = html.Div([html.H1('Brief introduction of myself', className='H1-1'),
                  html.H1(intro1, className='H1-2'),
                  html.H1('How does this dashboard work?', className='H1-1'),
                  html.H1(how1, className='H1-2'),
                  html.H1(how3, className='H1-2'),
                  html.H1(how4, className='H1-2'),
                  html.H1(how5, className='H1-2'),
                  html.H1(how6, className='H1-2')], className='how-container')
