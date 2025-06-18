from transformers import pipeline
import torch

device = 0 if torch.cuda.is_available() else -1

summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=device)


def resumir(text, nivel: float) -> str:
    print("nivel:          ", nivel)
    """
    if nivel not in [0.2, 0.5, 0.8]:
        raise ValueError("Nivel inválido. Debe ser uno de: 0.2, 0.5, 0.8")
"""
    palabras = len(text.split())
    tokens_estimados = int(palabras * 1.3)
    max_len = max(20, int(tokens_estimados * nivel))  # evita max_length < 0
    min_len = int(max_len * 0.8)
    resumen = summarizer(
        text,
        min_length=min_len,
        max_length=max_len,
        do_sample=False
    )
    return resumen[0]['summary_text']
