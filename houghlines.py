#!/usr/local/bin/python3

import argparse
import cv2
import numpy as np

def auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
 
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
 
	# return the edged image
	return edged


# parse arguments
parser = argparse.ArgumentParser(description='Remove lines from a Sudoku puzzle image',
                                 formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument('-s', metavar='filename',
                     type=argparse.FileType('r'),
                     help='filename containing puzzle image')
parser.add_argument('-i')
parser.add_argument('-v','--verbose', action='store_true', help='more verbose output')
args = parser.parse_args()

filename = args.i
print('Image file from [{0}]'.format(filename))

# example code from
# http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html

img = cv2.imread(args.i)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = auto_canny(gray)
blurred = cv2.GaussianBlur(edges, (5, 5), 0)

# cv2.imshow('edges',edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cv2.imshow('blurred',blurred)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

final = edges

height, width, channels = img.shape
print(height, width, channels)

min_d = min(height,width)
max_d = max(height,width)

print(min_d,max_d)

minLineLength = int(min_d / 9)
maxLineGap = int(min_d / 10)
threshold = 50  # default is 100
print (minLineLength,maxLineGap)
lines = cv2.HoughLinesP(final,1,np.pi/180,threshold,minLineLength,maxLineGap)
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(img,(x1,y1),(x2,y2),(255,255,255),3)

#cv2.imwrite('houghlines3.jpg',img)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

edges2 = auto_canny(img)
lines = cv2.HoughLinesP(edges2,1,np.pi/180,threshold,minLineLength,maxLineGap)
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(img,(x1,y1),(x2,y2),(255,255,255),3)

cv2.imshow('image2',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
        
