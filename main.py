from fastapi import FastAPI, APIRouter
from todo import todo_router

router = APIRouter()
app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name':'Nawfaa'}}

@app.get("/output")
async def welcome() -> dict:
    return {'message': 'Hello Nawfsaa'}

app.include_router(todo_router)    