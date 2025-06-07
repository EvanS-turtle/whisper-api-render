FROM python:3.11-slim
RUN apt-get update && apt-get install -y ffmpeg
RUN pip install fastapi uvicorn openai-whisper torch
COPY app.py .
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9000"]
