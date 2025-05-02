import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Викторина")

        self.questions = [
            {"question": "красики плвали...?", "options": ["В тазике", "В воде", "В лаве", "На земле"], "answer": "В тазике"},
            {"question": "?", "options": ["//", "#", "/*", "--"], "answer": "#"},
            {"question": "Какой метод используется для запуска главного цикла окна в Tkinter?", "options": ["main()", "run()", "start()", "mainloop()"], "answer": "mainloop()"},
        ]
        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(master, text="", wraplength=400)
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()
        self.options = []

        for i in range(4):
            option = tk.Radiobutton(master, text="", variable=self.var, value="", command=self.check_answer)
            option.pack(anchor='w')
            self.options.append(option)

        self.next_button = tk.Button(master, text="Следующий вопрос", command=self.next_question)
        self.next_button.pack(pady=20)

        self.show_question()

    def show_question(self):
        question_data = self.questions[self.current_question]
        self.question_label.config(text=question_data["question"])
        for i, option in enumerate(question_data["options"]):
            self.options[i].config(text=option, value=option)
        self.var.set(None)

    def check_answer(self):
        selected_answer = self.var.get()
        correct_answer = self.questions[self.current_question]["answer"]
        if selected_answer == correct_answer:
            self.score += 1

    def next_question(self):
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.show_question()
        else:
            self.end_quiz()

    def end_quiz(self):
        messagebox.showinfo("Результаты", f"Ваш результат: {self.score} из {len(self.questions)}")
        self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    quiz_app = QuizApp(root)
    root.mainloop()
