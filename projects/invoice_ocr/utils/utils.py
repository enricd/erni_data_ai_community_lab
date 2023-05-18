import cv2
import pytesseract

def Checkandrotate(image):
    results = pytesseract.image_to_osd(image, output_type=pytesseract.Output.DICT)
    if(results['orientation'] == 90):
        imrot =  cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    elif(results['orientation'] == 180):
        imrot =  cv2.rotate(image, cv2.ROTATE_180)
    elif(results['orientation'] == 270):
        imrot =  cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)        
    else:
        imrot = image
    return imrot