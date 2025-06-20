import os
from pyannote.audio import Pipeline

# hf_token = os.getenv("HF_TOKEN")
pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization@2.1",
    use_auth_token="YOUR_ACCESS_TOKEN"
)

def diarize_audio(audio_path):
    diarization = pipeline(audio_path)
    segments = []
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        segments.append((turn.start, turn.end, speaker))
    return segments

if __name__ == "__main__":
    result = diarize_audio("audio/output.wav")
    print(result)