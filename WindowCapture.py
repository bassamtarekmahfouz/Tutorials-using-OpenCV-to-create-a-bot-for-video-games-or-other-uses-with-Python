import pygetwindow as gw
import numpy as np
import mss
import win32gui
import win32ui
import win32con


def WindowCapture(window_title):
    # Get the window handle by its title
    windows = gw.getWindowsWithTitle(window_title)
    if not windows:
        raise Exception(f"No window with title '{window_title}' found")

    window = windows[0]

    # Get the window position and size
    left, top, right, bottom = window.left, window.top, window.right, window.bottom
    width = right - left
    height = bottom - top

    # Ensure the window is not minimized or offscreen
    if width <= 0 or height <= 0:
        raise Exception(f"Window '{window_title}' is minimized or offscreen")

    try:
        # Get device contexts
        hwnd = window._hWnd
        wDC = win32gui.GetWindowDC(hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()

        # Create a bitmap compatible with the device context
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, width, height)
        cDC.SelectObject(dataBitMap)

        # Copy the window's content into the bitmap
        cDC.BitBlt((0, 0), (width, height), dcObj, (left, top), win32con.SRCCOPY)

        # Convert bitmap to numpy array
        bmpstr = dataBitMap.GetBitmapBits(True)
        img = np.frombuffer(bmpstr, dtype='uint8')
        img.shape = (height, width, 4)

    finally:
        # Free resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

    return img