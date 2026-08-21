import sounddevice as sd
import soundfile as sf
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "data" / "sample.wav"


def record_audio(duration=5, samplerate=16000):
    print("🎙️ Recording started... Speak now!")

    audio = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype="int16"
    )
    sd.wait()

    sf.write(str(OUTPUT), audio, samplerate)
    print(f"✅ Audio saved at: {OUTPUT}")