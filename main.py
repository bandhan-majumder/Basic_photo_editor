import cv2
import numpy as np
import sys
import crop

# Create a window to display the first original image
def showIMG(image):
 cv2.imshow('window', image) # window name, image name
 cv2.resizeWindow("window", (733, 733))
 cv2.waitKey(0) # Wait for any key press....0 means infinite, the time parameter is in ms here
 cv2.destroyAllWindows()

# converting into a greyscale image
def conver2grey(image):
 image1_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 showIMG(image1_grey)

 """ 
 cvtcolor=convert color
 image1=image i want to convert from colorful to grey scale, cv
 cv2.COLOR_BGR2GRAY = the method i am using to convert it
 """

# removes a particular color
def removeCOLOR(image,i):
    image_new=image
    image_new[:,:,i]=0 # i = 0 means blue, 1 means green and 2 means red
    showIMG(image)

# shows the each color version of image
def showIndivisualColor(image):
    imageBlue=image[:,:,0] # only the blue version of image
    imageGreen=image[:,:,1] # green version
    imageRed=image[:,:,2] # red version
    img_of_3=np.hstack((imageBlue,imageGreen,imageRed))
    # takes a sequence of arrays as its argument and stacks them horizontally to form a new array.
    showIMG(img_of_3)

# resizing image
def resizeIMG(image, new_height, new_width):
    resized_image = cv2.resize(image, (new_width, new_height)) # img i want to resize and the shape in tuple
    showIMG(resized_image)
    print("Image shape: ", resized_image.shape) # if the channel is 3, it maintained all the color properly

# flipping image
def flipIMG(image, n):
    if n==2:
        flip_180=cv2.flip(image, 0)
        flip_horizonatlly=cv2.flip(image,1)
        flip_both=cv2.flip(image,-1)
        new_image=np.hstack((flip_180,flip_horizonatlly,flip_both))
        showIMG(new_image)
        saveIMG(new_image,"flippedimage.jpg")
    elif n>2:
        print("Wrong flipcode. Range should be between -1 to 2 .")
        sys.exit()
    else:
        new_image=cv2.flip(image,n)
        showIMG(new_image)
        saveIMG(new_image,"flippedimage.jpg")

# saving image in path /home/bandhan/PycharmProjects/OpenCV-python/images .. with user desired name.
def saveIMG(image, new_name):
    path=r"/home/bandhan/PycharmProjects/OpenCV-python/images/"
    cv2.imwrite(f"{path}{new_name}.jpg",image) # path, new-image-name



# main program code
path=input("Path of your image : ")
# Load an image
image1 = cv2.imread(path)
image1=cv2.resize(image1,(733,733)) # resizing the image

# converting image1 to grey image
decision=input("Do you want to convert your image into grayscale? y/n : ")
if decision=="y":
 conver2grey(image1)

# # removing color form image
"""removeCOLOR(image1,0) # removing blue color form image 1
removeCOLOR(image1, 1) # removing green color from image2
removeCOLOR(image1, 2) # removing red color from image3
showIndivisualColor(image1)"""

# resizing image
change=input("Do you want to resize the image? y/n : ")
if change == 'y':
    new_height=int(input("Enter the new height: ")) # by default the input is string
    new_width=int(input("Enter the new width: "))
    resizeIMG(image1,new_height,new_width)
else:
    print("Understood.")

# flipping image
change=input("Do you want to flip the image? y/n :")
if change == "y":
    flip_code=int(input("Enter the flip code :- \n -1 for both \n 0 for 180 flip \n 1 for horizontal \n Your Code: "))
    flipIMG(image1,flip_code)
else:
    print("Understood")

# normal cropping
decision=input("Do you want to crop the image ? y/n : ")
if decision.lower() == "y":
 crop.image_cropping(image1)
else:
 print("Understood")

# good bye message
print("Thanks user! See you again ..")
