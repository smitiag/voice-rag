from recorder import record_audio
from stt import speech_to_text
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

def capture_transcript(duration=5):
    record_audio(duration=duration)

    audio_path = ROOT / "data" / "sample.wav"

    transcript = speech_to_text(str(audio_path))

    return transcript