import os
from typing import Tuple
import torch
from faster_whisper import WhisperModel

from config import WHISPER_MODEL_SIZE, TRANSCRIPTS_DIR
from utils import ensure_dir, write_file

def get_device_and_compute_type():
    if torch.cuda.is_available():
        return "cuda", "float16"
    else:
        # CPU-friendly mode
        return "cpu", "int8"

def transcribe_audio(audio_path: str, output_basename: str) -> Tuple[str, float]:
    """
    Transcribes an audio file using a local Whisper model via faster-whisper.
    Returns: transcript_path, transcription_duration_sec
    """
    ensure_dir(TRANSCRIPTS_DIR)
    device, compute_type = get_device_and_compute_type()

    print(f"[STT] Loading Whisper model '{WHISPER_MODEL_SIZE}' on {device} ({compute_type})...")
    model = WhisperModel(WHISPER_MODEL_SIZE, device=device, compute_type=compute_type)

    print(f"[STT] Transcribing audio: {audio_path}")
    segments, info = model.transcribe(audio_path, beam_size=5)

    all_text = []
    for seg in segments:
        all_text.append(seg.text.strip())

    transcript_text = "\n".join(all_text)
    transcript_path = os.path.join(TRANSCRIPTS_DIR, f"{output_basename}.txt")
    write_file(transcript_path, transcript_text)

    return transcript_path, info.duration
