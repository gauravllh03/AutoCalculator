import cv2
import numpy as np
import pytesseract
from PIL import Image
import pyautogui
import time
cap = cv2.VideoCapture(0)
while(True):
    ret, image =cap.read()
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    ret,image= cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
    cv2.imshow("Capturing",image)
    key=cv2.waitKey(1)
    results =pytesseract.image_to_string(gray)
    if results:
        break
    
cap.release()
cv2.destroyAllWindows()
print(results)
