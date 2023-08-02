import tkinter as tk
import ui

ui_main = ui.main.MainWindow

if __name__ == "__main__":
    root = tk.Tk()
    app = ui_main(root)
    root.mainloop()
