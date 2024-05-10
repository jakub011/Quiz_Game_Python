from tkinter import *
from  quiz_brain import QuizBrain



THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)


        self.score_counter = Label(text="Score: 0" ,pady=20,padx=20,bg=THEME_COLOR,fg="white",font=("Arial",15))
        self.score_counter.grid(column=1,row=0)

        self.question_space = Canvas(width=300,height=250,bg="white")
        self.question_space.grid(column=0,row=1,columnspan=2,pady=20,padx=20)
        self.question = self.question_space.create_text(
            150,
            125,
            width=280,
            text=f"",
            font=("Arial",20,"italic"))



        self.true_icon = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=self.true_icon,command=self.its_true)
        self.true_button.grid(column=0,row=2, pady=20, padx=20)

        self.false_icon = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.false_icon,command=self.its_false)
        self.false_button.grid(column=1, row=2, pady=20, padx=20)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.true_button.config(state="normal")
        self.false_button.config(state="normal")
        self.question_space.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_counter.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.question_space.itemconfig(self.question, text=q_text)
        else:
            self.question_space.itemconfig(self.question, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def its_true(self):
        check = self.quiz.check_answer("True")
        self.give_feedback(check)
    def its_false(self):
        check = self.quiz.check_answer("False")
        self.give_feedback(check)
    def give_feedback(self, is_right):
        if is_right:
            self.question_space.config(bg="green")
        else:
            self.question_space.config(bg="red")

        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

        self.window.after(1000, self.get_next_question)



