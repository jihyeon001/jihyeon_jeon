# 이미지 데이터를 회전, 반전을 해서 데이터량 추가하기
# 
from PIL import Image
import numpy as np
import os, glob
from sklearn.model_selection import train_test_split

# 분류대상 카테고리 선택
caltech_dir = "./image/101"
categories = ["chair", "camera","butterfly", "elephant", "flamingo"]
nb_classes = len(categories)

# 이미지 크기 지정
image_w = 64
image_h = 64
pixels = image_w * image_h * 3

# 이미지 데이터 읽어 들이기
cnt = 0
flag = False
X = []
Y = []

for idx, cat in enumerate(categories):
    # 레이블 지정
    label = [0 for i in range(nb_classes)]
    label[idx] = 1

    # 이미지
    image_dir = caltech_dir + "/" + cat
    files = glob.glob(image_dir + "/*.jpg")
    for i, f in enumerate(files):
        img = Image.open(f)
        img = img.convert("RGB")
        img = img.resize(image_w, image_h)
        data = np.asarray(img)
        X.append(data)
        Y.append(label)
        if flag == False:
                img.save("./image/" + str(cnt) + ".png")
                cnt += 1
        for angle in range(-20, 20, 5):
            # 회전 데이터 추가
            img2 = img.rotate(angle)
            data = np.asarray(img2)
            X.append(data)
            Y.append(label)
            if flag == False:
                img2.save("./image/" + str(cnt) + ".png")
                cnt += 1
            # 반전 데이터
            img2 = img2.transpose(Image.FLIP_LEFT_RIGHT)
            X.append(data)
            Y.append(label)
            if flag == False:
                img2.save("./image/" + str(cnt) + ".png")
                cnt += 1
X = np.array(X)
Y = np.array(Y)

# 학습, 테스트 데이터 구분
X_train, X_test. Y_train, Y_test = \
    train_test_split(X, Y)
xy = (X_train, X_test. Y_train, Y_test)
np.save("./image/5obj.npy", xy)
print("ok", len(Y))