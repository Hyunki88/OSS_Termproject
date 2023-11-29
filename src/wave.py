import cv2
import image_processor
import numpy as np
import save_image

l = 20      # 파장(wave length)
amp = 15    # 진폭(amplitude)

img = image_processor.read_selected_image()    # 이미지 읽기
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
img = cv2.resize(img, (580, 400))
img_both = cv2.resize(img_both, (580, 400))

merge_image = cv2.hconcat([img, img_both])
cv2.imshow('wave', merge_image)

cv2.waitKey()
save_image.save_image(img)
cv2.destroyAllWindows()
