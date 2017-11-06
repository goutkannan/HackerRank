import numpy as np
import cv2

def edit_img():
    img = cv2.imread(r"C:\Users\Goutham\Documents\GitHub\HackerRank\python\openCV\images_1.jpg",

    cv2.IMREAD_COLOR)

    cv2.line(img, (10,10), (200, 200), (123, 223, 122), 10)
    cv2.rectangle(img, (10,10), (200, 200), (123, 223, 122), 10, 3)
    cv2.putText(img, "FootBall", (70,70), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (123, 223, 122), 2, cv2.LINE_AA)

    cv2.imshow('Title to be shown...', img)



    while True:
        if cv2.waitKey(1) & 0xFF == ord('q') or cv2.waitKey(1) & 0xFF == 27:
            break



    cv2.destroyAllWindows()


def add_img():
    img1 = cv2.imread('img3.png')
    img2 = cv2.imread(r"C:\Users\Goutham\Documents\GitHub\HackerRank\python\openCV\images_1.jpg")

    rows, cols, channels = img2.shape
    roi = img1[0:rows, 0:cols ]

    # Now create a mask of logo and create its inverse mask
    img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

    # add a threshold
    ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

    mask_inv = cv2.bitwise_not(mask)

    # Now black-out the area of logo in ROI
    img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

    # Take only region of logo from logo image.
    img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

    dst = cv2.add(img1_bg,img2_fg)
    img1[0:rows, 0:cols ] = dst

    cv2.imshow('add',img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    add_img()

if __name__ == '__main__':
    main()