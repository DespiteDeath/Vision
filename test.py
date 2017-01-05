import numpy as np
import cv2
import sys
from PIL import ImageGrab
import pytesseract
import textract                     #you may delete this string
import fileinput                    #you may delete this string
from matplotlib import lines        #you may delete this string

img = ImageGrab.grab(bbox=(10, 1015, 685, 1125)) #510, 440, 1050, 487(for card) #x, y, w, h 5, 505, 340, 555 could be changed for your window size

img_np = np.array(img)

frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

cv2.imshow("frame", frame)          #you may delete this string

img.save("screen_capture.png", "PNG")    #.save("screen_capture.png", "PNG")

#Deleting "Dealer: "
sys.stdout=open("test.txt","w")
print (pytesseract.image_to_string(img))
sys.stdout.close()

infile = "test.txt"
outfile = "test_cleaned.txt"

delete_list = ["Dealer: "]
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()
####################

sys.stdout.close()

cv2.waitKey(0)
cv2.destroyAllWindows()


#pytesseract.image_to_string(ImageGrab.open('screen_capture.png'))

#sys.stdout.write(pytesseract.image_to_string("screen_capture.png","PNG"))