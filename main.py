from fastapi import FastAPI, HTTPException
from transformers import pipeline
from src.models import Item

def init_fastapi():
    app = FastAPI()

    return app

def init_model(model_name):
    try:
        classifier = pipeline(model_name)
    except Exception as ex:
        return None

    return classifier

app = init_fastapi()
classifier = init_model("sentiment-analysis")

@app.get("/")
def root():
    return {"FastApi service started!"}

@app.get("/{text}")
def get_params(text: str):
    if classifier:
        return classifier(text)
    else:
        raise HTTPException(status_code=500, detail="Model not found!")

@app.post("/predict")
def predict(item: Item):
    if classifier:
        return classifier(item.text)
    else:
        raise HTTPException(status_code=500, detail="Model not found!")    