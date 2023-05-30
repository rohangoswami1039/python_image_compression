import os
import sys
from PIL import Image

list_image=[]
print("Image quality is between 1 to 100")
print()
qua=int(input("Enter the quality of the image: ")) 
for i in os.listdir('.'):
    exten=os.path.splitext(i)[1]
    if exten=='.jpeg' or exten=='.JPEG' or exten=='.png' or exten=='.PNG'or exten=='.jpg'or exten=='.JPG': 
        picture = Image.open(i) 
        picture.save("Compressed_"+i,  
                     "JPEG",  
                     optimize = True,  
                     quality = qua)


        print(i,"  ","Image Compressed")
        print()
 
