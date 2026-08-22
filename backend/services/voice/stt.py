import os
import whisper

model = whisper.load_model("base")


def transcribe(audio_path: str) -> str:
    if not os.path.exists(audio_path):
        return ""

    try:
        result = model.transcribe(audio_path)
        return result["text"].strip()
    except Exception:
        return ""