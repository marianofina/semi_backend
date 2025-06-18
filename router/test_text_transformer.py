from fastapi import APIRouter
from services.TextTransformer import resumir

router = APIRouter()


@router.get("/summarize")
def summarize(text: str, mini: float, maxi: float):
    return resumir(text, min_length=mini, max_length=maxi, do_sample=False)
