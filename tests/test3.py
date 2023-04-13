import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, minsize=10)

left_frame = tk.Frame(frame, bg="red", height=50)
left_frame.grid(row=0, column=0, sticky="nsew")

right_frame = tk.Frame(frame, bg="blue", height=50, width=10)
right_frame.grid(row=0, column=1, sticky="nsew")

root.mainloop()
