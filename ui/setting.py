import tkinter as tk


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("生草机")
        self.root.geometry("400x600")
        self.root.resizable(0,0)

        self.label_input = tk.Label(root, text="请输入要生草的内容：", font=("Microsoft YaHei", 11))
        self.label_input.grid(row=0, column=0, padx=5, pady=5)

        self.root.mainloop()
