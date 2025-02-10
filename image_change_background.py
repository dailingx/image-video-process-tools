import cv2
import numpy as np
from PIL import Image, ImageSequence


def replace_transparent_background(image_path):
    # 打开图片
    with Image.open(image_path) as img:
        # 将图片转换为RGBA模式，以支持透明度
        img = img.convert("RGBA")

        # 创建一个红色背景的图片，尺寸与原图相同
        # 绿色 0 255 0
        background = Image.new("RGBA", img.size, (0, 255, 0, 255))  # 红色背景，完全不透明

        # 将原图与背景图结合，透明部分会被背景图填充
        combined_image = Image.alpha_composite(background, img)

        # 获取原图片的文件名和扩展名
        filename = image_path.split("/")[-1]
        filename_without_ext, file_extension = filename.split(".")

        # 在同级目录下保存新文件，文件名为原文件名加上"_red_background"
        new_image_path = "/".join(
            image_path.split("/")[:-1]) + f"/{filename_without_ext}_green_background.{file_extension}"

        # 保存新图片
        combined_image.save(new_image_path)

        print(f"新图片已保存：{new_image_path}")


from moviepy.editor import VideoFileClip, ImageSequenceClip

def process_video_to_gif(video_path):
    clip = VideoFileClip(video_path)
    frames = []
    for frame in clip.iter_frames(fps=clip.fps):
        # 处理每一帧
        processed_frame = np.copy(frame)
        # 将视频帧转换为 RGBA 格式
        if processed_frame.shape[2] == 3:  # 如果视频帧不包含 alpha 通道
            processed_frame = np.concatenate([processed_frame, 255 * np.ones(processed_frame.shape[:2] + (1,), dtype=processed_frame.dtype)], axis=2)

        # 将满足条件的像素点设置为透明
        transparent_indices = np.where(
            (processed_frame[:, :, 0] >= 0) & (processed_frame[:, :, 0] <= 10) &
            (processed_frame[:, :, 1] >= 220) & (processed_frame[:, :, 1] <= 255) &
            (processed_frame[:, :, 3] >= 0) & (processed_frame[:, :, 3] <= 10)
        )
        processed_frame[transparent_indices[0], transparent_indices[1], 3] = 0
        frames.append(processed_frame)

    result_gif = ImageSequenceClip(frames, fps=clip.fps)
    result_gif.write_gif("result.gif", fps=clip.fps, program='ImageMagick', opt='optimizeplus', fuzz=10)



if __name__ == '__main__':
    # 使用示例
    replace_transparent_background("C:\\Users\daixinliang\Desktop\\test_img\少爷和我 剧本\音频分2\龙傲天-2-512-透明.png")
    # process_video_to_gif("C:\\Users\daixinliang\Desktop\\test_img\少爷和我 剧本\音频分2\\3-test-face0.5-l-green-2.mp4")
