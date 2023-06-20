from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/text")
def process_text(text_input: TextInput):
    processed_text = text_input.text + " yes"
    return {"text": processed_text}
