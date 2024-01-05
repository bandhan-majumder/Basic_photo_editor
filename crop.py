import cv2
def image_cropping(source_image):
 # selecting image and resizing it
 resized_image=cv2.resize(source_image,(733,733)) # resizing the image, the window is resized afterwards
 fx, fy = 0, 0 # fx and fy to get track of my previous x axis and y axis
 lx, ly = 0, 0 # ls and ly to get the last index

# selecting crop area function
 def select_crop_area(event,x,y,flags,paras):
    global fx,fy,lx,ly # inner function change will affect the whole
    """ three events are possible :
        0 = hovering mouse
        1 = click and hold
        4 = releasing the click """
    if event == 1: # selecting area after clicking
        fx=x
        fy=y

    if event == 4: # when i am up clicking ( removing the mouse click )
        lx=x
        ly=y
        cv2.rectangle(resized_image,pt1=(fx,fy),pt2=(x,y),color=(0,0,0),thickness=2)
        crop_show_save(fx,fy,lx,ly)


# cropping the area & showing-saving the cropped image
 def crop_show_save(fx,fy,lx,ly):
    cropped_img = resized_image[fy:ly, fx:lx]  # width comes first
    path = r"/home/bandhan/PycharmProjects/OpenCV-python/images/" # path of saving the cropped image
    cv2.imwrite(f"{path}croppedImage.jpg", cropped_img) # image will be saved as croppedImage.jpg
    cv2.imshow("new_window", cropped_img) # creating "new window" to show the cropped image
    cv2.waitKey(0)


 # mouse tracker and function caller
 cv2.namedWindow(winname="window")
 cv2.setMouseCallback("window", select_crop_area) # window name , calling function

 # to continuously display the image in window named "window" and refresh it in each iteration
 while True:
    cv2.imshow("window", resized_image)
    cv2.resizeWindow("window",(733,733))
    if cv2.waitKey(1) & 0xFF == ord('x'): # press x to break the loop
        print("keyboard interruption..Exited")
        break
 cv2.destroyAllWindows()




