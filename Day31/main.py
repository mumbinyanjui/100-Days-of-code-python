import random
from tkinter import *
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn={}
try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('data/german_words.csv')
    to_learn=original_data.to_dict(orient='records')
else:
    to_learn=data.to_dict(orient='records')

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)

    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title, text="German",fill="black")
    canvas.itemconfig(word,text=current_card['German'],fill="black")
    canvas.itemconfig(card_bg,image=front_image)
    flip_timer=window.after(3000, func=flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English",fill="white")
    canvas.itemconfig(word,text=current_card['English'],fill="white")
    canvas.itemconfig(card_bg, image=back_image)

def is_known():
    to_learn.remove(current_card)
    data=pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)

    next_card()



window = Tk()
window.title("Flash Card Card")
window.config(bg=BACKGROUND_COLOR, padx=20, pady=20)

flip_timer=window.after(3000,func=flip_card)

canvas=Canvas(height=526, width=800)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 260, image=front_image)
card_title=canvas.create_text(400,100,text="",font=("Arial",40,"italic"))
word=canvas.create_text(400,250,text="",font=("Arial",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

wrong_image= PhotoImage(file="images/wrong.png")
wrong_button=Button(image=wrong_image,highlightthickness=0,command=next_card)
wrong_button.grid(row=1, column=0)

right_image= PhotoImage(file="images/right.png")
right_button=Button(image=right_image,highlightthickness=0,command=is_known)
right_button.grid(row=1, column=1)



next_card()

window.mainloop()