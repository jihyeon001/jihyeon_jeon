import json

json_str = """
[
      { "name" : "사과", "price" : 1000},
      { "name" : "바나나", "price" : 2000},
      { "name" : "배", "price" : 3000},
      { "name" : "귤", "price" : 4000},
      { "name" : "자두", "price" : 5000}     
] """

output = json.loads(json_str)                  #문자열 -> 파이썬 자료형
print(type(output))
print()

text = json.dumps(output)                      #파이썬 자료형 -> 문자열
print(type(text)) 
