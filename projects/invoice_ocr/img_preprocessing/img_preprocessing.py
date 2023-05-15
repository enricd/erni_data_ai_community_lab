import cv2
import numpy as np

def no_preprocessing(img):
    return img

def Basic_preprocessing(im):
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    imden = cv2.fastNlMeansDenoising(imgray)
    #imgray = cv2.cvtColor(imden, cv2.COLOR_BGR2GRAY)
    imbw = cv2.adaptiveThreshold(imgray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)
    #_, imbw = cv2.threshold(imden, 127, 255, cv2.THRESH_BINARY)
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    # Apply the sharpening kernel to the image using filter2D
    sharpened = cv2.filter2D(imbw, -1, kernel)
    n = np.ones((2, 2), np.uint8)

    #imdil = cv2.erode(imbw, n, iterations=1)
    return sharpened