import sys

import cv2
import imutils
import pytesseract
import data_search

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract'
plate = ''
buf = 0
image = cv2.imread(sys.argv[1])

while(plate == ''):
        buf = buf + 1

        try:
                image = imutils.resize(image, width=500)
                cv2.waitKey(0)
                gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                cv2.destroyAllWindows()
                gray_image = cv2.bilateralFilter(gray_image, 11, 17, 17)
                edged = cv2.Canny(gray_image, 30, 200)
                cnts, new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
                image1 = image.copy()
                cv2.drawContours(image1, cnts, -1, (0, 255, 0), 3)
                cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]
                screenCnt = None
                image2 = image.copy()
                cv2.drawContours(image2, cnts, -1, (0, 255, 0), 3)
                i = 7
                for c in cnts:
                        perimeter = cv2.arcLength(c, True)
                        approx = cv2.approxPolyDP(c, 0.018 * perimeter, True)
                        if len(approx) == 4:
                                screenCnt = approx
                                x, y, w, h = cv2.boundingRect(c)
                                new_img = image[y:y + h, x:x + w]
                                cv2.imwrite('./' + 'plate' + '.png', new_img)
                                i += 1
                                break
                cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 3)
                cv2.waitKey(0)
                Cropped_loc = './plate.png'
                plate = pytesseract.image_to_string(Cropped_loc, lang='eng')
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                image = cv2.imread('plate.png')

        except:
                x = 1

        if buf > 7:
                break

print("Number plate is:", plate)
if(plate != ''):
        try:
                s = list(plate)
                while(s[-1] == '\n'):
                        s.pop(-1)
                plate = "".join(s)
                x = data_search.SQL_request("SELECT plate_number, active FROM plates WHERE plate_number = '{}'".format(plate))
                if (x[0] == plate):
                        if (x[1] == 1):
                                print("Opening gate")
                        else:
                                print("Car is not active")

                else:
                        print("Car is not in database")
        except:
                print("Cannot connect with database")



