import os.path
import subprocess


def cached_image(path: str):
    if not os.path.isfile(path):
        print("Rendering started")
        popen = subprocess.Popen(["./a.out"], stdout=subprocess.PIPE)
        popen.wait()
    else:
        print("Reusing cached image")
    with open(path, "rb") as fin:
        image_data = fin.read()
    return image_data
