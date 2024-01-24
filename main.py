from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data=pd.read_csv("data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict=data.to_dict(orient="records")


random_card={}
# -----------------------------------------CODE---------------------------------------------------------
def new_word():
    global random_card, flip_timer
    window.after_cancel(flip_timer)
    random_card=random.choice(data_dict)
    canvas.itemconfig(canvas_title,text="French",fill='black' )
    canvas.itemconfig(canvas_word, text=random_card["French"],fill='black')
    canvas.itemconfig(canvas_image, image=canvas_front_image)
    flip_timer=window.after(3000, func=flip_card)
    data_dict.remove(random_card)
    data=pd.DataFrame(data_dict)
    data.to_csv("words_to_learn.csv",index=False)
    print(len(data_dict))

def no_remove():
    global random_card, flip_timer
    print(len(data_dict))
    window.after_cancel(flip_timer)
    random_card = random.choice(data_dict)
    canvas.itemconfig(canvas_title, text="French", fill='black')
    canvas.itemconfig(canvas_word, text=random_card["French"], fill='black')
    canvas.itemconfig(canvas_image, image=canvas_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=canvas_back)
    canvas.itemconfig(canvas_title,text="English",fill='white')
    canvas.itemconfig(canvas_word,text=random_card["English"],fill='white')


# --------------------------------------------------------------------------------UI------------------------------
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer=window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_front_image = PhotoImage(file="images/card_front.png")
canvas_back=PhotoImage(file="images/card_back.png")
canvas_image=canvas.create_image(400, 263, image=canvas_front_image)
canvas_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_button = Button()
wrongImage = PhotoImage(file="images/wrong.png")
wrong_button.config(image=wrongImage, highlightthickness=0, bg=BACKGROUND_COLOR,command=no_remove)
wrong_button.grid(row=1, column=0)

right = Button()
right_image = PhotoImage(file="images/right.png")
right.config(image=right_image, highlightthickness=0,command=new_word)
right.grid(row=1, column=1)

no_remove()


window.mainloop()
