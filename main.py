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

@app.get("/index/")
def index():

    return 'prueba'