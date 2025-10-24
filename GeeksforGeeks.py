# this code is taken from https://www.geeksforgeeks.org/python/create-a-screen-recorder-using-python/ for learning purposes

# importing the required packages
import pyautogui
# the video thing
import cv2
# OPEN CV for recording
import numpy as np
# the frames and the window
import time

start_time = time.time()
frame_count = 0

# Specify resolution
resolution = (1920, 1080)

# Specify video codec
codec = cv2.VideoWriter_fourcc(*"mp4v")

# Specify name of Output file
filename = "Recording.mp4"

# Specify frames rate. We can choose any 
# value and experiment with it
fps = 45.0


# Creating a VideoWriter object
out = cv2.VideoWriter(filename, codec, fps, resolution)

# Create an Empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# Resize this window
cv2.resizeWindow("Live", 480, 270)

while True:
    # Take screenshot using PyAutoGUI
    img = pyautogui.screenshot()

    # Convert the screenshot to a numpy array
    frame = np.array(img)

    # Convert it from BGR(Blue, Green, Red) to
    # RGB(Red, Green, Blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write it to the output file
    out.write(frame)
    
    # increase frame - issue with sped up video
    frame_count += 1

    # Optional: Display the recording screen
    cv2.imshow('Live', frame)
    
    # Stop recording when we press 'q'
    if cv2.waitKey(1) == ord('j'):
        break

    # fixes sped up video
    elapsed = time.time() - start_time
    expected_time = frame_count / fps
    if expected_time > elapsed:
        time.sleep(expected_time - elapsed)

# Release the Video writer
out.release()

# Destroy all windows
cv2.destroyAllWindows()