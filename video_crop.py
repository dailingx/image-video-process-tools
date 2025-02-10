from moviepy.editor import *
import os

def split_video(input_video_path, timepoints):
    video = VideoFileClip(input_video_path)
    if not os.path.exists('result'):
        os.makedirs('result')

    for i in range(len(timepoints) + 1):
        if i == 0:
            start_time = 0
        else:
            start_time = convert_to_seconds(timepoints[i - 1])

        if i == len(timepoints):
            end_time = None
        else:
            end_time = convert_to_seconds(timepoints[i])

        subclip = video.subclip(start_time, end_time)
        output_path = f"result/{os.path.basename(input_video_path).split('.')[0]}_part{i + 1}.mp4"
        subclip.write_videofile(output_path, codec='libx264', audio_codec='aac')

def convert_to_seconds(timestamp):
    minutes, seconds = map(int, timestamp.split(':'))
    return minutes * 60 + seconds


if __name__ == '__main__':
    # Example usage
    input_video_path = "C:\\Users\daixinliang\Desktop\\test_img/Starbucks_all_video.mp4"
    timepoints = ["27:35", "52:34", "80:13", "108:38", "135:43", "165:40"]
    split_video(input_video_path, timepoints)
