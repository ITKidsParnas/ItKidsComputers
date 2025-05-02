import tkinter as tk
from tkinter import messagebox

class TodoList:
    def __init__(self, master):
        self.master = master
        master.title("Список дел")

        self.tasks = []  # Список задач
        self.completed_tasks = [] #Список завершенных задач

        # --- Элементы интерфейса ---

        # Поле ввода для новой задачи
        self.entry_task = tk.Entry(master, width=50)
        self.entry_task.pack(pady=5)

        # Кнопка добавления задачи
        self.button_add_task = tk.Button(master, text="Добавить задачу", width=48, command=self.add_task)
        self.button_add_task.pack(pady=2)

        # Список задач (ListBox)
        self.listbox_tasks = tk.Listbox(master, width=50, height=10)
        self.listbox_tasks.pack(pady=5)

        # Кнопка удаления задачи
        self.button_delete_task = tk.Button(master, text="Удалить задачу", width=48, command=self.delete_task)
        self.button_delete_task.pack(pady=2)

        # Кнопка завершения задачи
        self.button_complete_task = tk.Button(master, text="Отметить задачу как выполненную", width=48, command=self.complete_task)
        self.button_complete_task.pack(pady=2)

        # Кнопка просмотра выполненных задач
        self.button_view_completed = tk.Button(master, text="Посмотреть выполненные задачи", width=48, command=self.view_completed_tasks)
        self.button_view_completed.pack(pady=2)

        # --- Методы ---

    def add_task(self):
        """Добавляет задачу в список."""
        task = self.entry_task.get()
        if task != "":
            self.tasks.append(task)
            self.update_listbox()
            self.entry_task.delete(0, tk.END)  # Очистка поля ввода
        else:
            messagebox.showwarning("Предупреждение", "Пожалуйста, введите задачу.")

    def delete_task(self):
        """Удаляет выбранную задачу из списка."""
        try:
            task_index = self.listbox_tasks.curselection()[0]
            task = self.tasks[task_index] #Получаем удаляемую задачу, чтобы добавить в completed tasks в случае необходимости.
            self.tasks.pop(task_index) #Удаляем задачу из списка
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Предупреждение", "Пожалуйста, выберите задачу для удаления.")

    def complete_task(self):
        """Отмечает задачу как выполненную (перемещает в отдельный список)."""
        try:
            task_index = self.listbox_tasks.curselection()[0]
            task = self.tasks.pop(task_index)
            self.completed_tasks.append(task)
            self.update_listbox()
            messagebox.showinfo("Задача выполнена", f"Задача '{task}' отмечена как выполненная!") # Добавляем сообщение об успехе
        except IndexError:
            messagebox.showwarning("Предупреждение", "Пожалуйста, выберите задачу для завершения.")


    def view_completed_tasks(self):
        """Отображает окно со списком выполненных задач."""
        if not self.completed_tasks:
            messagebox.showinfo("Выполненные задачи", "Нет выполненных задач.")
            return

        completed_window = tk.Toplevel(self.master)
        completed_window.title("Выполненные задачи")

        listbox_completed = tk.Listbox(completed_window, width=50, height=10)
        for task in self.completed_tasks:
            listbox_completed.insert(tk.END, task)
        listbox_completed.pack(pady=5)

    def update_listbox(self):
        """Обновляет отображение списка задач."""
        self.listbox_tasks.delete(0, tk.END)  # Очистка списка
        for task in self.tasks:
            self.listbox_tasks.insert(tk.END, task)

# --- Запуск приложения ---
if __name__ == "__main__":
    root = tk.Tk()
    todo_list = TodoList(root)
    root.mainloop()