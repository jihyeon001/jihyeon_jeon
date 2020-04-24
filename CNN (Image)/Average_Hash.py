from PIL import Image
import numpy as np

# 이미지 데이터를 Average Hash로 변환
def average_hash(fname, size = 16): # 파일이름과 사이즈를 변수로 받음
    img = Image.open(fname)         # 이미지 데이터 열기
# pillow를 이용, convert 매개변수가 L - 그레이 스케일, 1 - 이진화 등
    img = img.convert('L')  
    img = img.resize((size, size), Image.ANTIALIAS) # 리사이즈하기
    pixel_data = img.getdata()     # 픽셀 데이터 가져오기
    pixels = np.array(pixel_data)  # Numpy 배열로 변환, 밝은정도를 0~255숫자로
    pixels = pixels.reshape((size, size))  # 2차원 배열로 변환
    avg = pixels.mean()  # 평균구하기
    diff = 1 * (pixels > avg) # 픽셀하나하나를 평균보다 크면 1, 작으면 0로 바꿈
    return diff

# 이진 해시로 변환하기
def np2hash(n):
    bhash = []
    for nl in ahash.tolist():
        sl = [str(i) for i in nl]
        s2 = "".join(sl)
        i = int(s2, 2)  # 이진수를 정수로 변환
        bhash.append("%04x" % i)
    return "".join(bhash)

# Average Hash 출력
ahash = average_hash("test-sushi.jpg")
print(ahash)
print(np2hash(ahash))