from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import pickle
import re
from pathlib import Path
from deep_translator import GoogleTranslator

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

model_path = Path("static/trained_pipeline-0.5.0.pkl").resolve()

with open(model_path, "rb") as f:
    model = pickle.load(f)

classes = [
    'Arabic', 'Danish', 'Dutch', 'English', 'French', 'German',
    'Greek', 'Gujarati', 'Hebrew', 'Hindi', 'Hinglish', 'Italian',
    'Kannada', 'Malayalam', 'Portugeese', 'Russian', 'Spanish',
    'Swedish', 'Tamil', 'Turkish'
]


class TextIn(BaseModel):
    text: str


class TranslationIn(BaseModel):
    text: str
    language: str


class PredictionOut(BaseModel):
    language: str
    translated_text: str


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict", response_model=PredictionOut)
async def predict(request: Request, payload: TextIn):
    try:
        print(payload.dict())  # Print the received payload
        language, translated_text = predict_pipeline(payload.text)
        return PredictionOut(language=language, translated_text=translated_text)

    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))


@app.post("/translate", response_model=PredictionOut)
async def translate(request: Request, payload: TranslationIn):
    try:
        print(payload.dict())  # Print the received payload
        translated_text = GoogleTranslator(source='en', target=payload.language).translate(payload.text)
        return PredictionOut(language=payload.language, translated_text=translated_text)

    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))


def predict_pipeline(text):
    text = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', " ", text)
    text = re.sub(r'[[]]', ' ', text)
    text = text.lower()

    translated_text = GoogleTranslator(source='auto', target='en').translate(text)
    pred = model.predict([text])
    return classes[pred[0]], translated_text


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

