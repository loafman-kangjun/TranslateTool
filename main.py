from tkinter import *


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("生草机")
        self.root.geometry("400x600")
        self.root.resizable(0, 0)

        self.button_setting = Button(root, text="打开设置", font=("Microsoft YaHei", 11), command=self.OpenSetting)
        self.button_setting.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

    @staticmethod
    def OpenSetting():
        moddal = SettingWindow(root)


class SettingWindow(Toplevel):

    def __init__(self, parent):
        Toplevel.__init__(self, parent)
        self.title('aaa')
        self.geometry("400x500")
        self.resizable(height=False, width=False)
        self.grab_set()

        self.label = Label(self, text="这是设置窗口", font=("Microsoft YaHei", 11))
        self.label.pack(pady=20)

        self.button_ok = Button(self, text="确定", font=("Microsoft YaHei", 11))
        self.button_ok.pack(pady=10)


if __name__ == '__main__':
    root = Tk()
    MainWindow(root)
    root.mainloop()
