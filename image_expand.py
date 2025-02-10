from PIL import Image

def extend_image_to_ratio(image_path, output_path, target_ratio=(1, 1)):
    # 打开图片
    with Image.open(image_path) as img:
        # 获取原始图片的尺寸
        original_width, original_height = img.size

        # 计算目标尺寸
        aspect_ratio = original_height / original_width
        target_height = original_height
        target_width = int(target_height * target_ratio[0] / target_ratio[1])

        # 如果计算出的宽度大于原始宽度，则需要调整
        if target_width > original_width:
            # 计算新的宽度和高度
            new_width = original_width
            new_height = int(new_width * aspect_ratio)

            # 扩展图片以保持原始比例
            img = img.resize((new_width, new_height), Image.LANCZOS)

            # 创建一个新的图片，背景为白色
            new_img = Image.new('RGB', (target_width, target_height), 'white')
            # 将原始图片粘贴到新图片的中心
            new_img.paste(img, ((target_width - new_width) // 2, 0))
        else:
            # 创建一个新的图片，背景为白色
            new_img = Image.new('RGB', (target_width, target_height), 'white')
            # 将原始图片粘贴到新图片的中心
            new_img.paste(img, (0, (target_height - original_height) // 2))

        # 保存新的图片
        new_img.save(output_path, quality=95)  # JPEG格式，质量设置为95


def replace_transparent_background(image_path, output_path):
    # 打开图片
    img = Image.open(image_path)

    # 将图片转换为 RGBA 模式，以确保有 alpha 通道
    img = img.convert("RGBA")

    # 创建一个白色背景的图片
    bg = Image.new("RGBA", img.size, (255, 255, 255, 255))

    # 将原始图片粘贴到白色背景上
    bg.paste(img, mask=img.split()[3])  # 3 是 alpha 通道的索引

    # 保存新的图片
    bg.save(output_path, "PNG")

if __name__ == '__main__':
    # replace_transparent_background("C:\\Users\daixinliang\Desktop\\test_img\\rembg-outer_7b528fd59bd.png", "C:\\Users\daixinliang\Desktop\\test_img\\out.jpg")
    # 使用函数
    extend_image_to_ratio('D:\\ComfyUI-workflow\\upscale_1729672988227_.png', 'D:\\ComfyUI-workflow\\output_image_1014_2.png')
