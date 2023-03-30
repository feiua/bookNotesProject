#!/usr/bin/env python
# _*_ coding.utf-8 _*_
# @Site    : 
# 开发团队: 待君加入
# 开发人员：Lenovo
# 开发时间：2023-03-3013:53
# 文件名称：gtp_version.py
# 开发工具：PyCharm

import tkinter as tk

class Notepad:
    def __init__(self, master):
        self.master = master
        self.master.title('Notepad')

        # create a menu bar
        menubar = tk.Menu(self.master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='New', command=self.new_note)
        filemenu.add_command(label='Open', command=self.open_note)
        menubar.add_cascade(label='File', menu=filemenu)
        self.master.config(menu=menubar)

    def new_note(self):
        # create a new note
        new_window = tk.Toplevel(self.master)
        new_window.title('New Note')

        # create labels and entry fields for the note information
        title_label = tk.Label(new_window, text='Title:')
        title_entry = tk.Entry(new_window)
        time_label = tk.Label(new_window, text='Time:')
        time_entry = tk.Entry(new_window)
        location_label = tk.Label(new_window, text='Location:')
        location_entry = tk.Entry(new_window)
        people_label = tk.Label(new_window, text='People:')
        people_entry = tk.Entry(new_window)
        event_label = tk.Label(new_window, text='Event:')
        event_entry = tk.Entry(new_window)

        # create a save button
        save_button = tk.Button(new_window,
                                text='Save',
                                command=lambda: self.save_note(title_entry.get(),
                                                               time_entry.get(), location_entry.get(), people_entry.get(), event_entry.get()))

        # grid the labels, entry fields, and save button
        title_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        title_entry.grid(row=0, column=1, padx=5, pady=5, sticky='e')
        time_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        time_entry.grid(row=1, column=1, padx=5, pady=5, sticky='e')
        location_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        location_entry.grid(row=2, column=1, padx=5, pady=5, sticky='e')
        people_label.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        people_entry.grid(row=3, column=1, padx=5, pady=5, sticky='e')
        event_label.grid(row=4, column=0, padx=5, pady=5, sticky='w')
        event_entry.grid(row=4, column=1, padx=5, pady=5, sticky='e')

    def open_note(self):
        # open an existing note
        pass

if __name__ == '__main__':
    root = tk.Tk()
    app = Notepad(root)
    root.mainloop()
