from typing import Optional

from fastapi import FastAPI
from firstgraph import first_graph_return

from predict import predictions

app = FastAPI()


@app.get("/")
def read_root():
    return "Server started"

@app.get("/predict")
def read_root():
    return predictions()



@app.get("/first_graph")
def read_root():
    return first_graph_return()

