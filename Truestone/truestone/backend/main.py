from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .preprocess import mask_entities
from .inference import analyze

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Payload(BaseModel):
    text: str

@app.post("/analyze")
def analyze_text(payload: Payload):
    masked = mask_entities(payload.text)
    result = analyze(masked)
    return result