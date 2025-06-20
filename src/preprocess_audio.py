from pydub import AudioSegment
import os

def convert_to_wav(input_path, output_path):
    audio = AudioSegment.from_file(input_path)
    audio = audio.set_channels(1).set_frame_rate(16000)
    audio.export(output_path, format="wav")

if __name__ == "__main__":
    convert_to_wav("audio/input.mp3", "audio/output.wav")