import soundfile as sf
from asr_transcribe import transcribe_audio_whisper
from diarization import diarize_audio

def align_transcription(diarization, transcription, audio_path):
    audio_duration = sf.info(audio_path).duration
    lines = transcription.strip().splitlines()
    if len(lines) == 0:
        raise ValueError("Transcription file is empty. Cannot align results.")
    step = audio_duration / len(lines)

    output = []
    for start, end, speaker in diarization:
        start_idx = int(start // step)
        end_idx = int(end // step)
        speaker_text = ' '.join(lines[start_idx:end_idx+1])
        output.append(f"{speaker}: {speaker_text}")
    return output

if __name__ == "__main__":
    diarization = diarize_audio("audio/output.wav")
    transcription = transcribe_audio_whisper("audio/output.wav", "models/whisper_large-v3")
    final_output = align_transcription(diarization, transcription, "audio/output.wav")
    for line in final_output:
        print(line)