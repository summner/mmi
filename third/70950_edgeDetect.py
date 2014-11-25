from matplotlib import pyplot as plt
import cv2
import numpy as np

img = cv2.imread('samolot00.jpg')
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray_image = img
# img = cv2.GaussianBlur(img, (5,5), sigmaX=1.4, sigmaY=1.4)
# img = cv2.Sobel(img, cv2.CV_8U,1,1,ksize=5)
img = cv2.Canny(img, 100, 40)

element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
element = np.ones((5, 5), np.uint8)

# img = cv2.erode(img, element, iterations=1)
# img = cv2.dilate(img, element, iterations=2)
# img = cv2.erode(img, element, iterations=2)
# img = cv2.dilate(img, element, iterations=2)
# img = cv2.erode(img, element, iterations=2)
# img = cv2.dilate(img, element, iterations=2)


# sobel = cv2.erode(sobel, np.)
# cv
# sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
labl = cv2.Laplacian(img, cv2.CV_64F)

# cv2.imshow('asf', sobel)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
plt.imshow(img)
plt.show()
# plt.show()



# from skimage import data
# from matplotlib import pyplot as plt
# image = data.lena() # Albo: coins(), page(), moon()
# io.imshow(image)
# plt.show()