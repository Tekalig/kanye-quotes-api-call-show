import requests
from app.main import canvas, quote_text

def get_quote():
    response = requests.get("https://api.kanye.rest/")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote, font=("Arial", 16, "bold"))
