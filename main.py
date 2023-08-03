from tkinter import *


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("生草机")
        self.root.geometry("400x600")
        self.root.resizable(0, 0)

        self.root.button_setting = Button(root, text="打开设置", font=("Microsoft YaHei", 11), command=self.OpenModal)
        self.root.button_setting.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        # self.root.mainloop()
    @staticmethod
    def OpenModal():
        moddal = SettingWindow(root)


class SettingWindow(Toplevel):

    def __init__(self, parent):
        Toplevel.__init__(self, parent)
        self.title('aaa')
        self.geometry("400x500")
        self.resizable(height=False, width=False)
        self.grab_set()


if __name__ == '__main__':
    root = Tk()
    MainWindow(root)
    root.mainloop()
