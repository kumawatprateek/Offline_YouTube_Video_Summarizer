import os
from typing import List
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

from config import (
    SUMMARIZATION_MODEL_NAME,
    SUMMARIZATION_CHUNK_WORDS,
    SUMMARY_MAX_LENGTH,
    SUMMARY_MIN_LENGTH,
    SUMMARIES_DIR,
)
from utils import ensure_dir, read_file, write_file, split_text_into_word_chunks

def load_summarization_pipeline():
    print(f"[SUM] Loading summarization model: {SUMMARIZATION_MODEL_NAME}")
    tokenizer = AutoTokenizer.from_pretrained(SUMMARIZATION_MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(SUMMARIZATION_MODEL_NAME)
    summarizer = pipeline(
        "summarization",
        model=model,
        tokenizer=tokenizer,
        device_map="auto" if model.device.type == "cuda" else None,
    )
    return summarizer

# def summarize_long_text(
#     text: str,
#     summarizer,
#     max_length: int,
#     min_length: int,
# ) -> str:
#     chunks = split_text_into_word_chunks(text, SUMMARIZATION_CHUNK_WORDS)
#     print(f"[SUM] Transcript split into {len(chunks)} chunk(s)")
#
#     chunk_summaries: List[str] = []
#     for idx, chunk in enumerate(chunks, start=1):
#         print(f"[SUM] Summarizing chunk {idx}/{len(chunks)}...")
#         summary = summarizer(
#             chunk,
#             max_length=max_length,
#             min_length=min_length,
#             do_sample=False,
#         )[0]["summary_text"]
#         chunk_summaries.append(summary)
#
#     # If more than one chunk, summarize the summaries
#     if len(chunk_summaries) > 1:
#         print("[SUM] Summarizing combined chunk summaries...")
#         combined_text = " ".join(chunk_summaries)
#         final_summary = summarizer(
#             combined_text,
#             max_length=max_length,
#             min_length=min_length // 2,
#             do_sample=False,
#         )[0]["summary_text"]
#     else:
#         final_summary = chunk_summaries[0]
#
#     return final_summary

def summarize_long_text(
    text: str,
    summarizer,
    max_length: int,
    min_length: int,
) -> str:
    # remove junk whitespace
    text = text.strip()

    # 🔒 SAFETY CHECK
    if len(text.split()) < 40:
        return "Text is too short or not suitable for summarization."

    chunks = split_text_into_word_chunks(text, SUMMARIZATION_CHUNK_WORDS)
    print(f"[SUM] Transcript split into {len(chunks)} chunk(s)")

    summaries = []

    for i, chunk in enumerate(chunks, start=1):
        print(f"[SUM] Summarizing chunk {i}/{len(chunks)}...")

        result = summarizer(
            chunk,
            max_length=min(max_length, 120),
            min_length=30,
            do_sample=False,
            truncation=True,
        )

        summaries.append(result[0]["summary_text"])

    return " ".join(summaries)


def summarize_transcript(transcript_path: str, output_basename: str) -> str:
    ensure_dir(SUMMARIES_DIR)
    text = read_file(transcript_path)

    summarizer = load_summarization_pipeline()
    summary = summarize_long_text(
        text,
        summarizer,
        max_length=SUMMARY_MAX_LENGTH,
        min_length=SUMMARY_MIN_LENGTH,
    )

    summary_path = os.path.join(SUMMARIES_DIR, f"{output_basename}.summary.txt")
    write_file(summary_path, summary)
    return summary_path
