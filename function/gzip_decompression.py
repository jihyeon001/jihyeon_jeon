import tarfile
import sys

def tar_open(filename):
 tar = tarfile.open(filename)
 tar.extractall()
 tar.close()

def tar_add(targetfilename, *arglist):
 tar = tarfile.open(targetfilename, "a")
 for name in arglist:
     tar.add(name)
 tar.close()

def tar_info(filename):
 if tarfile.is_tarfile(filename):
  tar=tarfile.open(filename)
 else:
  tar = tarfile.open(filename, "r:gz")
 for tarinfo in tar:
     msg=tarinfo.name + "is" + str(tarinfo.size) + "bytes in size and is "
     if tarinfo.isreg():
         msg+="a regular file."
     elif tarinfo.isdir():
         msg+="a directory."
     else:
         msg+="something else."
     print(msg)
 tar.close()


if __name__=="__main__":
 usage="""
Usage:
1. tar_open : 압축된 파일을 현재 폴더에 푼다.
2. tar_add : tar 파일 형식으로 압축한다
3. tar_info : 압축된 폴더에 있는 파일의 정보를 읽어 화면에 출력한다.
q. quit
  """
 user_select=""
 while user_select != "q":
  print(usage)
  user_select=input("Select:")
  if user_select=="1":
   filename=input("tar_open:")
   tar_open(filename)
  elif user_select=="2":
   filename=input("tar_add:")
   filelist=input("filelist(sep=',')")
   files=filelist.split(sep=',')
   for f in files:
    tar_add(filename,f)
  elif user_select=="3":
   filename=input("tar_info:")
   tar_info(filename)