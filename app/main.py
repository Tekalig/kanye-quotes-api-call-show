from tkinter import *
from app.quote import get_quote

BG = "#065535"

window = Tk()
window.title("Wise Man Says...")
window.config(padx=50, pady=50, background=BG)
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="./assets/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Quote Goes HERE", width=250,
                                font=("Arial", 30, "bold"), fill="#133337")
canvas.grid(row=0, column=0)
canvas.config(background=BG, highlightthickness=0)

kanye_img = PhotoImage(file=",/assests/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)
kanye_button.config(background=BG, activebackground="#FFC0CB", borderwidth=0, cursor="hand2")

window.mainloop()
