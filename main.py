import tkinter as tk

def add_task():
  task = task_entry.get()
  if task:
     task_listBox.insert(tk.END, task)
     task_entry.delete(0, tk.END)

def delete_task():
    selected_task = task_listBox.curselection()
    if selected_task:
       task = task_listBox.get(selected_task)
       task_listBox_del.insert(tk.END, task)
       task_listBox.delete(selected_task)
def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task = task_listBox.get(selected_task)
        task_listBox_redy.insert(tk.END, task)
        task_listBox.delete(selected_task)

root = tk.Tk()

root.title("Task list")
root.configure(background="cornsilk2")

text1 = tk.Label(root, text="Введите вашу задачу:", bg="cornsilk2")
text1.pack(pady=3)

task_entry = tk.Entry(root, width=30, bg="DarkSlateGray3")
task_entry.pack(pady=10)

add_task_button = tk.Button(root, text="Добавить задачу", command=add_task)
add_task_button.pack(pady=3)

delete_button = tk.Button(root, text="Удалить задачу", command=delete_task)
delete_button.pack(pady=3)

mark_button = tk.Button(root, text="Отметить выполненную задачу", command=mark_task)
mark_button.pack(pady=3)

text2 = tk.Label(root, text="Список задач:", bg="cornsilk2")
text2.pack(pady=3)

task_listBox = tk.Listbox(root, height=7, width=50, bg="DarkSeaGreen1")
task_listBox.pack(pady=10)

text3 = tk.Label(root, text="Удаленные задачи:", bg="cornsilk2")
text3.pack(pady=3)

task_listBox_del = tk.Listbox(root, height=7, width=50, bg="coral2")
task_listBox_del.pack(pady=10)

text4 = tk.Label(root, text="Выполненные задачи:", bg="cornsilk2")
text4.pack(pady=3)

task_listBox_redy = tk.Listbox(root, height=7, width=50, bg="dark green")
task_listBox_redy.pack(pady=10)

root.mainloop()