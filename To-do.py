from tkinter import *

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("600x310+300+150")

        # ======== UI Labels ========
        Label(self.root, text="To-Do-List-App", font="Arial 20 bold", width=20, bd=10, bg="pink", fg="black").pack(side=TOP, fill=BOTH)
        Label(self.root, text="Add Task", font="Arial 15 bold", bd=10, bg="green", fg="black").place(x=40, y=50)
        Label(self.root, text="Tasks", font="Arial 15 bold", bd=10, bg="green", fg="black").place(x=350, y=50)

        # ======== Widgets ========
        self.text = Text(self.root, bd=5, height=2, width=25, font="Arial 10 italic bold")
        self.text.place(x=40, y=100)

        self.task_listbox = Listbox(self.root, height=12, bd=5, width=28, font="Arial 15 italic bold")
        self.task_listbox.place(x=250, y=100)

        # ======== Buttons ========
        Button(self.root, text="Add", font="Sarif 15 bold italic", width=10, bd=5, bg="blue", fg="black", command=self.add_task).place(x=25, y=150)
        Button(self.root, text="Delete", font="Sarif 15 bold italic", width=10, bd=5, bg="blue", fg="black", command=self.delete_task).place(x=25, y=200)

        # ======== Load Existing Tasks ========
        try:
            with open("data.txt", "r") as file:
                tasks = file.readlines()
                for task in tasks:
                    self.task_listbox.insert(END, task.strip())
        except FileNotFoundError:
            open("data.txt", "w").close()

    # ======== Add Task ========
    def add_task(self):
        content = self.text.get(1.0, END).strip()
        if content:
            self.task_listbox.insert(END, content)
            with open("data.txt", "a") as file:
                file.write(content + "\n")
            self.text.delete(1.0, END)

    # ======== Delete Task ========
    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            task = self.task_listbox.get(selected)
            self.task_listbox.delete(selected)
            with open("data.txt", "r") as file:
                tasks = file.readlines()
            with open("data.txt", "w") as file:
                for line in tasks:
                    if line.strip() != task:
                        file.write(line)

def main():
    root = Tk()
    Todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()