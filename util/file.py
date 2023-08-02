import json
import os
# from tkinter import filedialog


# filedialog.askopenfilename(title="Select file", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

def setting(path):
    if not os.path.exists(path):
        data = {}
        with open(path, 'w') as file:
            json.dump(data, file)
    else:
        with open(path, 'r') as file:
            data = json.load(file)
    return data

# setting('./setting.json')