from fastapi  import  FastAPI

app = FastAPI()
@app.get("/")
def home():
    return {"message":"wallet app is running"}
