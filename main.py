from tkinter import *


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("生草机")
        self.root.geometry("400x600")
        self.root.resizable(0, 0)

        # self.label_input = tk.Label(root, text="请输入要生草的内容：", font=("Microsoft YaHei", 11))
        # self.label_input.grid(row=0, column=0, padx=5, pady=5)
        self.root.button_setting = Button(root, text="打开设置", font=("Microsoft YaHei", 11), command=self.onModal)
        self.root.button_setting.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        # self.root.mainloop()
    def onModal(self):
        moddal = Modal(root)


class Modal(Toplevel):

    def __init__(self, parent):
        Toplevel.__init__(self, parent)
        self.title('aaa')
        self.geometry("400x500")
        self.resizable(height=False, width=False)
        self.grab_set()


if __name__ == '__main__':
    root = Tk()
    # app = Main()
    MainWindow(root)
    root.mainloop()
