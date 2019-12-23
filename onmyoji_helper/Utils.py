"""
公用方法模块
原作者的检测方法在新版本的opencv中被移除了，采用新的检测方式ORB形式，参考：
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_orb/py_orb.html
"""
import random
import time
import cv2
import numpy
import numpy as np
import pyautogui
from PIL import ImageGrab

# 禁用 pyautogui 的保护性退出
pyautogui.FAILSAFE = False


def get_location(target, kp2, des2):
    """
    获取目标图像在截图中的位置
    :param target:目标图片
    :param kp2:截图的特征点
    :param des2:截图的描述
    :return: 返回坐标(x,y) 与 opencv 坐标系对应
    """
    MIN_MATCH_COUNT = 10
    img1 = target  # cv2.cvtColor(target,cv2.COLOR_BGR2GRAY)# 查询图片
    # img2 = screenShot
    # img2 = cv2.cvtColor(screenShot, cv2.COLOR_BGR2GRAY)  # 训练图片
    # img2 = cv2.resize(img2, dsize=None, fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)
    # 用SIFT找到关键点和描述符

    kp1, des1 = orb_compute(img1)

    # 提取并计算特征点
    bf = cv2.BFMatcher(cv2.NORM_HAMMING)

    # knn筛选结果
    matches = bf.knnMatch(des1, trainDescriptors=des2, k=2)
    good = [m for (m, n) in matches if m.distance < 0.75 * n.distance]
    print(4, len(good))
    if len(good) > MIN_MATCH_COUNT:
        src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        matchesMask = mask.ravel().tolist()
        h, w = img1.shape
        pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
        if M is not None:
            dst = cv2.perspectiveTransform(pts, M)
            arr = np.int32(dst)  #
            midPosArr = arr[0] + (arr[2] - arr[0]) // 2
            midPos = (midPosArr[0][0], midPosArr[0][1])
            # show=cv2.circle(img2,midPos,30,(255,255,255),thickness=5)
            # cv2.imshow('s',show)
            # cv2.waitKey()
            # cv2.destroyAllWindows()
            return midPos
        else:
            return None
    else:
        return None


def cheat_pos(origin, factor=5):
    """
    对原始点击坐标进行随机偏移，防止封号
    :param origin:原始坐标
    :return new:偏移后的坐标
    """
    x, y = random.randint(-factor, factor), random.randint(-factor, factor)
    new = (origin[0] + x, origin[1] + y)
    return new


def click(target):
    """
    点击屏幕上的某个点
    :param target:目标点
    """
    if target is None:
        print('未检测到目标')
    else:
        pyautogui.moveTo(target, duration=0.20)
        pyautogui.click()
        time.sleep(random.randint(500, 1000) / 1000)


def screen_shot():
    """
    获取屏幕截图
    :return:
    """
    screen = ImageGrab.grab()
    # screen.save('D:/screen.jpg')
    # screen = cv2.imread('D:/screen.jpg')
    screen = cv2.cvtColor(numpy.asarray(screen), cv2.COLOR_RGB2BGR)
    return screen


def detect_and_compute_screen_shot():
    kp2, des2 = orb_compute(screen_shot())
    return kp2, des2


def orb_compute(img):
    # 读取图片
    # img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)  # trainning picture
    # 初始化ORB检测器
    orb = cv2.ORB_create()
    kp, des = orb.detectAndCompute(img, None)
    return kp, des
