from fastapi import FastAPI, File, UploadFile
import subprocess

app = FastAPI()

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    with open("audio.mp3", "wb") as f:
        f.write(await file.read())
    
    result = subprocess.run(
        ["whisper", "audio.mp3", "--model", "tiny.en", "--output_format", "json"],
        capture_output=True, text=True
    )
    return {"transcription": result.stdout}
