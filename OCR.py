from PIL import Image
import pytesseract
import sys 
import pyocr
import pyocr.builders
import cv2

class OCR_class:
    def image_to_text(self,image):
        text = pytesseract.image_to_string(Image.open(image))
        print(text,sep='\n')

        tools = pyocr.get_available_tools()
        tool=tools[0]
        txt = tool.image_to_string(Image.open(image),lang='eng',builder=pyocr.builders.TextBuilder())
        print(txt)
        
class OCR_cv:
    def image_to_string(self,image):
        read_image=cv2.imread(image)
        img_rgb = cv2.cvtColor(read_image, cv2.COLOR_BGR2RGB) 
        print(pytesseract.image_to_string(img_rgb))

        # h,w,c=read_image.shape
        # boxes = pytesseract.image_to_boxes(read_image)
        # for b in boxes.splitlines():
        #     b = b.split(' ')
        #     img = cv2.rectangle(read_image, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

        # cv2.imshow('img',img)
        # cv2.waitKey(0)


if __name__=='__main__':
    # ocr=OCR_class()
    # ocr.image_to_text('/home/bigpenguin/test_image.jpeg')
    ocr2=OCR_cv()
    ocr2.image_to_string('/home/bigpenguin/test_image.jpeg')
