import cv2  # Importing OpenCV library
import win32gui, win32ui, win32con  # Importing required libraries for Windows GUI
from WindowCapture import WindowCapture  # Importing WindowCapture class from WindowCapture module

Items = []  # Empty list to store detected items

class Item:
    def __init__(self, rect, x, y):
        self.rect = rect
        self.x = x
        self.y = y

# Define low and high HSV color thresholds for detecting items
ItemsLow = (0, 255, 116)
ItemsHigh = (0, 255, 127)

# Function to draw rectangles and annotate items on the image
def DrowItems(img):
    if Items:
        for i ,Item in enumerate(Items):
            print(Item.rect)
            # Draw a rectangle around the detected item
            if Item.rect[2] * Item.rect[3] > 125 and Item.rect[2] * Item.rect[3] < 135:
                print(f'Get {len(Items)} items ')
                cv2.rectangle(img, (Item.rect[0] - 10, Item.rect[1] - 20),
                              (Item.rect[0] + 70, Item.rect[1] + 130), (0, 255, 0), 2)
                # Add text annotation "Item" near the detected item
                cv2.putText(img, f'Item{i}',
                            (Item.rect[0]-13, Item.rect[1]-25),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            (0, 0, 255),
                            2,
                            cv2.LINE_AA)

# Function to find items in the image using color thresholding
def Get_Items(img, low, high):
    mask = cv2.inRange(img, low, high)  # Create a binary mask based on the color thresholds
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # Find contours in the mask

    if contours:  # If contours are found
        for i, contour in enumerate(contours):
            rect = cv2.boundingRect(contour)  # Get the bounding rectangle of each contour
            Items.append(Item(rect, rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))  # Add the item to the Items list
    else:
        print("Not Found Any Items")

# Main function to capture the window, detect and annotate items, and display the output
def main():
    title_window = 'Conquer Online - Dragon`s Ascension'  # Window title to capture

    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Check for 'q' key press to exit
            break

        target = WindowCapture(title_window)  # Capture the window content
        background = target.copy()  # Create a copy of the captured content
        target = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)  # Convert the captured content to HSV color space

        Get_Items(target, ItemsLow, ItemsHigh)  # Detect items in the captured image
        DrowItems(background)  # Annotate items on the background image
        Items.clear()  # Clear the Items list for the next iteration
        cv2.imshow("output", background)  # Display the annotated image
        key = cv2.waitKey(30)  # Wait for key press

if __name__ == "__main__":
    main()  # Execute the main function if the script is run directly
