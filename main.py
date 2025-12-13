import os
import argparse
import sys
from urllib.parse import urlparse
# from downloader.py import download_audio_from_youtube
# from stt import transcribe_audio
# from summarizer import summarize_transcript
from downloader import download_audio_from_youtube
from stt import transcribe_audio
from summarizer import summarize_transcript

def validate_youtube_url(url: str) -> bool:
    parsed = urlparse(url)
    return "youtube.com" in parsed.netloc or "youtu.be" in parsed.netloc

def main():
    parser = argparse.ArgumentParser(
        description="Offline YouTube Video Summarizer (Audio -> STT -> Summary)"
    )
    parser.add_argument(
        "--url",
        type=str,
        required=True,
        help="Public YouTube video URL",
    )
    parser.add_argument(
        "--print-summary",
        action="store_true",
        help="Print the final summary to stdout",
    )

    args = parser.parse_args()
    url = args.url

    if not validate_youtube_url(url):
        print("[ERROR] The provided URL does not look like a YouTube URL.")
        sys.exit(1)

    try:
        # 1. Download audio
        audio_path, title = download_audio_from_youtube(url)
        print(f"[MAIN] Downloaded audio for: {title}")
        base_name = os.path.splitext(os.path.basename(audio_path))[0]

        # 2. Transcribe
        transcript_path, duration = transcribe_audio(audio_path, output_basename=base_name)
        print(f"[MAIN] Transcription saved to: {transcript_path} (duration ~{duration:.1f}s)")

        # 3. Summarize
        summary_path = summarize_transcript(transcript_path, output_basename=base_name)
        print(f"[MAIN] Summary saved to: {summary_path}")

        if args.print_summary:
            print("\n=== FINAL SUMMARY ===\n")
            with open(summary_path, "r", encoding="utf-8") as f:
                print(f.read())

    except Exception as e:
        print(f"[ERROR] {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
