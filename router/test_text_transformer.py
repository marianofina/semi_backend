from fastapi import APIRouter
from services.TextTransformer import resumir

router = APIRouter()


@router.get("/")
def auth():
    text = 'Hay chicos que dan lástima, cuenta Isabel, una vecina que todos los sábados alimenta a los chicos en el único comedor del barrio. El efecto visible de la pasta base en los más chicos, que van de los 9 a los 15 años, es el envejecimiento. La piel empieza a volvérseles gris, arrugada, y a los más grandes se les caen los dientes. A algunos, incluso, les han amputado las piernas o los brazos por infecciones que avanzaban mientras ellos permanecían hundidos en su letargo tóxico. Es por esto que a los transas allí los llaman "arruinaguachos", los que matan lentamente a los pibes adictos. Los niños de 4 años saben de qué se trata el circuito de consumo. Camila, una nena que participa del hogar de día de la Fundación Cadena, dice en su media lengua: «Mi hermana está con eso que comen los fisuritas; con la pasta base. Ella lleva y vende en el tren». Eso describe un informe elaborado por el Instituto de Investigación sobre Jóvenes, Violencia y Adicciones que habla del tren como elemento determinante en la venta de droga en Puerta de Hierro.'
    return resumir(text, max_length=130, min_length=30, do_sample=False)

