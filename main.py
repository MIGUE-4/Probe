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
   
   return {data[data['release_date'].str[0:4] == fecha.year]}