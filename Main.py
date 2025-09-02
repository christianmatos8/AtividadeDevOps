from fastapi import FastAPI

app = FastAPI()

#http://127.0.0.1:8000
@app.get("/")
async def root():
    return{"message", "hello"}

@app.get("/test")
async def teste():
    return{"message", "deu certo"}