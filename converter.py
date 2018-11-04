import numpy as np
from PIL import Image

# Change this to 1 if you want to invert the grey-scale values
invert_color = 0

# these the characters used to create the image, grey intensity increases towards right
point = ['`','.',',','^',':','-','~','+','*','?','@','%','#','$']

def scaleImage(image):
    if image.size[0] > image.size[1]:
        basewidth = 150
        height = (int)((basewidth / image.size[0]) * image.size[1])
        image = image.resize((basewidth, height), Image.ANTIALIAS)
    else:
        height = 90
        basewidth = (int)((height / image.size[1]) * image.size[0])
        image = image.resize((basewidth, height), Image.ANTIALIAS)

    return image

# keep your image path here
image = Image.open("original-images/boycart.jpg", "r")

# converting rgb image to grey-scale
image = image.convert('L')

# scaling image to smaller size
scaledimage = scaleImage(image)

# converting image to a matrix of grey values
mat=np.asarray(scaledimage.getdata(),dtype=np.int16).reshape((scaledimage.size[1],scaledimage.size[0]))

print(mat)

# this string contains the new image
newimage = ""

for i in range(0,mat.shape[0]):
    for j in range(0,mat.shape[1]):
        if invert_color:
            newimage += (point[int( mat[i][j] / 19)])
        else:
            newimage+=(point[int((255-mat[i][j])/19)])
    newimage+='\n'

# print the new image to console
print(newimage)