import os

import cv2

import easyocr

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

reader = easyocr.Reader(['ch_sim', 'en'])  # this needs to run only once to load the model into memory
img = cv2.imread('./examples/chinese.jpg')

result = reader.readtext(img)
print(result)

#将结果中的检测框渲染到图片上去
color = (0, 0, 255)
thick = 3
for res in result:
    print(res)
    pos = res[0]
    text = res[1]
    for p in [(0, 1), (1, 2), (2, 3), (3, 0)]:
        cv2.line(img, pos[p[0]], pos[p[1]], color, thick)
cv2.imwrite('bx-road-poetry.jpg', img)
