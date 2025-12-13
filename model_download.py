# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
# from faster_whisper import WhisperModel
#
# # Download summarization model
# AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
# AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")
#
# # Download Whisper model weights via faster-whisper
# model = WhisperModel("small")
# print("Done")


from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "csebuetnlp/mT5_multilingual_XLSum"

AutoTokenizer.from_pretrained(model_name)
AutoModelForSeq2SeqLM.from_pretrained(model_name)

print("Multilingual summarization model downloaded")
