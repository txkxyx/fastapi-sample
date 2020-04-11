# FastAPI入門

## Hello World

```python:main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

## パスパラメータの取得

```python:main.py
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/item/{item_id}")
def read_item(item_id):
    return {"item_id":item_id}

@app.get("/int/{num}")
def read_item(num: int):
    return {"num":num}

@app.get("/int/validation/{num}")
def read_item_validation(num: int = Path(..., gt=10, le=30)):
    return {"num":num}

@app.get("/float/{num}")
def read_float(num: float):
    return {"num": num}

@app.get("/boolean/{boolean}")
def read_boolean(boolean: bool):
    return {"boolean": boolean}
```

`http://127.0.0.1:8000/int/validation/11`

## クエリパラメータの取得

```python:main.py
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items")
def read_items(limit: int = 0, sort: str = "desc", option: bool = False):
    if option:
        return {"limit":limit, "sort": sort, "option": option}
    return {"limit":limit, "sort": sort}

@app.get("/item")
def read_item(item_id: str = Query(None, min_length=3, max_length=15, regex="^item_")):
    return {"item_id": item_id}

```

`http://127.0.0.1:8000/items?limit=10&sort=asc&option=True`

`http://127.0.0.1:8000/item?item_id=aaaaa`

## リクエストボディ

