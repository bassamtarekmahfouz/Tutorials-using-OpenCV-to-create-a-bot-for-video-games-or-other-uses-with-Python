import cv2
import numpy as np

def nothing(x):
    pass

# Read the image
path = "PATH"
img = cv2.imread(path)

# Convert BGR image to HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Create trackbars for HSV
cv2.namedWindow("Trackbars")
cv2.createTrackbar("Hue Min", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("Hue Max", "Trackbars", 19, 255, nothing)
cv2.createTrackbar("Sat Min", "Trackbars", 110, 255, nothing)
cv2.createTrackbar("Sat Max", "Trackbars", 240, 255, nothing)
cv2.createTrackbar("Val Min", "Trackbars", 153, 255, nothing)
cv2.createTrackbar("Val Max", "Trackbars", 255, 255, nothing)

while True:
    # Get current trackbar positions
    h_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
    s_min = cv2.getTrackbarPos("Sat Min", "Trackbars")
    s_max = cv2.getTrackbarPos("Sat Max", "Trackbars")
    v_min = cv2.getTrackbarPos("Val Min", "Trackbars")
    v_max = cv2.getTrackbarPos("Val Max", "Trackbars")

    # Create a numpy array for lower and upper bounds
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    # Create a mask
    mask = cv2.inRange(img_hsv, lower, upper)

    # Show the original image, HSV image, and mask
    cv2.imshow("Image", img)
    cv2.imshow("Image HSV", img_hsv)
    cv2.imshow("Image Mask", mask)

    # Wait for key press
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# Close all windows
cv2.destroyAllWindows()
