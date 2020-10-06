from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from core.models.Bien import Bien
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/estimate/")
async def read_item(metre_carre: int = 0, nb_pieces: int = 0, terrain: int = 0, code_postal: int = 0):
    # metre_carre : le nombre de m² habitables loi Carrez
    # nb_pieces : nombre de pièces principales
    # terrain : le nombre de m² du terrain
    # code_postal : le code postal où se trouve le bien
    
    bien = Bien(metre_carre, nb_pieces, terrain, code_postal)
     
    bien.calcul_estimation()

    return bien


if __name__ == "__main__":
    uvicorn.run(app, port=5003)