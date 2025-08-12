from tkinter import *                                                   # Import all classes and functions from the tkinter module for GUI creation
from PIL import ImageTk, Image                                          # Import ImageTk and Image classes from the PIL (Pillow) library for image handling
import os                                                               # Import the os module for interacting with the operating syst

def rotate_image():                                                     # Define a function to rotate (change) the displayed image
    global counter                                                      # Declare counter as a global variable to keep track of the current image index
    img_label.config(image=img_array[counter % len(img_array)])         # Update the image displayed in img_label using the current index
    counter = counter + 1                                               # Increment the counter to point to the next image

counter = 1                                                             # Initialize the counter to 1 (the first image will be displayed)

root = Tk()                                                             # Create the main application window
root.title("Wallpaper")                                                 # Set the title of the window
root.geometry("400x400")                                                # Set the dimensions of the window to 400x400 pixels
root.configure(bg="black")                                              # Set the background color of the window to black

files = os.listdir(r"D:\New folder")                                    # List all files in the specified directory
img_array = []                                                          # Initialize an empty list to store the images
for files in files:                                                     # Iterate over each file in the directory
    img = Image.open(os.path.join(r"D:\New folder", files))             # Open the image file
    resize_img = img.resize((200, 200))                                 # Resize the image to 200x200 pixels
    img_array.append(ImageTk.PhotoImage(resize_img))                    # Convert the resized image to a PhotoImage and add it to the img_array

img_label = Label(root, image=img_array[0])                             # Create a label to display the first image in img_array
img_label.pack(pady=(15, 10))                                           # Pack the label into the window with some padding

next_btn = Button(root, text="Next", bg='white', fg='black', command=rotate_image)  # Create a button to go to the next image
next_btn.pack(pady=(10, 50))                                            # Pack the button into the window with some padding
root.mainloop()                                                         # Start the main event loop to run the application
