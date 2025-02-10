from PIL import Image


def split_image_into_parts(image_path, n):
    # 打开图片
    img = Image.open(image_path)

    # 获取图片的宽度和高度
    width, height = img.size

    # 计算每份图片的宽度
    part_width = width // n

    # 创建一个列表来保存切割后的图片
    parts = []

    # 循环切割图片
    for i in range(n):
        # 计算切割区域的坐标
        left = i * part_width
        top = 0
        right = left + part_width
        bottom = height

        # 切割图片
        part = img.crop((left, top, right, bottom))

        # 保存切割后的图片
        part.save(f'part_{i + 1}.jpg')

        # 将切割后的图片添加到列表中
        parts.append(part)

    return parts


if __name__ == '__main__':
    # 使用函数
    image_path = 'C:\\Users\daixinliang\Desktop\\test_img\output (3).png'  # 替换为你的图片路径
    n = 3  # 你想要切割的份数
    split_image_into_parts(image_path, n)


