# Make a function for splitting videos into frames

import cv2
import os
import time

vidcap = cv2.VideoCapture('videos/video.mp4')
total = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
success, image = vidcap.read()
count = 0
while success:
    cv2.imwrite("images/frame%d.jpg" % count, image)  # save frame as JPEG file
    success, image = vidcap.read()
    print(f'Read a new frame: {count + 1}/{total} {success}')
    count += 1
