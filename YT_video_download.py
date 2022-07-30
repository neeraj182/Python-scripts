from pytube import YouTube
import os

print(" YouTube Video Downloader")
filedir = os.path.join('/home/neji/Downloads')


try:
    print("YouTube DOWNLOADER")
    print("Paste the link of the YouTube video in the next line.")
    link = input(' ')
    yt = YouTube(link)
    print(yt.title)
    print("Downloading......")
    yd = yt.streams.get_highest_resolution()
    yd.download(filedir)
    print('Downloaded!!!')
except:
    print("Invalid URL, please enter a valid URL")
