import cv2
import time

# SET THE COUNTDOWN TIMER
# for simplicity we set it to 3
# We can also take this as input
TIMER = int(5)

# Open the camera
cap = cv2.VideoCapture(0)

while True:

    ret, img = cap.read()
    cv2.imshow('a', img)
    k = cv2.waitKey(125)
    if k == ord('q'):
        prev = time.time()

        while TIMER >= 0:
            ret, img = cap.read()
            print(TIMER)
            if(TIMER==0):
                quit()
            cv2.imshow('a', img)
            cv2.waitKey(125)
            cur = time.time()
            if cur - prev >= 1:
                prev = cur
                TIMER = TIMER - 1

        else:
            ret, img = cap.read()

            # Display the clicked frame for 2
            # sec.You can increase time in
            # waitKey also
            cv2.imshow('a', img)

            # time for which image displayed
            cv2.waitKey(2000)

            # Save the frame
            cv2.imwrite('camera.jpg', img)

            # HERE we can reset the Countdown timer
            # if we want more Capture without closing
            # the camera

    # Press Esc to exit
    elif k == 27:
        break

# close the camera
cap.release()

# close all the opened windows
cv2.destroyAllWindows()