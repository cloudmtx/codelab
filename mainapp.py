from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Helloooo World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/items/", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

# mount subapplication

subapi = FastAPI()

@subapi.get("/sub")  # sub application root is /subapi, so this is /subapi/sub
def read_sub():
    return {"message": "Hello World from sub API"}

app.mount("/subapi", subapi)