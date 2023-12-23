import os 
import shutil
from_directory="C:/Users/Shubh/Downloads"
to_directory="C:/Users/Shubh/Downloads"
filesList=os.listdir(from_directory)
print(filesList)
for eachFile in filesList:
    name,extension=os.path.splitext(eachFile)
    print(extension,name)
    if extension in [".png",".jpg",".jpeg",".gif"]:
        p1=from_directory+"/"+eachFile
        p2=to_directory+"/"+"pictures"
        p3=to_directory+"/"+"pictures"+"/"+eachFile
        if os.path.exists(p2):
            shutil.move(p1,p3)
        else:
            os.makedirs(p2)
            shutil.move(p1,p3)