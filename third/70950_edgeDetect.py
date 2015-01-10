# from matplotlib import pyplot as plt
import cv2
import numpy as np
from colorsys import hsv_to_rgb
from glob import glob


def calc(img):
    hsl = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsl], [1], None, [256], [0,256])
    hist = [(512/(i+1))*h for i,h in enumerate(hist[220:255])]
    print(sum(hist))
    return sum(hist)

for fpath in glob("./*.jpg"):
# for fpath in ["samolot01.jpg"]:
    img = cv2.imread(fpath)
    tmp = img.copy()
    # while calc(tmp) > 5000:
    #     tmp = cv2.multiply(tmp, np.array([0.8]))
    tmp = cv2.GaussianBlur(tmp, (5,5), sigmaX=1.4, sigmaY=1.4)

# tmp = cv2.Canny(tmp, 100, 40)
    thr = cv2.cvtColor(tmp, cv2.COLOR_BGR2GRAY)

    high_thresh, thresh_im = cv2.threshold(thr, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    lowThresh = 0.5*high_thresh
    tmp  = thr
    # tmp = cv2.bilateralFilter(thr, 11, 11, 11)
    tmp = cv2.Canny(tmp, lowThresh, high_thresh)

    tmp = cv2.dilate(tmp, np.ones((2,2)), iterations=4)
    (cnts, _) = cv2.findContours(tmp.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    final = img
    i = len(cnts)
    print "s"
    for i, c in enumerate(cnts):
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.1 * peri, True)
        print peri
        if peri < 400.0:
            continue
        # if our approximated contour has four points, then
        # we can assume that we have found our screen
        # if len(approx) > 14:
        #     continue
        cv2.drawContours(final, [c], -1, tuple([a*255 for a in hsv_to_rgb(0.1 + 0.9*float(i)/float(len(cnts)), 1, 1)]), 4)
        m = cv2.moments(c)
        x = int(m['m10']/m['m00'])
        y = int(m['m01']/m['m00'])
        cv2.circle(final, (x, y), 8,(255,255,255), -1, 8)
    # cv2.imwrite("detected/" + fpath, final)
    final = cv2.resize(final, (200,200))
    cv2.imshow("as", final)
    cv2.waitKey(0)




#
# element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
# element = np.ones((5, 5), np.uint8)
#
# plt.imshow(img)
# plt.show()
