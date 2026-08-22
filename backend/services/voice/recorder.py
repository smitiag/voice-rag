import sounddevice as sd
import soundfile as sf

SAMPLE_RATE = 16000
DURATION = 5


def record_audio(output_file: str = "recording.wav") -> str:
    """
    Records audio from microphone for 5 seconds.
    """

    print("🎙 Recording... Speak now!")

    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32",
    )

    sd.wait()

    sf.write(output_file, audio, SAMPLE_RATE)

    print(f"Saved: {output_file}")

    return output_file