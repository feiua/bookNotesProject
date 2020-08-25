# _*_ coding.utf-8 _*_
# 开发团队: 待君加入
# 开发人员：Jianfei
# 开发时间：some data5:10 PM
# 文件名称：prac1.py
# 开发工具：PyCharm

'''

'''

import tkinter as tk

class APP:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack(side=tk.LEFT, padx=20, pady=20)

        self.hi_there = tk.Button(frame, text='   打招呼   ', fg='blue',
                                  command=self.say_hi)
        self.hi_there.pack()

    def say_hi(self):
        print('Hi!')

root = tk.Tk()
app = APP(root)

root.mainloop()
