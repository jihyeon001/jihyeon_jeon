import csv, codecs

filename = "test.csv"
file = codecs.open(filename, "r", "euc_kr")     #텍스트 파일,  r , 인코딩형식
                                                                           
reader = csv.reader(file, delimiter=",")      
for cells in reader:
   print(cells[1], cells[2])