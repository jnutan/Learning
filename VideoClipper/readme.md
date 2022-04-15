This code uses moviepy library (https://pypi.org/project/moviepy/). Similar functionality can be achieved through OpenCV and other libraries.

Please follow below steps to install and run the code -
  2.1 Create a virtual env in your project and run -> pip install moviepy
  
  2.2 Add "interval.txt" file at the root and make entries of interval in seconds based on the video file length. 
  
      Below sample is for a video file between 5-6 minutes duration. Add/remove entries based on video file length.
        0-60
        61-120
        121-180
        181-240
        241-300
        301-360
        
  
  2.3 Run VideoClipper.py file and pass the absolute video path as an argument. Output would be the clips of chosen interval saved as ".mp4" in current project directory.
      
      The file name of clips is the starting frame of the clip. For example, the 1st clip may be named 0thFrame.mov, the 2nd clip may be named 180.1234thFrame.mov, etc.
  
 Code desciption:
  
    Lines 1-2: Importing necessary libraries
    Line 4: Define the class that holds the functionality
    Lines 5-7: initialize the object using input/output location
    Lines 10-11: loads the video object and return frame per second value. the fps value will be used later to name the clips.
    Lines 12-14: read the defined interval (60 seconds in this case) and clean up any leading/trailing whitespaces
    Line 17: run for loop for each of the lines in interval.txt file
    Lines 18-19: split and extract values such as 0 and 60 from lines in interval.txtx
    Line 20: logic to name of each clip file 
    Line 21-22: extract the clipped videos (60 seconds length) and save in current directory
    Line 23: increment the value by 1 for the next for loop iteration and support frame based naming of clips
    Line 24: return total clips created
    
Run test case:
  python -m unittest -v c:\Code\Nutan\Video-clipping\test_video_clipper.py
