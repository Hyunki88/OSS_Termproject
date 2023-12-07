import cv2
import image_processor
import save_image
import numpy as np

img = image_processor.read_selected_image()    # 이미지 읽기
med_eval = np.median(img)
lower = int(max(0,0.7*med_eval)) #중앙값의 70%의 값이 0보다 작아질경우 0으로 설정
upper = int(min(255, 1.3*med_eval)) #중앙값의 130%값의 255를 넘어가면 255로 설정

dst = cv2.GaussianBlur(img,(3,3,),0,0)
dst = cv2.Canny(dst,lower,upper,3)

cv2.imshow('img', img)
cv2.imshow('dst',dst)
cv2.waitKey()
save_image.save_image(dst)
cv2.destroyAllWindows()
