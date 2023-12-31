import cv2
import image_processor
import numpy as np
import save_image

l = 20      # 파장(wave length)
amp = 15    # 진폭(amplitude)
win_title = 'wave'

img = image_processor.read_selected_image()    # 이미지 읽기
cv2.namedWindow(win_title, cv2.WINDOW_NORMAL)
new_width = img.shape[1] 
new_height = img.shape[0] // 2
cv2.resizeWindow(win_title, new_width, new_height)
rows, cols = img.shape[:2]

# 초기 매핑 배열 생성 ---①
mapy, mapx = np.indices((rows, cols),dtype=np.float32)

# sin, cos 함수를 적용한 변형 매핑 연산 ---②
sinx = mapx + amp * np.sin(mapy/l)  
cosy = mapy + amp * np.cos(mapx/l)

# 영상 매핑 ---③

img_sinx=cv2.remap(img, sinx, mapy, cv2.INTER_LINEAR) # x축만 sin 곡선 적용
img_cosy=cv2.remap(img, mapx, cosy, cv2.INTER_LINEAR) # y축만 cos 곡선 적용
# x,y 축 모두 sin, cos 곡선 적용 및 외곽 영역 보정
img_both=cv2.remap(img, sinx, cosy, cv2.INTER_LINEAR, \
                    None, cv2.BORDER_REPLICATE)
# 결과 출력


merge_image = cv2.hconcat([img, img_both])
cv2.imshow(win_title, merge_image)

cv2.waitKey()
save_image.save_image(img_both)
cv2.destroyAllWindows()
