import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_DIR = os.path.join(BASE_DIR, "downloads")
TRANSCRIPTS_DIR = os.path.join(BASE_DIR, "transcripts")
SUMMARIES_DIR = os.path.join(BASE_DIR, "summaries")

# STT model: "tiny", "base", "small", "medium", "large-v2" etc.
WHISPER_MODEL_SIZE = "small"

# Summarization model - ensure it is downloaded beforehand (offline use)
SUMMARIZATION_MODEL_NAME = "facebook/bart-large-cnn"

# Approx max words per chunk for summarization pipeline
SUMMARIZATION_CHUNK_WORDS = 800
SUMMARY_MAX_LENGTH = 200
SUMMARY_MIN_LENGTH = 60
