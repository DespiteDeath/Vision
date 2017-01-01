import numpy as np
import cv2
import sys
from PIL import ImageGrab
import textract         #you may delete this string
import pytesseract



img = ImageGrab.grab(bbox=(10, 1000, 685, 1125)) #x, y, w, h 5, 505, 340, 555 could be changed for your window size
img_np = np.array(img)
frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
cv2.imshow("frame", frame)      #you may delete this string
img.save("screen_capture.png", "PNG")    #.save("screen_capture.png", "PNG")


sys.stdout=open("test.txt","w")
print (pytesseract.image_to_string(img))

sys.stdout.close()
cv2.waitKey(0)
cv2.destroyAllWindows()



#pytesseract.image_to_string(ImageGrab.open('screen_capture.png'))

#sys.stdout.write(pytesseract.image_to_string("screen_capture.png","PNG"))