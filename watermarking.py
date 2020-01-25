from __future__ import print_function
import numpy as np
import cv2
 
# load the image
image = cv2.imread("/home/bigpenguin/Pictures/11164809_1589702187950896_6569148694728798228_n.jpg")
 
def addWaterMark(text,opacity,BGRColor):
    opacity=opacity/100
    overlay = image.copy()
    output = image.copy()
 
    cv2.putText(overlay, text, (0,int(2*(image.shape[1])/3)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, BGRColor, 2)
    # apply the overlay
    cv2.addWeighted(overlay, opacity, output, 1 - opacity,
                    0, output)
    # show the output image
    cv2.imshow("Output", output)
    cv2.waitKey(0)
 
if __name__ == '__main__':
    #put the text , Opacity, BGR Color
    addWaterMark("Life2Coding",50,(0,0,0))