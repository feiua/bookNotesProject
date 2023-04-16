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
from PyQt5 import QtWidgets, QtGui, QtCore
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

    # Create a Qt QPixmap object from the resized image
    return QtGui.QPixmap.fromImage(ImageQt(img))


# Connect to the database
database_path = r'D:/UserFiles/文档/GitHub/bookNotesProject/db/data/mydatabase.db'
conn = sqlite3.connect(database_path)
c = conn.cursor()

# Retrieve the image file paths from the database
c.execute("SELECT data FROM image_table WHERE event_id=?", ('940ade2b-f141-4152-b250-11b972776184',))
images_data = [row[0] for row in c.fetchall()]

app = QtWidgets.QApplication([])

mother_frame = QtWidgets.QWidget()
mother_frame.show()
button = QtWidgets.QPushButton("Hover over me", mother_frame)
button.show()

preview_window = QtWidgets.QWidget()
preview_window.hide()

def show_preview(event):
    # Create a new window to display the preview
    preview_window.show()
    preview_window.setWindowTitle("Image Preview")

    # Create a layout to display the images
    layout = QtWidgets.QHBoxLayout(preview_window)

    x_coordinate = 0
    pixmap_list = []
    new_width = 100
    for i, image_data in enumerate(images_data):
        # Create the Pillow image and Qt QPixmap objects
        img = Image.open(io.BytesIO(image_data))
        pixmap = zoom_image(img, new_width)
        pixmap_list.append(pixmap)

        # Display the image on the layout
        label = QtWidgets.QLabel(preview_window)
        label.setPixmap(pixmap_list[i])
        layout.addWidget(label)
        x_coordinate += 10 + new_width


def hide_preview(event):
    # Code to hide preview of images
    preview_window.hide()

button.enterEvent = show_preview
button.leaveEvent = hide_preview

app.exec_()