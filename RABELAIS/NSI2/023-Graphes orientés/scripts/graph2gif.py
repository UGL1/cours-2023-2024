from PIL import Image

images = []
for i in range(7):
    images.append(Image.open(str(i).zfill(2) + '.png'))


images[0].save('result.gif',
               save_all=True, append_images=images[1:], optimize=False, duration=1000, loop=0)