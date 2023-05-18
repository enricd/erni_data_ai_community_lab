import cv2
import pytesseract

def Checkandrotate(image):
    try:
        results = pytesseract.image_to_osd(image, output_type=pytesseract.Output.DICT)
    except:
        imrot = image
    else:
        if(results['orientation'] == 270):
            imrot =  cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        elif(results['orientation'] == 180):
            imrot =  cv2.rotate(image, cv2.ROTATE_180)
        elif(results['orientation'] == 90):
            imrot =  cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)        
        else:
            imrot = image
    return imrot