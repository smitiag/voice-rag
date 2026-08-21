import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()

client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY")
)


def speech_to_text(audio_path: str):
    """
    Convert audio file to text using ElevenLabs STT.
    Returns transcript string.
    """
    with open(audio_path, "rb") as audio:
        result = client.speech_to_text.convert(
            file=audio,
            model_id="scribe_v1"
        )

    return result.text