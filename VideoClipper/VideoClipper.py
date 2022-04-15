from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip

class VideoEditor:
  def __init__(self, input_video_location, output_location):
    self.input_location = input_video_location
    self.output_location = output_location

  def clip(self):
    clip = VideoFileClip(self.input_location)
    rate = clip.fps
    with open("interval.txt") as f:
      interval = f.readlines()
    interval = [x.strip() for x in interval]

    clipcount = 0
    for time in interval:
      starttime = int(time.split("-")[0])
      endtime = int(time.split("-")[1])
      name = str(rate * 60 * clipcount) + "thFrame.mp4"
      ffmpeg_extract_subclip(
          self.input_location, starttime, endtime, targetname=name)
      clipcount += 1
    return clipcount

#test = VideoEditor(r"C:\Users\nik_s\Downloads\data\airshow.mp4", '')
#print (test.clip())