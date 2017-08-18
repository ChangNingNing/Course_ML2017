import Image
import sys

fileName = sys.argv[1]

im = Image.open(fileName)
oim = im.rotate(180, Image.BILINEAR)
oim.save('ans2.png')
