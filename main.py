from fastapi import FastAPI
from pydantic import BaseModel
import ast
import pandas as pd
import re


app = FastAPI()

with open(r'steam_games.json') as file:

    data = []
    for line in file.readlines():
      
      data.append(ast.literal_eval(line))

data = pd.DataFrame(data)


def format_date(fecha):
    patron = r'^\d{4}-\d{2}-\d{2}$'
    
    return re.match(patron, str(fecha)) is not None

data = data[data['release_date'].apply(format_date)]
data.release_date = pd.to_datetime(data.release_date)

@app.get("/genero/{fecha}")
def genero(fecha:int):
   
   return data[data['release_date'].dt.year == fecha]['genres'].value_counts().head(5).index.to_list()
        

@app.get("/juegos/{fecha}")
def juegos(fecha:int):
   
   return data[data['release_date'].dt.year == fecha]['title'].unique().tolist()


@app.get("/specs/{fecha}")
def specs(fecha:int):
   
   return data[data['release_date'].dt.year  == fecha].specs.value_counts().head(5).index.tolist()



@app.get("/earlyacces/{fecha}")
def earlyacces(fecha:int):
   
   return int(data[data['release_date'].dt.year == fecha].early_access.value_counts()[True])
   

@app.get("/metascore/{fecha}")
def metascore(fecha:int):
    return data[data['release_date'].dt.year == fecha].sort_values('metascore', ascending=False).head(5)['title'].tolist()


@app.get("/sentiment/{fecha}")
def sentiment(fecha:int):
    return data[data['release_date'].dt.year == fecha]['sentiment'].value_counts().to_dict()
    

