import openpyxl
workbook = openpyxl.Workbook()  #work북 만들기
sheet = workbook.active         #활성화 된 파일 불러오기

sheet["A1"] = "테스트 파일"    #데이터 쓰기
sheet["A2"] = "안녕"            
sheet.merge_cells("A1:C1")    #병합하고 가운데 맞춤
sheet["A1"].font = openpyxl.styles.Font(size=20,color="FF0000")   #폰트설정

workbook.save("newFile.xlsx")