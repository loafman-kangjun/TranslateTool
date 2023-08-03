# import tkinter as tk
# import ui
# import util
#
# root = tk.Tk()
#
#
# def main_window():
#     ui.main.MainWindow(root)
#
#
# if __name__ == "__main__":
#     util.file.setting('./setting.json')
#     main_window()
#     root.mainloop()

# import tkinter as tk
# import ui
# import util
#
#
# class MainWindow:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("生草机")
#         self.root.geometry("400x600")
#         self.root.resizable(0, 0)
#
#         # 添加一个按钮，点击后打开设置窗口并设为模态对话框
#         self.button_setting = tk.Button(root, text="打开设置", font=("Microsoft YaHei", 11), command=self.open_setting)
#         self.button_setting.grid(row=7, column=0, columnspan=2, padx=5, pady=5)
#
#     def open_setting(self):
#         setting_window = tk.Toplevel(self.root)
#         setting_window.title("设置窗口")
#         setting_window.geometry("300x200")
#         setting_window.transient(self.root)
#
#         setting_window.grab_set()  # 设为模态对话框，阻塞主窗口
#         self.root.wait_window(setting_window)  # 等待设置窗口关闭
#
#
# if __name__ == "__main__":
#     base = tk.Tk()
#     # util.file.setting('./setting.json')
#     main_window = MainWindow(base)
#     base.mainloop()
#

from tkinter import Tk, Frame, Menu, Toplevel, X, Button
from tkinter.ttk import Label


class Example(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Multi windows")

        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        self.master.button_setting = Button(root, text="打开设置", font=("Microsoft YaHei", 11), command=self.onModal)
        self.master.button_setting.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        fileMenu = Menu(menubar, tearoff=0)
        fileMenu.add_command(label="Modal", command=self.onModal)
        menubar.add_cascade(label="File", menu=fileMenu)

    def onModal(self):
        moddal = Modal(root, title="Modal")



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


if __name__ == '__main__':
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example()
    root.mainloop()
