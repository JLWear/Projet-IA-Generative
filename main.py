from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline, Pipeline
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

generator: Pipeline = None

history: List[dict] = []

def load_model():
    global generator
    try:
        generator = pipeline("text-generation", model="gpt2")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors du chargement du modèle: {e}")

load_model()

class TextRequest(BaseModel):
    prompt: str

@app.post("/generate/")
async def generate_text(request: TextRequest):
    global history, generator
    if generator is None:
        raise HTTPException(status_code=500, detail="Le générateur de texte n'a pas pu être chargé.")

    generated_text = generator(request.prompt, max_length=400, num_return_sequences=1)[0]["generated_text"]

    history.insert(0, {"prompt": request.prompt, "response": generated_text})
    if len(history) > 10:
        history.pop()

    return {"generated_text": generated_text, "history": history}

@app.get("/history/")
def get_history():
    return {"history": history}
