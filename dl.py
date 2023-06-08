from pytube         import YouTube
from moviepy.editor import VideoFileClip
from os             import path, remove

def download(url):
    yt          = YouTube(url)
    stream      = yt.streams.get_highest_resolution ()
    vid_path    = stream    .download               ()

    name, extension = path.splitext(vid_path)
    if not extension == ".mp4":
        VideoFileClip(vid_path).write_videofile(name + ".mp4")
        remove(vid_path)
        return name + ".mp4"

    return vid_path
