#!/bin/python3

import sys
import numpy as np

nameA = sys.argv[1]
nameB = sys.argv[2]

finA = open(nameA, 'r')
finB = open(nameB, 'r')
matrixA = []
matrixB = []
for line in finA:
    matrixA.append([int(x) for x in line.split()])
for line in finB:
    matrixB.append([int(x) for x in line.split()])
finA.close()
finB.close()

matrixC = np.dot(matrixA, matrixB)

sortC = np.sort(matrixC, axis=None)

fout = open('ans_one.txt', 'w')
for x in sortC:
    fout.write('%d\n' % x)
fout.close()
