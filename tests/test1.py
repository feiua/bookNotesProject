#!/usr/bin/env python
# _*_ coding.utf-8 _*_
# @Site    : 
# 开发团队: 待君加入
# 开发人员：Lenovo
# 开发时间：2020-09-2616:18
# 文件名称：test.py
# 开发工具：PyCharm


import sqlite3
import os
import io
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def zoom_image(img, new_width):
    """
    Keep the aspect ratio of image
    :param img: img = Image.open('path/to/image.jpg')
    :param new_width: value of new width set
    :return: the image with new size
    """

    # Get the original size of the image
    width, height = img.size

    # Calculate the aspect ratio of the image
    aspect_ratio = width / height

    # Calculate the new height of the image based on a width of 100 pixels
    new_height = int(new_width / aspect_ratio)

    # Resize the image using Lanczos resampling
    img = img.resize((100, new_height), Image.LANCZOS)

    # Create a Tkinter PhotoImage object from the resized image
    return img


# Connect to the database
database_path = r'D:/UserFiles/文档/GitHub/bookNotesProject/db/data/mydatabase.db'
conn = sqlite3.connect(database_path)
c = conn.cursor()

# Retrieve the image file paths from the database
c.execute("SELECT data FROM image_table WHERE event_id=?", ('940ade2b-f141-4152-b250-11b972776184',))
images_data = [row[0] for row in c.fetchall()]

root = tk.Tk()


# Create a canvas to display the images
canvas = tk.Canvas(root, width=110 * len(images_data), height=300)
canvas.pack()

# Loop through the image file paths and display the images on the canvas

x_coordinate = 0
photo_list = []
for i, image_data in enumerate(images_data):
    # Create the Pillow image and Tkinter PhotoImage objects
    img = Image.open(io.BytesIO(image_data))
    new_width = 100
    # print(x_coordinate, x_coordinate+new_width)
    img = zoom_image(img, new_width)
    photo_list.append(ImageTk.PhotoImage(img))

    # Display the image on the canvas
    canvas.create_image(x_coordinate, 0, image=photo_list[i], anchor=tk.NW)
    x_coordinate += 10 + new_width

    # break

root.mainloop()