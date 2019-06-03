import os
import random
from PIL import Image, ImageFilter

from pic_gentor import cpt_textor
from pic_gentor import back_gentor
from pic_gentor import dist_gentor
try:
    from pic_gentor import written_text
except ImportError as e:
    print('无文本生成模块.')


# 将所有参数作为一个元组
class FakeTextDataGenerator(object):
    @classmethod
    def generate_from_tuple(cls, t):

        cls.generate(*t)

    @classmethod
    def generate(cls, index, text, font, out_dir, size, extension, skewing_angle, random_skew, blur, random_blur, background_type, distorsion_type, distorsion_orientation, is_handwritten, name_format, width, alignment, text_color, orientation, space_width, margins, fit):
        image = None

        margin_top, margin_left, margin_bottom, margin_right = margins
        horizontal_margin = margin_left + margin_right
        vertical_margin = margin_top + margin_bottom

        # 创建文本图片
        if is_handwritten:
            if orientation == 1:
                raise ValueError("Vertical handwritten text is unavailable")
            image = handwritten_text_generator.generate(text, text_color, fit)
        else:
            image = cpt_textor.generate(text, font, text_color, size, orientation, space_width, fit)

        random_angle = random.randint(0-skewing_angle, skewing_angle)

        rotated_img = image.rotate(skewing_angle if not random_skew else random_angle, expand=1)

        # 对图像应用扭曲
        if distorsion_type == 0:
            distorted_img = rotated_img # Mind = blown
        elif distorsion_type == 1:
            distorted_img = dist_gentor.sin(
                rotated_img,
                vertical=(distorsion_orientation == 0 or distorsion_orientation == 2),
                horizontal=(distorsion_orientation == 1 or distorsion_orientation == 2)
            )
        elif distorsion_type == 2:
            distorted_img = dist_gentor.cos(
                rotated_img,
                vertical=(distorsion_orientation == 0 or distorsion_orientation == 2),
                horizontal=(distorsion_orientation == 1 or distorsion_orientation == 2)
            )
        else:
            distorted_img = dist_gentor.random(
                rotated_img,
                vertical=(distorsion_orientation == 0 or distorsion_orientation == 2),
                horizontal=(distorsion_orientation == 1 or distorsion_orientation == 2)
            )

        # 将图像大小调整为所需格式

        # 水平方向
        if orientation == 0:
            new_width = int(distorted_img.size[0] * (float(size - vertical_margin) / float(distorted_img.size[1])))
            resized_img = distorted_img.resize((new_width, size - vertical_margin), Image.ANTIALIAS)
            background_width = width if width > 0 else new_width + horizontal_margin
            background_height = size
        # 垂直方向
        elif orientation == 1:
            new_height = int(float(distorted_img.size[1]) * (float(size - horizontal_margin) / float(distorted_img.size[0])))
            resized_img = distorted_img.resize((size - horizontal_margin, new_height), Image.ANTIALIAS)
            background_width = size
            background_height = new_height + vertical_margin
        else:
            raise ValueError("Invalid orientation")

        # 生成背景图像
        if background_type == 0:
            background = back_gentor.gaussian_noise(background_height, background_width)
        elif background_type == 1:
            background = back_gentor.plain_white(background_height, background_width)
        elif background_type == 2:
            background = back_gentor.quasicrystal(background_height, background_width)
        else:
            background = back_gentor.picture(background_height, background_width)

        # 放置对齐文本
        new_text_width, _ = resized_img.size

        if alignment == 0 or width == -1:
            background.paste(resized_img, (margin_left, margin_top), resized_img)
        elif alignment == 1:
            background.paste(resized_img, (int(background_width / 2 - new_text_width / 2), margin_top), resized_img)
        else:
            background.paste(resized_img, (background_width - new_text_width - margin_right, margin_top), resized_img)

        # 高斯模糊
        final_image = background.filter(
            ImageFilter.GaussianBlur(
                radius=(blur if not random_blur else random.randint(0, blur))
            )
        )

        # 生成结果图像的名称
        if name_format == 0:
            image_name = '{}_{}.{}'.format(text, str(index), extension)
        elif name_format == 1:
            image_name = '{}_{}.{}'.format(str(index), text, extension)
        elif name_format == 2:
            image_name = '{}.{}'.format(str(index),extension)
        else:
            print('{} is not a valid name format. Using default.'.format(name_format))
            image_name = '{}_{}.{}'.format(text, str(index), extension)

        # 保存图片
        final_image.convert('RGB').save(os.path.join(out_dir, image_name))
