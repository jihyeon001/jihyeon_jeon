csv = """\
p,x,s,n,t,p,f,c,n,k,e,e,s,s,w,w,p,w,o,p,k,s,u
e,x,s,y,t,a,f,c,b,k,e,c,s,s,w,w,p,w,o,p,n,n,g
e,b,s,w,t,l,f,c,b,n,e,c,s,s,w,w,p,w,o,p,n,n,m
p,x,y,w,t,p,f,c,n,n,e,e,s,s,w,w,p,w,o,p,k,s,u
e,x,s,g,f,n,f,w,b,k,t,e,s,s,w,w,p,w,o,e,n,a,g\
"""
splitted = csv.split("\n")          # data seperate
for item in splitted:               
   list_testdata = item.split(",")  # comma seperate
   print(list_testdata[0])
   print(list_testdata[1])
   print(list_testdata[1:4])
   print(list_testdata[2:])         # index2 ~ last
   print(list_testdata[:4])         # first ~ index4
