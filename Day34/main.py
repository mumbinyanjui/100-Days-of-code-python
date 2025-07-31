from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR,padx=20,pady=20)

        self.label = Label(text="Score: 0", fg="white",bg=THEME_COLOR)
        self.label.grid(column=1, row=0)

        self.canvas = Canvas(height=250,width=300,bg="white")
        self.Question_text = self.canvas.create_text(150,125,text="Moe",font=("Arial",20,"italic"),fill=THEME_COLOR,width=280)
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)

        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image,command=self.is_true)
        self.true_button.grid(row=2,column=0)

        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image,command=self.not_true)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.Question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.Question_text,text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def is_true(self):
        self.give_fedback(self.quiz.check_answer("True"))

    def not_true(self):
        self.give_fedback(self.quiz.check_answer("False"))

    def give_fedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,self.get_next_question)

