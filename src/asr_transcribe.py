import subprocess
import os

def transcribe_audio_whisper(audio_path, model_path):
    exe_path = "D:/wavenet/ASR/models/whisper.cpp/build/bin/Release/whisper-cli.exe"
    command = f"{exe_path} -m {model_path}/ggml-base.en.bin -f {audio_path} -otxt -of outputs/result"
    subprocess.run(command, shell=True)
    if not os.path.exists("outputs/result.txt"):
        print("outputs/result.txt does not exist!")
    with open("outputs/result.txt", "r") as file:
        text = file.read()
    return text

if __name__ == "__main__":
    text = transcribe_audio_whisper("audio/output.wav", "models/whisper_large-v3")
    print(text)
