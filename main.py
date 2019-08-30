from PIL import Image


im = Image.open('genesis.jpg')

print(im.format, im.size)

im.show()
