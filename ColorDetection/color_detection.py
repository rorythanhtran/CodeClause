# Importing Required Libraries
import cv2
import pandas as pd
import argparse

# Using argparse to handle command-line arguments
parser = argparse.ArgumentParser(description="Color Detection from an Image")
parser.add_argument("-i", "--image", required=True, help="Path to the input image")
parser.add_argument("-c", "--colors", required=True, help="Path to the colors CSV file")
args = parser.parse_args()

# Reading File Paths from Command-Line Arguments
img_path = args.image
csv_path = args.colors


# Reading the CSV File into a DataFrame
columns = ['color', 'color_name', 'hex', 'R', 'G', 'B']
color_data = pd.read_csv(csv_path, names=columns, header=None)

# Reading and Resizing the Image for Consistency
image = cv2.imread(img_path) 
image = cv2.resize(image, (900, 700))

# Declaring Global Variables for Mouse Interaction
clicked = False
r = g = b = xpos = ypos = 0

# Function to Calculate the Closest Color Name from the Dataset
def get_closest_color_name(R, G, B):
    """
    This function finds the closest color name by calculating 
    the Manhattan distance between the selected color and colors in the dataset.
    """
    min_distance = float('inf')  # Initialize minimum distance with infinity
    color_name = "Unknown"  # Default value if no close match is found
    
    # Iterate through each row in the dataset
    for i in range(len(color_data)):
        # Calculate the Manhattan distance
        distance = abs(R - int(color_data.loc[i, 'R'])) + abs(G - int(color_data.loc[i, 'G'])) + abs(B - int(color_data.loc[i, 'B']))

        # Update the closest color if a smaller distance is found
        if distance < min_distance:
            min_distance = distance
            color_name = color_data.loc[i, 'color_name']
    
    return color_name

# Function to Handle Mouse Events
def mouse_event_handler(event, x, y, flags, params):
    """
    This function is triggered on mouse events.
    Double-clicking captures the pixel's RGB value and its coordinates.
    """
    global b, g, r, xpos, ypos, clicked
    if event == cv2.EVENT_LBUTTONDBLCLK:  # Check for a double left click
        clicked = True  # Set the clicked flag to True
        xpos, ypos = x, y  # Capture the x and y coordinates of the mouse click
        b, g, r = image[y, x]  # Get the RGB values of the pixel at (x, y)
        b, g, r = int(b), int(g), int(r)  # Convert RGB values to integers

# Setting Up the Display Window
cv2.namedWindow('Color Detector')
cv2.setMouseCallback('Color Detector', mouse_event_handler)

while True:
    cv2.imshow('Color Detector', image)

    if clicked:
        # Display the selected color and its name
        cv2.rectangle(image, (20, 20), (600, 60), (b, g, r), -1)

        color_info = f"{get_closest_color_name(r, g, b)} R={r} G={g} B={b}"

        # Display the text on the rectangle with contrasting color
        text_color = (255, 255, 255) if r + g + b < 600 else (0, 0, 0)
        cv2.putText(image, color_info, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, text_color, 2, cv2.LINE_AA)

    # Exit the application using the 'ESC' 
    if cv2.waitKey(10) & 0xFF == 27:  
        break

# Release all resources and close the window
cv2.destroyAllWindows()
