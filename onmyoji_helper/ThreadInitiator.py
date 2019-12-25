import threading

from onmyoji_helper import main


class ThreadInitiator(threading.Thread):
    def __init__(self, target):
        threading.Thread.__init__(self)
        self.flag = True
        self.target = target

    def run(self):
        print("开始线程：" + self.target)
        while self.flag:
            if self.target == 'kylin':
                main.kylin()
            elif self.target == 'orochi':
                main.orochi()
            elif self.target == 'troops':
                main.troops()
        print("退出线程：" + self.target)

    def stop(self):
        self.flag = False
