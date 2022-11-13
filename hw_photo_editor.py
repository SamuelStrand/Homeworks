import cv2

value = 'Temp_hw/meme.jpg'

img2 = cv2.imread(value, cv2.IMREAD_COLOR)
cv2.imshow('meme', img2)
cv2.waitKey(0)

image = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

width = int(image.shape[1] * 50 / 100)
height = int(image.shape[0] * 50 / 100)
quality = 50

image = cv2.resize(image, (width, height))


cv2.imwrite("Temp_hw/new_meme.jpg", image, [cv2.IMWRITE_JPEG_QUALITY, quality])

