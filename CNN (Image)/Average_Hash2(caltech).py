from PIL import Image
import numpy as np 
import os, re

# 파일경로 지정
search_dir = "./image/파일이름"
cache_dir = "./image/파일이름"

if not os.path.exists(cache_dir):
    os.mkdir(cache_dir)

# 이미지 데이터를 Average Hash로 변환
def average_hash(fname, size = 16): 
    fname2 = fname[len(search_dir):]
    # 이미지 캐시하기
    cache_file = cache_dir + "/" + fname2.replace('/', "_") + ".csv"
    if not os.path.exists(cache_file): # 해시생성
        img = Image.open(fname) 
        img = img.convert('L').resize((size, size), Image.ANTIALIAS) # pillow, resize
        #------------------------------------------------
        pixel_data = img.getdata()     
        pixels = np.array(pixel_data)  
        pixels = pixels.reshape((size, size)) 
        # pixels = np.array(img.getdata()).reshape((size, size))  한번에
        avg = pixels.mean()  
        px = 1 * (pixels > avg) 
        np.savetxt(cache_file, px, fmt=".0f", delimiter=",")
    else:
        px = np.loadtxt(cache_file, delimiter=",") # 캐시 돼 있으면 읽지 않기
    return px

# 해밍 거리 구하기
def hamming_dist(a,b):
    aa = a.reshape(1, -1)  # 1차원 배열로 변환
    ab = b.reshape(1, -1)
    dist = (aa != ab).sum()
    return dist

# 모든 폴더에 처리 적용
def enum_all_files(path):




