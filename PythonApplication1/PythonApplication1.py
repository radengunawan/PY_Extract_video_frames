## by Eka G
import cv2
import os

print("here is your")
print(os.getcwd())
print("FInish")

'''
import numpy as np
import glob
import matplotlib.pyplot as plt
import skimage.io
import skimage.color
import skimage.filters
import numpy as np
#import argparse
import imutils
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
from pyzbar.pyzbar import decode
from pyzbar import pyzbar
import cv2
import glob
from tqdm import tqdm
from barcode import EAN13
from barcode.writer import ImageWriter

## add video path
video_path = r'D:\Raw_Data\Videos of box\vid_04.mp4'
address_path = 'D:\\Raw_Data\\Videos of box\\'


# Opens the inbuilt camera of laptop to capture video.

cap = cv2.VideoCapture(video_path)

i = 0
while(cap.isOpened()):
    ret, frame = cap.read()

    # This condition prevents from infinite looping
    # incase video ends.
    if ret == False:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    t,bimage = cv2.threshold(gray,160,255,cv2.THRESH_BINARY)
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]], np.float32)
    #kernel = 1/3 * kernel
    image_sharp = cv2.filter2D(src=bimage, ddepth=-1, kernel=kernel)
    barcodes = decode(image_sharp)
    
# Save Frame by Frame into disk using imwrite method
    if (len(barcodes) != 0):
        list_barcodeData = []
        list_barcodeType = []
        for barcode in barcodes:
            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), thickness=2)
            barcodeData = barcode.data.decode("utf-8")
            list_barcodeData.append(barcodeData)
            barcodeType = barcode.type
            list_barcodeType.append(barcodeType)
            
            text = "{} ({})".format(barcodeData, barcodeType)
            cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imwrite(address_path+'Frame'+str(i)+'.jpg', frame)
    i += 1

cap.release()
cv2.destroyAllWindows()
'''




