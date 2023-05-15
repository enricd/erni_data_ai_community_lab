import easyocr
import cv2
import numpy as np


def easyOCRImage2Text(image):

    ## Y tolerance to format the text in different lines
    Tolerance = 30

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




