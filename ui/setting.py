import tkinter as tk
from tkinter import ttk


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("生草机")
        self.root.geometry("800x600")
        self.root.resizable(0,0)

        self.label_input = tk.Label(root, text="请输入要生草的内容：", font=("Microsoft YaHei", 11))
        self.label_input.grid(row=0, column=0, padx=5, pady=5)

        self.text_input = tk.Text(root, font=("Microsoft YaHei", 11), wrap=tk.WORD, width=50, height=8)
        self.text_input.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.label_times = tk.Label(root, text="次数：", font=("Microsoft YaHei", 11))
        self.label_times.grid(row=2, column=0, padx=5, pady=5)

        self.entry_times = tk.Entry(root, font=("Microsoft YaHei", 11), width=5)
        self.entry_times.grid(row=2, column=1, padx=5, pady=5)
        self.entry_times.insert(0, "1")

        self.label_timeout = tk.Label(root, text="超时：", font=("Microsoft YaHei", 11))
        self.label_timeout.grid(row=2, column=2, padx=5, pady=5)

        self.entry_timeout = tk.Entry(root, font=("Microsoft YaHei", 15), width=5)
        self.entry_timeout.grid(row=2, column=3, padx=5, pady=5)
        self.entry_timeout.insert(0, "10")

        self.button_start = tk.Button(root, text="开始翻译", font=("Microsoft YaHei", 11), )  # command=self.start
        self.button_start.grid(row=2, column=4, padx=5, pady=5)

        self.label_output = tk.Label(root, text="生草结果：", font=("Microsoft YaHei", 11))
        self.label_output.grid(row=3, column=0, padx=5, pady=5)

        self.text_output = tk.Text(root, font=("Microsoft YaHei", 11), wrap=tk.WORD, width=50, height=8)
        self.text_output.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.label_lang = tk.Label(root, text="当前语言：None", font=("Microsoft YaHei", 11))
        self.label_lang.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.progress_bar = ttk.Progressbar(root, maximum=1, mode="determinate", length=500)
        self.progress_bar.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        self.label_url_base = tk.Label(root, text="谷歌翻译镜像网站：", font=("Microsoft YaHei", 11))
        self.label_url_base.grid(row=8, column=0, padx=5, pady=5)

        self.entry_url_base = tk.Entry(root, font=("Microsoft YaHei", 11), width=30)
        self.entry_url_base.grid(row=8, column=1, columnspan=2, padx=5, pady=5)
        self.entry_url_base.insert(0, "https://gt.cky.codes")
        self.root.mainloop()
