from fastapi import FastAPI
from pydantic import BaseModel
import ast
import pandas as pd


app = FastAPI()

with open(r'steam_games.json') as file:

    data = []
    for line in file.readlines():
      
      data.append(ast.literal_eval(line))

data = pd.DataFrame(data)


class fecha_gen(BaseModel):
   year : str


@app.post("/genero")
def genero(fecha:fecha_gen):
   
   return data[data['release_date'].str[0:4] == fecha.year]['genres'].value_counts().head(5).index.to_list()
        


class juegos_year(BaseModel):
   year : str

@app.post("/juegos")
def genero(juego:juegos_year):
   
   return data[data['release_date'].str[0:4] == juego.year]['title'].unique().tolist()

class specs_year(BaseModel):
   year : str

@app.post("/specs")
def specs(spec:specs_year):
   
   return data[data['release_date'].str[0:4] == spec.year].specs.value_counts().head(5).index.tolist()

class early_year(BaseModel):
   year : str

@app.post("/earlyacces")
def specs(early:early_year):
   
   return data[data['release_date'].str[0:4] == early.year].early_access.value_counts().loc[True]
   

class metascore_year(BaseModel):
   year : str

@app.post("/metascore")
def specs(early:metascore_year):
    return data[data['release_date'].str[0:4] == early.year].sort_values('metascore', ascending=False).head(5)['title'].tolist()

class sentiment_year(BaseModel):
   year : str

@app.post("/sentiment")
def specs(sent:sentiment_year):
    return data[data['release_date'].str[0:4] == sent.year]['sentiment'].value_counts().to_dict()
    

