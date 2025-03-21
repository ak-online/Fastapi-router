from fastapi import FastAPI
from app.routers import task, user

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "My shop"}

app.include_router(task.router)
app.include_router(user.router)

#python -m uvicorn main:app
#uvicorn main:app --reload --port 8001