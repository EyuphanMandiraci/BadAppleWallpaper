# Change the Windows Wallpaper

import os
import ctypes
import time
import playsound


def main():

    path = os.path.dirname(os.path.realpath(__file__))
    image_path = os.path.join(path, "images")

    images = os.listdir(image_path)
    images = tuple(sorted(images, key=lambda x: int(x.split(".")[0].replace("frame", ""))))
    for idx, image in enumerate(images):
        if idx == 0:
            playsound.playsound("video.mp3", False)
        image = os.path.join(image_path, image)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image, 0)
        print(f"{idx + 1}/6580")
        time.sleep(1/30)


main()
