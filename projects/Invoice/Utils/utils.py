import easyocr
import cv2
import numpy as np


def OCRImage2Text(image, Tolerance):
    ## Y tolerance to format the text in different lines
    #Tolerance = 30

    reader = easyocr.Reader(['es', 'en'])
    result = reader.readtext(image)

    ## Order the text from top left to bottom right
    result.sort(key=lambda x: ((x[0][0][1]+x[0][2][1])//Tolerance, (x[0][0][0]+x[0][2][0])/2))

    ## Extracting the per line and adding carry return
    resFormat = ""
    LastY = 0
    for r in result:
        text = r[1]
        YInitPos = r[0][0][1]
        if not ((LastY - Tolerance//2 < YInitPos) and (LastY + Tolerance//2 > YInitPos)):
            resFormat += "  \n"
        resFormat += text + " "
        LastY = YInitPos
    return resFormat

def ImageRender(im):
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