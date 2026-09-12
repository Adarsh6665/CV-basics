import cv2
import numpy as np

img = cv2.imread("input.jpeg")
brightness = 50
enhanced = np.clip(img.astype(np.int16) + brightness, 0, 255).astype(np.uint8)
x, y = 100, 100
print("Pixel before", img[y, x])
print("Pixel after ", enhanced[y, x])
cv2.imwrite("output.png", enhanced)
