from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

class Form(BaseModel):
    string: str
    numbet: int
    decimal: float
    boolean: bool

@app.get("/item/{item_id}")
def read_item(form: Form):
    if form:
        return {"form": form}
    return {"form": None}