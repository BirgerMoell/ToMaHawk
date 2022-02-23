from typing import Optional

from fastapi import FastAPI, File, UploadFile, Form
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://127.0.0.1:5500", "http://127.0.0.1:8000", "localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/save")
def save(file: UploadFile):
    audio_bytes = file.file.read()
    print(audio_bytes)

@app.post("/form")
async def form(AudioFile: str = Form(...)):
    print(AudioFile)
    # return {"username": username}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}