import pandas as pd
from fastapi import FastAPI, HTTPException, Header

df = pd.read_csv("players.csv")

app = FastAPI()

API_KEY = "apikeyftdssub02"

@app.get("/")
def homepage():
    return{"message":"Welcome to Players API"}

@app.get("/players")
def getAllPlayers(api_key:str=Header(None)):
    print(api_key)
    if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code = 401, detail="Wrong API Key")
    else:
        return df.to_dict(orient='records')
    
@app.get("/players/state/{state}")
def getPlayerbyState(state:str,api_key:str=Header(None)):
    print(api_key)
    print(state)
    if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code = 401, detail="Wrong API Key")
    else:
        player_by_state = df[df["state"]==state]
        return player_by_state.to_dict(orient='records')

@app.get("/players/pos/{position}")
def getPlayerbyposition(position:str,api_key:str=Header(None)):
    print(api_key)
    print(position)
    if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code = 401, detail="Wrong API Key")
    else:
        player_by_position = df[df["position"]==position]
        return player_by_position.to_dict(orient='records')  