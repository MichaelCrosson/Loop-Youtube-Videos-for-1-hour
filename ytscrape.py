from pytube import YouTube 
from moviepy.editor import *


def one_hour_loop(SAVE_PATH, link):
#download mp4 from youtube
    
    try:
        yt = YouTube(link)  
        yt_name = yt.title 
        yt_length = yt.length
        yt.streams.filter(progressive = True, 
        file_extension = "mp4").first().download(output_path = SAVE_PATH, 
        filename = yt_name)
        print('mp4 downloaded')
        print(yt_length)
    except:
        print("Error with download")

#looping video with moviepy.editor
    n_name = yt_name+".mp4"
    path = SAVE_PATH+n_name
    clip = VideoFileClip(path)

#loop for makingit 1 hour

    timex = int(round(60/(yt_length/60),0))
    clist = []
    for i in range(timex):
        clist.append(clip)

    clipx = concatenate_videoclips(clist)
    clipx.write_videofile(SAVE_PATH+yt_name+"1 hr Looped.mp4")





