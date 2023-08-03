import json
import os


# from tkinter import filedialog


# filedialog.askopenfilename(title="Select file", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
def setting(path):
    with open(path, 'r') as file:
        data = json.load(file)
    return data


def init(path):
    data = {}
    if not os.path.exists(path):
        with open(path, 'w') as file:
            json.dump(data, file)
    return data

# setting('./setting.json')
