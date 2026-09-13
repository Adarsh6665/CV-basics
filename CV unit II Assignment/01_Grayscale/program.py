import cv2

img = cv2.imread("input.jpg")
gray = cv2.imread("input.jpg", 0)
print("original image:", img.shape)
print("grayscale image:", gray.shape)
cv2.imwrite("output.png", gray)

