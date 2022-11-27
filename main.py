# Import Modules
import pyautogui
from PIL import ImageGrab, ImageOps
import time

"""NOTE: This is set up for Windows 10 and would need to be adjusted to open on other OS"""
"""NOTE: Sleep times may need to be adjusted depending on your computer speed"""
"""NOTE: This is for a 1440p monitor and would need to be adjusted depending on screen size"""
"""NOTE: This script needs to be ran on the same monitor that chrome will open on if you have more than one monitor"""
"""NOTE: Adjust the constants below depending on your screen"""

# CONSTANTS - Adjust depending on your screen size
DINO = (105, 815, 290, 1010)  # Dino variable with its corner coordinates
# Delta variable to grab the image immediately to the right of the dino image
DELTA_1 = 245
DELTA_2 = 50
# Baseline pixel value for the target cell. This needs to be adjusted based on your screen
BASELINE_SUM = 27080  #


# Function to grab an image of the area just to the right of the dino that is checking for obstacles
def dino_image_grab():
    # Determine the bounding box for ImageGrab.grab
    bounding_box = (DINO[0] + DELTA_1, DINO[1], DINO[2] + DELTA_1, DINO[3] - DELTA_2)
    img = ImageGrab.grab(bbox=bounding_box)  # Grab an image to the right of the dino
    grey_img = ImageOps.grayscale(image=img)  # Grey out the image to work better
    # # This part is commented out but can help troubleshoot the block in front of the dino that the screen is detecting
    # grey_img.save(fp="target.jpg")sum_colors
    # print(dino_image_grab())  # # Use to get the initial BASELINE_SUM CONSTANT and then comment out
    # This will sum up all the pixels into a single number that can be compared to the target
    sum_colors = sum(map(sum, grey_img.getcolors()))
    return sum_colors  # Returns this number sum to be compared to later


# Jump function. It can jump over most obstacles including the birds
def jump():
    pyautogui.keyDown("space")
    time.sleep(.001)
    pyautogui.keyUp("space")
    time.sleep(.001)


# Duck function. Not currently being used in bot but can be adjusted to include
def duck():
    pyautogui.keyDown("down")
    time.sleep(.001)
    pyautogui.keyUp("down")
    time.sleep(.001)


# Function to start playing the game
def play_game():
    while True:
        # If the target image is not the same sum value as the baseline then it will execute the jump command
        if dino_image_grab() != BASELINE_SUM:
            jump()


# Open chrome from search bar. Needs chrome already installed
pyautogui.typewrite(["win"])  # Open search bar on Windows
time.sleep(.5)  # Sleep .5 seconds to allow for search bar to open
pyautogui.typewrite("chrome")  # Type out chrome
time.sleep(1)  # Sleep 1 second to ensure chrome is the selected browser and not searching for it
pyautogui.typewrite(["enter"])  # Hit enter key

# Open the dino game from chrome
time.sleep(1)  # Sleep one second to make sure chrome has opened
pyautogui.typewrite("chrome://dino/")  # Type out address to chrome dino game
pyautogui.typewrite(["enter"])  # Hit enter to open dino game
pyautogui.typewrite(["space"])  # Hit space bar to start the dino game
time.sleep(2)  # Sleep 2 seconds to allow for game to load and move to full screen

# Play the game
play_game()

