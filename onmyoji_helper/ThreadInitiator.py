"""
线程支持类，用于启动线程调用脚本方法
"""
import threading
import time
from tkinter import END

from onmyoji_helper import main


class ThreadInitiator(threading.Thread):
    def __init__(self, target, log):
        threading.Thread.__init__(self)
        self.flag = True
        self.target = target
        self.log = log

    def run(self):
        count = 1
        print("开始线程：" + self.target)
        self.log.insert(END,
                        time.strftime('%Y-%m-%d %H:%M:%S ',
                                      time.localtime(time.time())) + '开始挑战\n')
        while self.flag:
            self.log.insert(END,
                            time.strftime('%Y-%m-%d %H:%M:%S ',
                                          time.localtime(time.time())) + '第' + str(count) + '轮开始\n')
            self.log.see(END)
            if self.target == 'kylin':
                main.kylin()
            elif self.target == 'orochi':
                main.orochi()
            elif self.target == 'troops':
                main.troops()
            # elif self.target == 'test':
            #     print('test')
            #     time.sleep(2)
            count += 1
            if count > 60:
                self.log.delete(1.0, END)  # 使用 delete
                self.log.insert(END, ' 清空日志\n')
                self.log.see(END)
        self.log.insert(END,
                        time.strftime('%Y-%m-%d %H:%M:%S ',
                                      time.localtime(time.time())) + '结束挑战\n')
        self.log.see(END)

    def stop(self):
        self.flag = False
