# Welcome to Cursor



# 1. Try generating with command K on a new line. Ask for a pytorch script of a feedforward neural network
# 2. Then, select the outputted code and hit chat. Ask if there's a bug. Ask how to improve.
# 3. Try selecting some code and hitting edit. Ask the bot to add residual layers.
# 4. To try out cursor on your own projects, go to the file menu (top left) and open a folder.

import db
import tkinter as tk
from tkinter import filedialog
import os


class Notepad:
    def __init__(self, master):
        self.master = master
        master.title("Notepad")

        self.textarea = tk.Text(master)
        self.textarea.pack(fill=tk.BOTH, expand=True)

        self.menu = tk.Menu(master)
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.menu.add_cascade(label="File", menu=self.file_menu)

        master.config(menu=self.menu)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                self.textarea.delete(1.0, tk.END)
                self.textarea.insert(tk.END, file.read())

    def new_file(self):
        self.textarea.delete(1.0, tk.END)
        self.master.title("Untitled - Notepad")
        self.file_path = None
        self.dialog = tk.Toplevel()
        self.dialog.title("New Event")
        tk.Label(self.dialog, text="Title:").grid(row=0, column=0, sticky="w")
        tk.Label(self.dialog, text="Time:").grid(row=1, column=0, sticky="w")
        tk.Label(self.dialog, text="Note:").grid(row=2, column=0, sticky="w")
        tk.Label(self.dialog, text="location:").grid(row=3, column=0, sticky="w")
        self.title_entry = tk.Entry(self.dialog)
        self.time_entry = tk.Entry(self.dialog)
        self.note_entry = tk.Entry(self.dialog)
        self.location_entry = tk.Entry(self.dialog)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)
        self.time_entry.grid(row=1, column=1, padx=5, pady=5)
        self.note_entry.grid(row=2, column=1, padx=5, pady=5)
        self.location_entry.grid(row=3, column=1, padx=5, pady=5)

        image_path = []

        def browse_file():
            filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file",
                                                  filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
            image_path.append(filename)

        tk.Button(self.dialog, text="添加图片", command=browse_file)\
            .grid(row=4, column=0, sticky="w")
        tk.Button(self.dialog, text="保存", command=self.save_data_to_database).grid(row=5, column=0, sticky="w")
        tk.Button(self.dialog, text="取消", command=self.dialog.destroy).grid(row=5, column=1, sticky="e")

    def save_data_to_database(self):
        title = self.title_entry.get()
        time = self.time_entry.get()
        notes = self.notes_entry.get()
        location = self.location_entry.get()
        image = self.image_entry.get()
        db.insert_data(title, time, notes, location, image)


root = tk.Tk()
notepad = Notepad(root)
root.mainloop()
