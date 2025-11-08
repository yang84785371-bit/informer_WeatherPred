import cv2

# 读取 PNG 图片
img = cv2.imread('path_to_your_image.png')

# 显示图片
cv2.imshow('Prediction vs True', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
