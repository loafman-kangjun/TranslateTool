# import tkinter as tk
#
#
# class MainWindow:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("生草机")
#         self.root.geometry("400x600")
#         self.root.resizable(0,0)
#
#         self.label_input = tk.Label(root, text="请输入要生草的内容：", font=("Microsoft YaHei", 11))
#         self.label_input.grid(row=0, column=0, padx=5, pady=5)
#
#         self.root.mainloop()
from tkinter import *


class Modal(Toplevel):

    def __init__(self, parent, title=None):
        Toplevel.__init__(self, parent, width=200, height=300)
        self.geometry("100x80+%d+%d" % (parent.winfo_rootx() + 30,
                                        parent.winfo_rooty() + 30))
        self.title(title)
        self.resizable(height=False, width=False)
        self.grab_set()
        self.initUI()

    def initUI(self):
        self.frame = Frame(self)
        self.frame.pack(fill=X, expand=True)

        lbl = Label(self.frame, text="这是模态窗口", width=10)
        lbl.pack(fill=X, padx=5, expand=True)
