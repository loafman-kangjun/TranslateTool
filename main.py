import time
from tkinter import *
from tkinter.ttk import *
import util
import translates
import random


class MainWindow:
    def __init__(self, __root):
        self.root = __root
        self.root.title("生草机")
        self.root.geometry("600x400")
        self.root.resizable(0, 0)

        self.title_label = Label(__root, text="输入原始内容：", anchor="center", font=("Microsoft YaHei", 11))
        self.title_label.place(x=5, y=5, width=110, height=30)

        self.original_text = Text(__root)
        self.original_text.place(x=5, y=40, width=573, height=140)
        self.original_scroll = Scrollbar(__root)
        self.original_scroll.place(x=580, y=40, width=17, height=140)
        self.original_scroll.config(command=self.original_text.yview)
        self.original_text.config(yscrollcommand=self.original_scroll.set)

        self.times_label = Label(__root, text="翻译次数：", anchor="center", font=("Microsoft YaHei", 11))
        self.times_label.place(x=5, y=190, width=70, height=30)

        self.translate_times = Entry(__root)
        self.translate_times.place(x=79, y=190.5, width=55, height=30)

        self.translate_button = Button(__root, text="翻译", command=self.translate)
        self.translate_button.place(x=140, y=190.5, width=50, height=30)

        self.translate_progressbar = Progressbar(__root)
        self.translate_progressbar.place(x=199, y=196, width=394, height=21)
        # self.button_setting = Button(root, text="打开设置", font=("Microsoft YaHei", 11), command=self.OpenSetting)
        # self.button_setting.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

    @staticmethod
    def OpenSetting():
        _ = SettingWindow(root)

    def translate(self):
        __original = self.original_text.get("1.0", "end-1c")
        __times = self.translate_times.get()
        for i in range(100):
            self.translate_progressbar['value'] = i + 1
            root.update()
            time.sleep(0.05)
        __translation = translates.fanyi(__original)
        print(__translation + __times)


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
