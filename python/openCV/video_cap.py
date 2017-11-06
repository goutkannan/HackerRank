import numpy as np

import cv2

cap = cv2.VideoCapture(0) #Call for web cam '0' default one




def show_cam(cap):
    while True:
     ret, frame = cap.read()
     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

     cv2.imshow('frame', gray)
     if cv2.waitKey(1) & 0xFF == ord('q') or cv2.waitKey(1) & 0xFF == 27:
         break
    
    return 

def write_from_cam(cap):
    """
    Function to open web cam and save the recording
    """
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('G:\output.avi',fourcc, 20.0, (640,480))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            #frame = cv2.flip(frame,0)

            # write the flipped frame
            out.write(frame)

            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q') or cv2.waitKey(33) == 27:
                break
        else:
            break

    out.release()






#show_cam(cap)

write_from_cam(cap)


cap.release()
cv2.destroyAllWindows() 
