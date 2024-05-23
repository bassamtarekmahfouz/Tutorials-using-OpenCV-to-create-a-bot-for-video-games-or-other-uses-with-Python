# Item Detection

This Python script utilizes computer vision techniques to detect items in a real-time window environment. It's particularly useful for scenarios where objects need to be identified and labeled within a graphical user interface.

## Libraries Used

- **OpenCV (cv2)**: 
- **Win32 GUI (win32gui, win32ui, win32con)**:

## Color Thresholds

- `ItemsLow` and `ItemsHigh`: These tuples define the lower and upper bounds of a specific color range. These thresholds are used to identify items based on their color characteristics.

## Functions

1. **`DrowItems(img)`**: This function draws rectangles and adds text annotations to detected items on the input image (`img`). 
    - It iterates over each detected item, draws a rectangle around it, and adds a descriptive label next to it.

2. **`Get_Items(img, low, high)`**: This function detects items in the input image (`img`) by applying color thresholding.
    - It creates a binary mask based on the specified color thresholds.
    - Contours are then extracted from the mask, and bounding rectangles are calculated for each contour.
    - Detected items are represented as instances of the `Item` class and stored in the `Items` list.

3. **`main()`**: The main function of the script.
    - It initializes the title of the window to be captured.
    - Enters a loop to continuously capture the window content, detect items, annotate them, and display the annotated image.
    - The loop exits when the 'q' key is pressed.

## Execution

- Upon execution, the `main()` function is invoked.
- The script continuously captures the specified window, detects items, annotates them, and displays the annotated image in real-time.
- Pressing the 'q' key terminates the script.

Note: The script's functionality is not limited to any specific application or game and can be adapted to various real-time object detection and annotation tasks.
