from fastapi import FastAPI
from gacha_logic import draw_gacha

app = FastAPI()

@app.get("/")
def read_root():
    return {"result": draw_gacha()}
