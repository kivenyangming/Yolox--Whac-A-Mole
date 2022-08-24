import numpy as np
from PIL import Image
from yolo import YOLO

# 监控鼠标键盘的库

import pyautogui


def GetImages():
    img = pyautogui.screenshot()  # 获取当前屏幕图像
    return img


if __name__ == "__main__":
    # 获取当前屏幕信息
    yolo = YOLO()
    while 1:
        img = GetImages()
        frame = Image.fromarray(np.uint8(img))
        yolo.detect_image(frame)
