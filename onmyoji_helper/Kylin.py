"""
觉醒材料模块
"""
import cv2
import numpy

from onmyoji_helper import Config, Utils


class Kylin:
    def __init__(self):
        self._flag = False
        self.NeedCloseGame = False
        self.NeedCloseSystem = False

    def run(self):
        while self._flag is not True:
            kp, des = Utils.detect_and_compute_screen_shot()
            print(1, len(kp), '--', des)
            img = cv2.imread('D:/target.png', cv2.IMREAD_GRAYSCALE)
            kp1, des1 = Utils.orb_compute(img)
            print(2, len(kp1), '--', des1)
            pos = Utils.get_location(img, kp, des)
            print(2, pos)
            new = Utils.cheat_pos(pos)
            Utils.click(new)
            self._flag = True


if __name__ == '__main__':
    ky = Kylin()
    ky.run()
