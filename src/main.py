from preprocess_audio import convert_to_wav
from diarization import diarize_audio
from asr_transcribe import transcribe_audio_whisper
from align_results import align_transcription

if __name__ == "__main__":
    input_audio = "audio/input.mp3"
    wav_audio = "audio/output.wav"

    print("\n[+] Converting to WAV...")
    convert_to_wav(input_audio, wav_audio)

    print("\n[+] Performing Diarization...")
    diarization = diarize_audio(wav_audio)

    print("\n[+] Transcribing Audio...")
    transcription = transcribe_audio_whisper(wav_audio, "models/whisper_large-v3")

    print("\n[+] Aligning Results...")
    final_output = align_transcription(diarization, transcription, wav_audio)

    print("\n[+] Final Speaker-Labeled Transcription:\n")
    for line in final_output:
        print(line)

    with open("outputs/transcription.txt", "w") as f:
        for line in final_output:
            f.write(line + "\n")

    print("\n[+] Transcription saved to outputs/transcription.txt")
