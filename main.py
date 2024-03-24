from PIL import Image
import cv2

#To understand the RGB value according to specific x and y coordinates
def rgb_of_pixel(img_path, x, y):
    im = Image.open(img_path).convert('RGB')
    r, g, b = im.getpixel((x, y))
    a = (r, g, b)
    return a

def Capture_Event(event, x, y, flags, params):
    #if left mouse button pressed
    if event == cv2.EVENT_LBUTTONDOWN:
    #printing the coordinate of the clicked point
        print("Selected Coordinates:",f"({x},{y})")
    # Choose the image and print the rgb values of selected point
        img = "js.png"
        print("Color Code of the Coordinates",rgb_of_pixel(img, x, y))
# Main
if __name__ == "__main__":
    # read the image.
    img = cv2.imread('js.png', 1)
    # Show the image
    cv2.imshow('image', img)
    # the Capture_Event function.
    cv2.setMouseCallback('image', Capture_Event)
    # To close program
    cv2.waitKey(0)
    # Close the picture
    cv2.destroyAllWindows()