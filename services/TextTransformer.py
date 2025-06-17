from transformers import pipeline

summarizer = pipeline("summarization")


def resumir(text, max_length, min_length, do_sample):
    resumen = summarizer(text, max_length=max_length, min_length=min_length, do_sample=do_sample)
    return resumen[0]['summary_text']
