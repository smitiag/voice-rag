import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import save

load_dotenv()

client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY")
)


def text_to_speech(
    text: str,
    output_file: str = "response.mp3"
) -> str:
    """
    Convert text into speech using ElevenLabs.
    """

    audio = client.text_to_speech.convert(
        voice_id="JBFqnCBsd6RMkjVDRZzb",
        model_id="eleven_multilingual_v2",
        text=text,
    )

    save(audio, output_file)

    return output_file