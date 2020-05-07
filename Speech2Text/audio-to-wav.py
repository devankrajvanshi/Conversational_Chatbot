from ffmpy import FFmpeg
import os
from pydub import AudioSegment
from os import path

#Path of directory where audio file is stored
os.chdir("C:\\Users\\devan\\Desktop\\SOC20\\Speech2Text")

#"Write the name of the file in this directory to be converted"
audio_file_name = input("File name to be converted ")
Extension_file = input("Extension of file ")
src = audio_file_name + Extension_file

try:
    #Using pyaudio, written for .mp3, can be changed to other input file formats
    ##No need for ffmpy
    dst = "test.wav"

    # convert mp3 to wav
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")
except:
    pass
try:
    #Using ffmpeg, input format need not be .mp3
    ## Reference: https://ffmpy.readthedocs.io/en/latest/examples.html#format-convertion
    ff = FFmpeg(inputs={src: None}, outputs={audio_file_name + '.wav':None})
    ff.cmd
    ff.run()
except:
    print("Invalid input")


