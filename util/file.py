import json
from tkinter import filedialog


# filedialog.askopenfilename(title="Select file", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

def setting(path):
    with open(path, 'r') as file:
        data = json.load(file)
    return data
