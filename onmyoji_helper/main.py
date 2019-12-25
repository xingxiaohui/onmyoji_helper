"""
程序主入口
其他模块都可删除了都以方法的形式写在这里
"""
import time

from onmyoji_helper import utils
from onmyoji_helper import config


jieshu = ['jiangli.png', 'jieshu.png']


# 觉醒副本
def kylin():
    path = 'F:/image/kylin/'
    images = config.kylin_image_names
    for img in images:
        print(img)
        # 注意 需要针对不同的图片进行不同的鼠标点击偏移
        if img in jieshu:
            utils.find_and_click(path + str(img), 30)
        else:
            utils.find_and_click(path + str(img), 5)


# 御魂副本
def orochi():
    path = 'F:/image/orochi/'
    images = config.orochi_image_names
    for img in images:
        # 注意 需要针对不同的图片进行不同的鼠标点击偏移
        if img in jieshu:
            utils.find_and_click(path + str(img), 30)
        else:
            utils.find_and_click(path + str(img), 5)


# 探索副本
# 探索副本要素过多且复杂，不打算实现了
# def explore():
#     FLAG = True
#     path = 'F:/image/explore/'
#     images = config.explore_image_names
#     while FLAG:
#         for img in images:
#             print(img)
#             # 注意 需要针对不同的图片进行不同的鼠标点击偏移
#             if img in jieshu:
#                 utils.find_and_click(path + str(img), 30)
#             else:
#                 utils.find_and_click(path + str(img), 5)


# 组队战斗、妖气封印、年兽
def troops():
    path = 'F:/image/troops/'
    images = config.troops_image_names
    for img in images:
        print(img)
        # 注意 需要针对不同的图片进行不同的鼠标点击偏移
        if img in jieshu:
            utils.find_and_click(path + str(img), 30)
        else:
            utils.find_and_click(path + str(img), 5)