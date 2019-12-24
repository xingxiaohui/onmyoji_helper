"""
觉醒材料模块
"""
import cv2
import numpy

from onmyoji_helper import Config, Utils

# images = Config.kylin_image_names
# images = Config.yuhun_image_names
images = Config.tansuo_image_names


class Kylin:
    def __init__(self):
        self._flag = False
        self.NeedCloseGame = False
        self.NeedCloseSystem = False

    def run(self):
        while self._flag is not True:
            kp, des = Utils.detect_and_compute_screen_shot()
            print(1, len(kp), '--', des)
            for i in images:
                url = 'G:/image/'+str(i)
                # print(url)
                img = cv2.imread(url, cv2.IMREAD_GRAYSCALE)
                kp1, des1 = Utils.orb_compute(img)
                print(2, len(kp1), '--', des1)
                pos = Utils.get_location(img, kp, des)
                if pos is not None:
                    print(2, pos)
                    new = Utils.cheat_pos(pos)
                    Utils.click(new)
            # self._flag = True
            img = cv2.imread('D:/target.png', cv2.IMREAD_GRAYSCALE)
            # img1 = cv2.resize(img, (300, 300), 0, 0)  # 注意width在前 height在后
            # cv2.imshow('img1', img1)  # 显示原始图片
            # cv2.waitKey(0)
            kp1, des1 = Utils.orb_compute(img)
            print(2, len(kp1), '--', des1)
            pos = Utils.get_location(img, kp, des)
            print(3, pos)
            new = Utils.cheat_pos(pos)
            Utils.click(new)
            self._flag = True


if __name__ == '__main__':
    ky = Kylin()
    ky.run()
