import cv2
import math
import os
import random
import numpy as np

from PIL import Image, ImageDraw, ImageFilter

# 增加背景噪声
def gaussian_noise(height, width):

    # 创建白图片
    image = np.ones((height, width)) * 255

    # 加入高斯噪声
    cv2.randn(image, 235, 10)

    return Image.fromarray(image).convert('RGBA')

# 纯白色背景
def plain_white(height, width):
    return Image.new("L", (width, height), 255).convert('RGBA')

# 灰阶背景
def quasicrystal(height, width):
    image = Image.new("L", (width, height))
    pixels = image.load()
    # 计算频率
    frequency = random.random() * 30 + 20
    # 增加相
    phase = random.random() * 2 * math.pi
    # 轮流替换
    rotation_count = random.randint(10, 20)

    for kw in range(width):
        y = float(kw) / (width - 1) * 4 * math.pi - 2 * math.pi
        for kh in range(height):
            x = float(kh) / (height - 1) * 4 * math.pi - 2 * math.pi
            z = 0.0
            for i in range(rotation_count):
                r = math.hypot(x, y)
                a = math.atan2(y, x) + i * math.pi * 2.0 / rotation_count
                z += math.cos(r * math.sin(a) * frequency + phase)
            c = int(255 - round(255 * z / rotation_count))
            pixels[kw, kh] = c
    return image.convert('RGBA')

# 图片背景
def picture(height, width):

    pictures = os.listdir('./pictures')

    if len(pictures) > 0:
        picture = Image.open('./pictures/' + pictures[random.randint(0, len(pictures) - 1)])

        if picture.size[0] < width:
            picture = picture.resize([width, int(picture.size[1] * (width / picture.size[0]))], Image.ANTIALIAS)
        elif picture.size[1] < height:
            picture.thumbnail([int(picture.size[0] * (height / picture.size[1])), height], Image.ANTIALIAS)

        if (picture.size[0] == width):
            x = 0
        else:
            x = random.randint(0, picture.size[0] - width)
        if (picture.size[1] == height):
            y = 0
        else:
            y = random.randint(0, picture.size[1] - height)
            
        return picture.crop(
            (
                x,
                y,
                x + width,
                y + height,
            )
        )
    else:
        raise Exception('没文件在目录里面!')
