import openpyxl
book = openpyxl.load_workbook("stats_104102")  #book을 로드

 # book.get 입력 후 sheet등의 여러 메서드 확인
 # 첫번째 방법
 # print(book.get_sheet_names())
 # print(book.get_sheet_by_name('stats_104102'))

 #두번쨰 방법
sheet = book.worksheets[0]     #sheet 로드
for row in sheet.rows:
   for data in row:
      print(data, end=" ")
   print(" ", end="\n")