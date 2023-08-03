# dialog.py
from tkinter import *

class Dialog(Toplevel):
    def __init__(self, master=None, **kw) -> None:
        super().__init__(master, **kw)
        self.protocol("WM_DELETE_WINDOW", self.destroy) # intercept close button
        self.transient(master)   # dialog window is related to main
        self.wait_visibility() # can't grab until window appears, so we wait
        self.grab_set()        # ensure all input goes to our window
        # place dialog below parent if running htest
        self.geometry("+%d+%d" % (
                        master.winfo_rootx()+30,
                        master.winfo_rooty()+30))

    def destroy(self):
        self.grab_release()
        super().destroy()
