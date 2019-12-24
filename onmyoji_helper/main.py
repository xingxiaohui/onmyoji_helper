"""
程序主入口
其他模块都可删除了都以方法的形式写在这里
"""
from onmyoji_helper import utils
from onmyoji_helper import config
import os


jieshu = ['jiangli.png','jieshu.png']


# 觉醒副本
def kylin():
    FLAG = True
    path = 'F:/image/kylin/'
    images = config.kylin_image_names
    while FLAG:
        for img in images:
            print(img)
            # 注意 需要针对不同的图片进行不同的鼠标点击偏移
            if img in jieshu:
                utils.find_and_click(path + str(img), 30)
            else:
                utils.find_and_click(path + str(img), 5)


# 御魂副本
def orochi():
    FLAG = True
    path = 'F:/image/orochi/'
    images = config.orochi_image_names
    while FLAG:
        for img in images:
            # 注意 需要针对不同的图片进行不同的鼠标点击偏移
            utils.find_and_click(path + str(img))
        FLAG = False


# 探索副本
def explore():
    FLAG = True
    path = 'F:/image/explore/'
    images = config.explore_image_names
    while FLAG:
        for img in images:
            print(img)
            # 注意 需要针对不同的图片进行不同的鼠标点击偏移
            if img in jieshu:
                utils.find_and_click(path + str(img), 30)
            else:
                utils.find_and_click(path + str(img), 5)


if __name__ == "__main__":
    # kylin()
    explore()
#     print(os.getcwd())
