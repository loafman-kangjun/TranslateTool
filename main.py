import tkinter as tk
import ui
import util


def main_window():
    ui.main.MainWindow(root)


def setting_window():
    ui.setting.MainWindow(root)


if __name__ == "__main__":
    util.file.setting('./setting.json')
    root = tk.Tk()
    main_window()
    root.mainloop()
