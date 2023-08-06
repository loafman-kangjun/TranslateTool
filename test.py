import time
import tkinter
import tkinter.ttk

def show():
    for i in range(100):
        # 每次更新加1
        progressbarOne['value'] = i + 1
        # 更新画面
        root.update()
        time.sleep(0.05)

root = tkinter.Tk()
root.geometry('150x120')

progressbarOne = tkinter.ttk.Progressbar(root)
progressbarOne.pack(pady=20)
# 进度值最大值
progressbarOne['maximum'] = 100
# 进度值初始值
progressbarOne['value'] = 0

button = tkinter.Button(root, text='Running', command=show)
button.pack(pady=5)

root.mainloop()
