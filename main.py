import tkinter as tk
import ui
import util

ui_main = ui.main.MainWindow

if __name__ == "__main__":
    util.file.setting('./setting.json')
    root = tk.Tk()
    app = ui_main(root)
    root.mainloop()
