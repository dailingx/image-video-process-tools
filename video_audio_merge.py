import os
from moviepy.editor import VideoFileClip, concatenate_audioclips

def merge_videos_audio_to_mp3(input_directory, output_filename):
    audio_clips = []

    # 获取目录下所有以 00 开头的 mp4 文件
    video_files = [file for file in os.listdir(input_directory) if file.endswith(".mp4") and file.startswith("000")]
    video_files.sort()  # 按顺序排序

    for video_file in video_files:
        video_path = os.path.join(input_directory, video_file)
        video = VideoFileClip(video_path)
        audio = video.audio
        audio_clips.append(audio)

    final_audio = concatenate_audioclips(audio_clips)
    final_audio.write_audiofile(output_filename)

if __name__ == '__main__':
    # Example usage
    input_directory = "C:\\Users\daixinliang\Desktop\\test_img\\result"
    output_filename = "merged_audio.mp3"
    merge_videos_audio_to_mp3(input_directory, output_filename)
