import VideoClipper
import unittest

class VideoClipperTests(unittest.TestCase):
    def test_video_clipper_output (self):
        clip = VideoClipper.VideoEditor(
                r"C:\Users\nik_s\Downloads\data\airshow.mp4", '')
        clipcount = clip.clip()
        self.assertEqual(clipcount, 6)

