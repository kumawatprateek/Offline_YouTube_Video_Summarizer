# 🎥 Offline YouTube Video Summarizer (Multilingual)

An **end-to-end offline YouTube video summarizer** built with Python.
It downloads audio from YouTube, transcribes speech using **Whisper (offline)**, and generates summaries using a **multilingual transformer model**, all running **locally without cloud APIs**.

---

## 🚀 Features

* 🔹 Download audio from any public YouTube video
* 🔹 Offline speech-to-text using **faster-whisper**
* 🔹 Multilingual transcription (Hindi, English, Hinglish, etc.)
* 🔹 Offline text summarization using **mT5 multilingual model**
* 🔹 CPU-friendly (no GPU required)
* 🔹 Command-line interface
* 🔹 Saves transcript and summary as files

---

## 🧠 Tech Stack

* **Python 3.10+**
* **yt-dlp** – YouTube audio downloader
* **FFmpeg** – audio processing
* **faster-whisper** – offline speech-to-text
* **Hugging Face Transformers**
* **mT5_multilingual_XLSum** – multilingual summarization model

---

## 📂 Project Structure

```text
Offline_youtube_summarizer/
│
├── main.py               # Entry point (CLI)
├── downloader.py         # YouTube audio downloader
├── stt.py                # Speech-to-text (Whisper)
├── summarizer.py         # Text summarization
├── config.py             # Configuration
├── utils.py              # Helper functions
├── model_download.py     # One-time model download
├── requirements.txt
│
├── downloads/             # Audio files
├── transcripts/           # Transcribed text
├── summaries/             # Generated summaries
└── .venv/
```

---

## ⚙️ Setup Instructions (Windows)

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd Offline_youtube_summarizer
```

---

### 2️⃣ Create & activate virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

### 3️⃣ Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### 4️⃣ Install FFmpeg (Required)

1. Download from:
   👉 [https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip)
2. Extract to:

   ```
   C:\Program Files\ffmpeg-8.0.1-essentials_build\
   ```
3. Add this to **PATH**:

   ```
   C:\Program Files\ffmpeg-8.0.1-essentials_build\bin
   ```
4. Verify:

   ```cmd
   ffmpeg -version
   ```

---

### 5️⃣ Download models (One-time)

```bash
python model_download.py
```

This downloads:

* Whisper model
* Multilingual summarization model

After this step, the project runs **fully offline**.

---

## ▶️ Usage

Run the summarizer:

```bash
python main.py --url "https://youtu.be/VIDEO_ID" --print-summary
```

---

## 📄 Output Files

| File                      | Description        |
| ------------------------- | ------------------ |
| `downloads/*.webm`        | Downloaded audio   |
| `transcripts/*.txt`       | Transcribed speech |
| `summaries/*.summary.txt` | Generated summary  |

---

## 🌍 Multilingual Support

The project supports:

* Hindi
* English
* Hinglish
* Other languages supported by Whisper + mT5

⚠️ **Note:**
Songs or highly repetitive lyrics are **not ideal for summarization**.
The system works best for:

* Talks
* Lectures
* Podcasts
* Interviews
* Educational videos

---

## 🛠️ Configuration

Edit `config.py` to change:

* Whisper model size (`tiny`, `small`, `medium`)
* Summarization chunk size
* Output length

---

## ❗ Known Limitations

* Songs and music videos may produce poor summaries
* Long videos may take time on CPU
* Requires FFmpeg installed on system

---

## 📌 Future Improvements

* 🔹 FastAPI / Flask API
* 🔹 Streamlit web UI
* 🔹 Translation before summarization
* 🔹 Keyword extraction
* 🔹 PDF / DOCX export
* 🔹 Speaker diarization

---

## 👤 Author

**Prateek Kumawat**
AI / ML Engineer | Python Developer

📍 India

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!

---