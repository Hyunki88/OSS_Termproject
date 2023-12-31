import cv2
import image_processor
import save_image

rate = 15               # 모자이크에 사용할 축소 비율 (1/rate)
win_title = 'mosaic'    # 창 제목
img = image_processor.read_selected_image()    # 이미지 읽기
cv2.namedWindow(win_title, cv2.WINDOW_GUI_EXPANDED)
new_width = img.shape[1] // 2
new_height = img.shape[0] // 2
cv2.resizeWindow(win_title, new_width, new_height)
while True:
    x,y,w,h = cv2.selectROI(win_title, img, False) # 관심영역 선택
    if w and h:
        roi = img[y:y+h, x:x+w]   # 관심영역 지정
        roi = cv2.resize(roi, (w//rate, h//rate)) # 1/rate 비율로 축소
        # 원래 크기로 확대
        roi = cv2.resize(roi, (w,h), interpolation=cv2.INTER_AREA)  
        img[y:y+h, x:x+w] = roi   # 원본 이미지에 적용
        cv2.imshow(win_title, img)
    else:
        break

cv2.waitKey()
save_image.save_image(img)
cv2.destroyAllWindows()