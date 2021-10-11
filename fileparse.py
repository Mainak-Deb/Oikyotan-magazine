import os
 
# Get the list of all files and directories
path = "D:/Mainak Deb 2019-2021/Documents/Art of code/Oikyotan magazine/images"
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
    
# prints all files
print(dir_list)
content=""
bef='<div ><img src="images/'
aft='" >  </div> \n'

for i in  dir_list:
    parts=bef+i+aft
    content+=parts



with open("D:/Mainak Deb 2019-2021/Documents/Art of code/Oikyotan magazine/divs.html", 'w', encoding='utf-8') as fp:
    fp.write(content)
    fp.close()
  
    pass