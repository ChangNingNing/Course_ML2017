#!/bin/python3

import sys
from PIL import Image

imN = sys.argv[1]
im_mN = sys.argv[2]

im = Image.open(imN)
im_m = Image.open(im_mN)

imP = im.load()
im_mP = im_m.load()

im_r = Image.new(im.mode, im.size, 'white')
im_rP = im_r.load()

for x in range(im.size[0]):
    for y in range(im.size[1]):
        if imP[x, y] != im_mP[x, y]:
            im_rP[x, y] = im_mP[x, y]
im_r.save('ans_two.png')
