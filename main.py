from tkinter import *
import util


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("生草机")
        self.root.geometry("600x400")
        self.root.resizable(0, 0)

        self.title_label = Label(root,text="输入原始内容：",anchor="center", font=("Microsoft YaHei", 11))
        self.title_label.place(x=5, y=5, width=110, height=30)

        self.original_text = Text(root)
        self.original_text.place(x=5, y=40, width=573, height=140)
        self.original_scroll = Scrollbar(root)
        self.original_scroll.place(x=580, y=40, width=17, height=140)

        # 两个控件关联
        self.original_scroll.config(command=self.original_text.yview)
        self.original_text.config(yscrollcommand=self.original_scroll.set)
        # self.button_sestting = Button(root, text="打开设置", font=("Microsoft YaHei", 11), command=self.OpenSetting)
        # self.button_sestting.grid(row=7, column=0, columnspan=2, padx=5, pady=5)
        #
        # self.button_setting = Button(root, text="打开设置", font=("Microsoft YaHei", 11), command=self.OpenSetting)
        # self.button_setting.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

    @staticmethod
    def OpenSetting():
        _ = SettingWindow(root)


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
    util.file.init('./setting.json')
    root = Tk()
    MainWindow(root)
    root.mainloop()
