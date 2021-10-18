#! usr/bin/python3

from pytube import YouTube  

print("Enter the URL of the youtube video to be downloaded " )
u = input()
print("Enter the URL of the youtube video to be downloaded " + u)

print("Enter the location of the file to be stored " )
p = input()
print("Enter the location of the file to be stored " + p)



path = p
url = u
resol = "720p"
file_type = "mp4"


video = YouTube(url)

Streams = video.streams


vid = Streams.filter(progressive=True,res=resol).first()
print(vid)

vid.download(path)