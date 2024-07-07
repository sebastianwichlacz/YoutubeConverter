from pytube import YouTube
from sys import argv

video_url = argv[1]

yt = YouTube(video_url)

print("Title: ",yt.title)

print("Views: ",yt.views)

video_stream = yt.streams.filter(only_audio=True).first()

video_stream.download(filename='video.mp3')

print("File saved as 'audio.mp3'")