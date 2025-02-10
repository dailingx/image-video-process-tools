import os
import wave

def join_voice(voice_dir):
    output_file = os.path.join(voice_dir, "combined.wav")
    with wave.open(output_file, 'wb') as output:
        file_count = len([name for name in os.listdir(voice_dir) if name.endswith('.wav')])
        for i in range(1, file_count):
            file_name = os.path.join(voice_dir, f"{i}.wav")
            with wave.open(file_name, 'rb') as input_file:
                if i == 1:
                    output.setparams(input_file.getparams())
                output.writeframes(input_file.readframes(input_file.getnframes()))


if __name__ == '__main__':
    voice_dir = "C:\\Users\daixinliang\Desktop\\test1"
    join_voice(voice_dir)
