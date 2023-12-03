import cv2
import image_processor
import numpy as np
import save_image

win_title = 'lens'
img = image_processor.read_selected_image()    # 이미지 읽기
cv2.namedWindow(win_title, cv2.WINDOW_NORMAL)
new_width = img.shape[1] 
new_height = img.shape[0] // 2
cv2.resizeWindow(win_title, new_width, new_height)
print(img.shape)
rows, cols = img.shape[:2]

# ---① 설정 값 셋팅
exp = 2       # 볼록, 오목 지수 (오목 : 0.1 ~ 1, 볼록 : 1.1~)
scale = 1           # 변환 영역 크기 (0 ~ 1)

# 매핑 배열 생성 ---②
mapy, mapx = np.indices((rows, cols),dtype=np.float32)

# 좌상단 기준좌표에서 -1~1로 정규화된 중심점 기준 좌표로 변경 ---③
mapx = 2*mapx/(cols-1)-1
mapy = 2*mapy/(rows-1)-1

# 직교좌표를 극 좌표로 변환 ---④
r, theta = cv2.cartToPolar(mapx, mapy)

# 왜곡 영역만 중심확대/축소 지수 적용 ---⑤
r[r< scale] = r[r<scale] **exp  

# 극 좌표를 직교좌표로 변환 ---⑥
mapx, mapy = cv2.polarToCart(r, theta)

# 중심점 기준에서 좌상단 기준으로 변경 ---⑦
mapx = ((mapx + 1)*cols-1)/2
mapy = ((mapy + 1)*rows-1)/2
# 재매핑 변환
distorted = cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)



merge_image = cv2.hconcat([img, distorted])
cv2.imshow(win_title, merge_image)

cv2.waitKey()
save_image.save_image(distorted)
cv2.destroyAllWindows()
