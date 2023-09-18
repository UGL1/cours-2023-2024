from PIL import Image
from os import listdir


def make_gif(folder):
    images = [Image.open(folder + '/' + file) for file in listdir(folder)]
    images[0].save('result.gif', save_all=True, append_images=images[1:], optimize=True, duration=1000, loop=0)


make_gif('rotation')
