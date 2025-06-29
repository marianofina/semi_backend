from transformers import pipeline, AutoTokenizer

model_name = "facebook/bart-large-cnn"
device = -1  # CPU

summarizer = pipeline("summarization", model=model_name, device=device)
tokenizer = AutoTokenizer.from_pretrained(model_name)


def resumir(texto: str, nivel, resumen_final: bool = False) -> str:
    if not texto.strip():
        return ""

    max_tokens = 1024
    inputs = tokenizer(texto, truncation=False, return_tensors="pt")["input_ids"][0]
    chunks = [inputs[i:i + max_tokens] for i in range(0, len(inputs), max_tokens)]

    resúmenes = []

    for chunk in chunks:
        input_chunk = tokenizer.decode(chunk, skip_special_tokens=True)
        token_count = len(chunk)

        # Asegurarse que max_len y min_len no superen token_count y no sean menores a 1
        max_len = max(1, min(token_count, int(token_count * nivel)))
        min_len = max(1, min(max_len, int(max_len * 0.8)))

        # En caso que max_len < min_len (muy raro), ajustar min_len
        if min_len > max_len:
            min_len = max_len

        try:
            resumen = summarizer(
                input_chunk,
                min_length=min_len,
                max_length=max_len,
                do_sample=False
            )
            resúmenes.append(resumen[0]["summary_text"])
        except Exception as e:
            print(f"Error resumiendo chunk: {e}")
            continue

    resumen_total = " ".join(resúmenes)

    if resumen_final and len(resúmenes) > 1:
        total_tokens = len(tokenizer(resumen_total)["input_ids"])
        max_len = max(5, int(total_tokens * nivel))
        min_len = max(1, int(max_len * 0.8))
        try:
            resumen_final_result = summarizer(
                resumen_total,
                min_length=min_len,
                max_length=max_len,
                do_sample=False
            )
            return resumen_final_result[0]["summary_text"]
        except Exception as e:
            print(f"Error en resumen final: {e}")

    return resumen_total
