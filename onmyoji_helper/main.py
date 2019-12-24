"""
程序主入口
其他模块都可删除了都以方法的形式写在这里
"""
from onmyoji_helper import Utils
from onmyoji_helper.Config import Config
import os


# 觉醒副本
def kylin():
    FLAG = True
    path = 'E:/kylin/'
    images = Config.kylin_image_names
    while FLAG:
        for img in images:
            # 注意 需要针对不同的图片进行不同的鼠标点击偏移
            Utils.find_and_click(path+str(img))
        FLAG = False


# 御魂副本
def orochi():
    FLAG = True
    path = 'E:/orochi/'
    images = Config.kylin_image_names
    while FLAG:
        for img in images:
            # 注意 需要针对不同的图片进行不同的鼠标点击偏移
            Utils.find_and_click(path+str(img))
        FLAG = False


# 探索副本
def explore():
    FLAG = True
    path = 'E:/explore/'
    images = Config.kylin_image_names
    while FLAG:
        for img in images:
            # 注意 需要针对不同的图片进行不同的鼠标点击偏移
            Utils.find_and_click(path+str(img))
        FLAG = False


# if __name__ == "__main__":
#     kylin()
#     print(os.getcwd())
