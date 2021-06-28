import requests as re
import bs4
import sqlite3 as sql
import datetime
import pandas as pd

conn = sql.connect('steam.db')

url = "https://store.steampowered.com/stats/"
a = re.get(url)
df = pd.read_html(a.text, displayed_only=False, header=0)[1]  
df = df.dropna(axis=1, how='all').dropna(axis=0, how='all') 
df['access_date'] = datetime.datetime.utcnow()

df.to_sql('top', conn, if_exists='append', index=False)
