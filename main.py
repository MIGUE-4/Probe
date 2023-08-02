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


@app.get("/index")
def index():

    return 'prueba'

class fecha_gen(BaseModel):
   year : str


@app.post("/genero")
def genero(fecha:fecha_gen):
   
   return {f"El año de {fecha.year} tuvo estos 5 géneros más vendidos":
           data[data['release_date'].str[0:4] == fecha.year]['genres'].value_counts().head(5).index.to_list()
           }


class juegos_year(BaseModel):
   year : str

@app.post("/juegos")
def genero(juego:juegos_year):
   
   return {f"Juegos lanzados en {juego.year}":
           data[data['release_date'].str[0:4] == '2010']['title'].unique().tolist()}