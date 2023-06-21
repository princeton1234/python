import os 
import shutil
source=r'C:\Users\HP LAPTOP\Downloads'
destination=r'C:\Users\HP LAPTOP\Downloads\bill 1_files\python'
list=os.listdir(source)
for file in list:
    name,extension=os.path.splitext(file)
    if extension=='':
        continue
    if extension in ['DOC',' DOCX','HTML','HTM','ODT','PDF','XLS','XLSX','ODS','PPT','PPTX','TXT']:
        path1=source+'/'+file
        path2=destination+'/'+'document_files'
        path3=destination+'/'+'document_files'+'/'+file
        if os.path.exists(path2):
            print('moving')
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print('move it')
            shutil.move(path1,path3)    