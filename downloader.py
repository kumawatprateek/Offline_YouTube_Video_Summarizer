# import os
# from typing import Tuple
# from yt_dlp import YoutubeDL
# from config import DOWNLOAD_DIR
# from utils import ensure_dir
#
# def download_audio_from_youtube(url: str) -> Tuple[str, str]:
#     """
#     Downloads audio from YouTube as mp3.
#     Returns: audio_path, video_title
#     """
#     ensure_dir(DOWNLOAD_DIR)
#
#     ydl_opts = {
#         "format": "bestaudio/best",
#         "outtmpl": os.path.join(DOWNLOAD_DIR, "%(id)s.%(ext)s"),
#         "noplaylist": True,
#         "quiet": False,
#         "postprocessors": [
#             {
#                 "key": "FFmpegExtractAudio",
#                 "preferredcodec": "mp3",
#                 "preferredquality": "192",
#             }
#         ],
#     }
#
#     with YoutubeDL(ydl_opts) as ydl:
#         info = ydl.extract_info(url, download=True)
#         video_id = info.get("id")
#         title = info.get("title", "untitled")
#         audio_path = os.path.join(DOWNLOAD_DIR, f"{video_id}.mp3")
#
#     return audio_path, title

import os
from typing import Tuple
from yt_dlp import YoutubeDL
from config import DOWNLOAD_DIR
from utils import ensure_dir

# <-- set this to the exact bin folder you showed earlier:
FFMPEG_BIN = r"C:\Program Files\ffmpeg-8.0.1-essentials_build\bin"

def download_audio_from_youtube(url: str) -> Tuple[str, str]:
    """
    Downloads best audio and uses ffmpeg at FFMPEG_BIN for postprocessing.
    """
    ensure_dir(DOWNLOAD_DIR)

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(DOWNLOAD_DIR, "%(id)s.%(ext)s"),
        "noplaylist": True,
        "quiet": False,
        # Postprocessor to extract audio to mp3
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        # <-- important: explicitly point to ffmpeg/ffprobe location
        "ffmpeg_location": FFMPEG_BIN,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        video_id = info.get("id")
        title = info.get("title", "untitled")
        ext = info.get("ext", "webm")
        audio_path = os.path.join(DOWNLOAD_DIR, f"{video_id}.mp3") if any(
            p.get("key") == "FFmpegExtractAudio" for p in ydl_opts["postprocessors"]
        ) else os.path.join(DOWNLOAD_DIR, f"{video_id}.{ext}")

    return audio_path, title

