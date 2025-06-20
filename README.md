# ASR Pipeline Project

## Overview
This project provides a complete pipeline for automatic speech recognition (ASR) with speaker diarization and alignment. It processes audio files, identifies speakers, transcribes speech using Whisper models, and aligns the results for speaker-labeled transcription.

## Prerequisites
- **Python 3.8+**
- **ffmpeg** (required by pydub; must be installed and available in PATH)
- **HuggingFace account & token** (for pyannote.audio diarization)
- **Whisper.cpp binary**
  - Build or download `whisper-cli.exe` and place it at `models/whisper.cpp/build/bin/Release/whisper-cli.exe`
  - Download the Whisper model (e.g., `ggml-base.en.bin`) and place it in `models/whisper_large-v3/`

## Installation
1. **Clone the repository**
2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Install ffmpeg**:
   - Windows: Download from https://ffmpeg.org/download.html and add to PATH
   - Linux/macOS: `sudo apt install ffmpeg` or `brew install ffmpeg`
4. **Set up HuggingFace token**:
   - Register at https://huggingface.co/
   - Get your token and update `src/diarization.py` if needed
5. **Build Whisper.cpp** (if not already built):
   - Follow instructions at https://github.com/ggerganov/whisper.cpp
   - Ensure `whisper-cli.exe` is at the path used in `src/asr_transcribe.py`

## requirements.txt
```
pydub
pyannote.audio
soundfile
```

## Usage
1. **Prepare your input audio**: Place your audio file (e.g., `input.mp3`) in the `audio/` directory.
2. **Run the main pipeline**:
   ```bash
   python src/main.py
   ```
3. **Output**:
   - Speaker-labeled transcription will be printed and saved to `outputs/transcription.txt`

## Pipeline Details
- **Audio Conversion**: Converts input audio to mono 16kHz WAV (`preprocess_audio.py`)
- **Speaker Diarization**: Identifies speaker segments using `pyannote.audio` (`diarization.py`)
- **Transcription**: Uses Whisper.cpp binary and model to transcribe audio (`asr_transcribe.py`)
- **Alignment**: Aligns diarization and transcription for speaker-labeled output (`align_results.py`)

## Notes
- Ensure all paths in the scripts match your local setup (especially the Whisper binary and model paths).
- The HuggingFace token in `diarization.py` should be kept secure. For production, use environment variables.
- Large models may require significant RAM and CPU resources.

## Credits
- [Whisper.cpp](https://github.com/ggerganov/whisper.cpp)
- [pyannote.audio](https://github.com/pyannote/pyannote-audio)
