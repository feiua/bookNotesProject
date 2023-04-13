from db import data_control
import tkinter as tk
from tkinter import ttk
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
        self.file_menu.add_command(label="New", command=self.new_file) # create/add a record
        self.file_menu.add_command(label="Open", command=self.open_file) # open a notebook from the database
        self.menu.add_cascade(label="File", menu=self.file_menu)

        master.config(menu=self.menu)

    def open_file(self):
        # database_path = r'D:/UserFiles/文档/GitHub/bookNotesProject/db/data/mydatabase.db'
        database_path = r'E:/PythonCode/practices/bookNotesProject/db/data/mydatabase.db'
        col_names, rows = data_control.get_table_data(database_path)

        # Create a frame to hold the table and buttons
        self.dialog = tk.Toplevel()
        self.dialog.title("Table View")
        frame = tk.Frame(self.dialog)
        frame.pack(side="top", fill="both", expand=True)

        # Create a table widget
        style = ttk.Style()
        style.configure("Treeview.Heading", rowheight=400)
        style.configure("Treeview", rowheight=30)
        table = ttk.Treeview(frame)
        table.pack(side="left", fill="both", expand=True)

        # Define the columns
        table['columns'] = col_names

        # Format the columns
        table.column('#0', width=0, stretch=tk.NO)
        for col_name in col_names:
            table.column(str(col_name), anchor=tk.CENTER, width=100)

        # Create the headings
        table.heading('#0', text='', anchor=tk.CENTER)
        for col_name in col_names:
            table.heading(str(col_name).lower(), text=str(col_name), anchor=tk.CENTER)

        # Add the data to the table
        for row in rows:
            table.insert(parent='', index='end', iid=row[0], values=row)

        # Create a frame to hold the buttons
        button_frame = tk.Frame(frame)
        button_frame.pack(side="right", fill="y")
        tk.Frame(button_frame, height=25).pack(side="top", fill="x")

        # Create a button for each row in the table
        for item in table.get_children():
            button = tk.Button(button_frame, text="Edit")
            button.configure(width=5, height=1)
            button.pack(side="top", fill="x")


    def new_file(self):
        self.textarea.delete(1.0, tk.END)
        self.master.title("Untitled - Notepad")
        self.file_path = None
        self.dialog = tk.Toplevel()
        self.dialog.title("New Event")

        # create frames to place entries and labels and buttons
        entry_frame = tk.Frame(self.dialog)
        entry_frame.pack(side="top", fill="both", expand=True)

        entry_frame.columnconfigure(0, minsize=10)  # column to place labels
        entry_frame.columnconfigure(1, weight=1)  # column to place entries
        entry_frame.columnconfigure(2, minsize=20)  # column for margin on right side

        button_frame = tk.Frame(self.dialog)
        button_frame.pack(side="top", fill="both", expand=True)
        button_frame.columnconfigure(0, minsize=20)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)
        button_frame.columnconfigure(3, minsize=20)

        bottom_frame = tk.Frame(self.dialog, height=10)
        bottom_frame.pack(side="top")


        # place labels and entries
        tk.Label(entry_frame, text="Title:", width=10).grid(row=0, column=0)
        tk.Label(entry_frame, text="Time:", width=10).grid(row=1, column=0)
        tk.Label(entry_frame, text="Note:", width=10).grid(row=2, column=0)
        tk.Label(entry_frame, text="location:", width=10).grid(row=3, column=0)
        self.title_entry = tk.Entry(entry_frame)
        self.time_entry = tk.Entry(entry_frame)
        self.note_entry = tk.Entry(entry_frame)
        self.location_entry = tk.Entry(entry_frame)
        self.title_entry.grid(row=0, column=1, sticky="ew")
        self.time_entry.grid(row=1, column=1, sticky="ew")
        self.note_entry.grid(row=2, column=1, sticky="ew")
        self.location_entry.grid(row=3, column=1, sticky="ew")

        self.image_paths = []

        def browse_file():
            self.image_paths = filedialog.askopenfilenames(initialdir=os.getcwd(), title="Select image",
                                                  filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

        def save_data_to_database():
            title = self.title_entry.get()
            time = self.time_entry.get()
            notes = self.note_entry.get()
            location = self.location_entry.get()
            image_paths = self.image_paths
            data_control.insert_data(title, time, notes, location, image_paths)
            self.dialog.destroy()

        tk.Button(button_frame, text="添加图片", command=browse_file)\
            .grid(row=0, column=1, sticky="ew")
        tk.Button(button_frame, text="保存", command=save_data_to_database).grid(row=1, column=1, sticky="ws")
        tk.Button(button_frame, text="取消", command=self.dialog.destroy).grid(row=1, column=2, sticky="es")


    def delete_data(self):
        pass


root = tk.Tk()
notepad = Notepad(root)
root.mainloop()
