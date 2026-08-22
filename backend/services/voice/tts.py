import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import save

load_dotenv()

client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY")
)


def text_to_speech(text: str, output_file: str = "response.mp3") -> str:
    try:
        audio = client.text_to_speech.convert(
            voice_id="YOUR_VOICE_ID",
            model_id="eleven_multilingual_v2",
            text=text,
        )

        with open(output_file, "wb") as f:
            for chunk in audio:
                f.write(chunk)

        return output_file

    except Exception:
        return None