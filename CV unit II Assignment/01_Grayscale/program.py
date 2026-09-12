import cv2

img = cv2.imread("input.jpeg")
gray = cv2.imread("input.jpeg", 0)
print("original image:", img.shape)
print("grayscale image:", gray.shape)
cv2.imwrite("output.png", gray)
cv2.waitKey()
cv2.destroyAllWindows()
