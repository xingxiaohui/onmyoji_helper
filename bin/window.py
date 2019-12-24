import ctypes
import inspect
import threading
import time
import tkinter as tk
from concurrent.futures import thread
from tkinter import *
from tkinter import scrolledtext, messagebox
from onmyoji_helper import main


tasks = []


def StopAll(LogUI):
    """
    :return:
    """
    try:
        global tasks
        for i in tasks:
            i.Terminate()
        tasks = []
        if LogUI is not None:
            LogUI.insert(END,
                         time.strftime('%Y-%m-%d %H:%M:%S',
                                       time.localtime(time.time())) + ' 脚本停止\n')
            # LogUI.insert(END, '全部动作停止\n')
            LogUI.see(END)
    except Exception as e:
        if LogUI is not None:
            tasks = []
            LogUI.insert(END,
                         time.strftime('%Y-%m-%d %H:%M:%S',
                                       time.localtime(time.time())) + ' 脚本停止异常,可能已经停止,请重启再试\n')
            LogUI.see(END)
            print(e)


class Window:
    def __init__(self):
        self.initWidgets()

    def initWidgets(self):
        self.app = tk.Tk()  # 根窗口的实例(root窗口)
        self.app.title('阴阳师游戏助手')
        self.app.geometry('600x300')
        self.app.resizable(0, 0)  # 阻止Python GUI的大小调整
        frame1 = Frame(self.app, padx=20)
        frame1.pack(side=LEFT, fill=BOTH)
        t1 = tk.Label(frame1, text='护肝脚本', font=("华文行楷", 22), borderwidth=2).pack(side=TOP, fill=X, expand=YES)

        frame2 = Frame(self.app)
        t1 = tk.Label(frame2, text='日志', borderwidth=2, font=('微软雅黑', 10), height=1).pack(side=TOP, fill=X, expand=YES)
        t3 = scrolledtext.ScrolledText(frame2, font=('微软雅黑', 10))
        t3.pack(side=TOP, fill=X, expand=YES)
        frame2.pack(side=RIGHT, fill=BOTH, expand=YES)
        Button(frame1, command=lambda: main.orochi(), text='自动御魂副本', width=20).pack(
            side=TOP, expand=YES)
        Button(frame1, command=lambda: main.kylin(), text='自动觉醒副本', width=20).pack(
            side=TOP, expand=YES)
        Button(frame1, command=lambda: main.explore(), text='自动探索副本', width=20).pack(
            side=TOP, expand=YES)
        Checkbutton(frame1, text='体力用完自动关闭游戏', command='').pack(side=TOP, anchor='w')
        Checkbutton(frame1, text='体力用完自动关机', command='').pack(side=TOP, anchor='w')
        Button(frame1, command=lambda: StopAll(t3), text='停止', width=20).pack(side=TOP, expand=YES)

        self.app.protocol("WM_DELETE_WINDOW", '')
        Window.LogUI = t3
        self.app.bind("<Key>", '')
        self.app.mainloop()  # 窗口的主事件循环，必须的。


if __name__ == '__main__':
    app = Window()
