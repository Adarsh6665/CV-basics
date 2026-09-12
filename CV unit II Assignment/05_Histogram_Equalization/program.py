import cv2
import numpy as np

img = cv2.imread("input.jpg")
greyscale = cv2.imread("input.jpg", 0)
equalized = cv2.equalizeHist(greyscale)

cv2.imwrite("output.jpg", equalized)
