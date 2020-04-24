import hashlib

with open("파일이름", "rb") as file:
    string = file.read()
    m = hashlib.md5()
    m.update(string)
    result = m.digest()
    print(result)
# 해시값 b'"\x1c\xfb\xa0:2\xb9Y\xd4\x84l\x1e\xed\x0c\x02\x8f' 얻음
# 크기변환이나, 확장자 변환등이 일어나면 사용 불가