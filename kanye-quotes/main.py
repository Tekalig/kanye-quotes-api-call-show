from tkinter import *
import requests

BG = "#065535"


def get_quote():
    response = requests.get("https://api.kanye.rest/")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote, font=("Arial", 16, "bold"))


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50, background=BG)
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250,
                                font=("Arial", 30, "bold"), fill="#133337")
canvas.grid(row=0, column=0)
canvas.config(background=BG, highlightthickness=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)
kanye_button.config(background=BG, activebackground="#FFC0CB", borderwidth=0, cursor="hand2")

window.mainloop()
