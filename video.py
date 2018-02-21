import os
import sys

cmd = "ffmpeg -r 1/4 -f image2 -s 1920x1080 -i images/%d.png -vframes 1000 -vcodec libx264 -crf 25  -pix_fmt yuv420p test.mp4";

images = [];
images = os.listdir("./images");
sound = os.listdir("./sound");

os.system(cmd);
images.sort();
