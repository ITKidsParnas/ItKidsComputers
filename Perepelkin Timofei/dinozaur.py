import tkinter as tk
from tkinter import scrolledtext

class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat GPT")

        self.chat_area = scrolledtext.ScrolledText(root, state='disabled', wrap=tk.WORD, width=50, height=20, bg="lightgrey")
        self.chat_area.pack(padx=10, pady=10)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack(padx=10, pady=10)
        self.entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(pady=5)

    def send_message(self, event=None):
        user_message = self.entry.get()
        if user_message.strip():
            self.display_message("You: " + user_message)
            self.entry.delete(0, tk.END)
            self.bot_response(user_message)

    def display_message(self, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, message + '\n')
        self.chat_area.config(state='disabled')
        self.chat_area.see(tk.END)

    def bot_response(self, message):
        # Здесь можно добавить логику для более сложных ответов
        response = "Bot: " + self.generate_response(message)
        self.display_message(response)

    def generate_response(self, message):
        # Простейшая логика ответов для демонстрации
        if "hello" in message.lower():
            return "Hello! How can I help you today?"
        elif "how are you" in message.lower():
            return "I'm just a program, but thanks for asking!"
        elif "bye" in message.lower():
            return "Goodbye! Have a great day!"
        else:
            return "I'm sorry, I don't understand that."

if __name__ == "__main__":
    root = tk.Tk()
    chat_bot = ChatBot(root)
    root.mainloop()
