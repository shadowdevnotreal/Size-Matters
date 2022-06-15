# File: Size Matters.py
# Author: Slow_One
# Date: 2022-06-14

import os
import sys
import time
import random
import tkinter as tk
from tkinter import filedialog
from PIL import Image
import cv2
import webbrowser
import win32gui
import win32con
hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

print("""
     _           __  __       _______ _______ ______ _____   _____ _ 
     (_)         |  \/  |   /\|__   __|__   __|  ____|  __ \ / ____| |
  ___ _ _______  | \  / |  /  \  | |     | |  | |__  | |__) | (___ | |
 / __| |_  / _ \ | |\/| | / /\ \ | |     | |  |  __| |  _  / \___ \| |
 \__ \ |/ /  __/ | |  | |/ ____ \| |     | |  | |____| | \ \ ____) |_|
 |___/_/___\___| |_|  |_/_/    \_\_|     |_|  |______|_|  \_\_____/(_)
""")

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

print_slow("Another Slow Production. ")
print()
print()
print()
print()

# greet user and ask for name

name = input("What is your name? ")
# greet user
print("Hello, " + name + "!")

# ask user for file location
print("Where is your file located? ")

# open file explorer and select file
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

# show dimensions of current image
image = Image.open(file_path)
print("Your image is currently " + str(image.size[0]) + "x" + str(image.size[1]) + ".")

# convert image to width 100, height 100 and save as new file
print("Let's convert your file to different sizes.")
print("Converting...")

# 50x50
img = cv2.imread(file_path, cv2.IMREAD_UNCHANGED) # read image
dim = (50, 50) # set dimensions
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA) # resize image
cv2.imwrite(os.path.splitext(file_path)[0] + "_50x50" + os.path.splitext(file_path)[1], resized)

print('Resized Dimensions : ', resized.shape)

# 100x100
img = cv2.imread(file_path, cv2.IMREAD_UNCHANGED) # read image
dim = (100, 100) # set dimensions
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA) # resize image
cv2.imwrite(os.path.splitext(file_path)[0] + "_100x100" + os.path.splitext(file_path)[1], resized)

print('Resized Dimensions : ', resized.shape)

# 200x200
img = cv2.imread(file_path, cv2.IMREAD_UNCHANGED) # read image
dim = (200, 200) # set dimensions
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA) # resize image
cv2.imwrite(os.path.splitext(file_path)[0] + "_200x200" + os.path.splitext(file_path)[1], resized)

print('Resized Dimensions : ', resized.shape)

# 400x400
img = cv2.imread(file_path, cv2.IMREAD_UNCHANGED) # read image
dim = (400, 400) # set dimensions
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA) # resize image
cv2.imwrite(os.path.splitext(file_path)[0] + "_400x400" + os.path.splitext(file_path)[1], resized)

print('Resized Dimensions : ', resized.shape)

# 600x600
img = cv2.imread(file_path, cv2.IMREAD_UNCHANGED) # read image
dim = (600, 600) # set dimensions
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA) # resize image
cv2.imwrite(os.path.splitext(file_path)[0] + "_600x600" + os.path.splitext(file_path)[1], resized)

print('Resized Dimensions : ', resized.shape)

# 800x800
img = cv2.imread(file_path, cv2.IMREAD_UNCHANGED) # read image
dim = (800, 800) # set dimensions
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA) # resize image
cv2.imwrite(os.path.splitext(file_path)[0] + "_800x800" + os.path.splitext(file_path)[1], resized)

print('Resized Dimensions : ', resized.shape)
# 1000x1000
img = cv2.imread(file_path, cv2.IMREAD_UNCHANGED) # read image
dim = (1000, 1000) # set dimensions
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA) # resize image
cv2.imwrite(os.path.splitext(file_path)[0] + "_1000x1000" + os.path.splitext(file_path)[1], resized)

print('Resized Dimensions : ', resized.shape)

# ask user if they need a custom size image
custom = input("Do you need a custom size image? (y/n) ")

if custom == "y":
    print("What size do you need?")
    width = input("Width: ")
    height = input("Height: ")
    img = cv2.imread(file_path, cv2.IMREAD_UNCHANGED) # read image
    dim = (int(width), int(height)) # set dimensions
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA) # resize image
    cv2.imwrite(os.path.splitext(file_path)[0] + "_" + width + "x" + height + os.path.splitext(file_path)[1], resized)

    print('Resized Dimensions : ', resized.shape)

if custom == "n":
    print("Okay.")

print("Done!")
print("Your file has been converted to 50x50 and 100x100 and 200x200 and 400x400 and 600x600 and 800x800 and 1000x1000 and Your Custom Selection and is located at: " + os.path.splitext(file_path)[0] + "_100x100" + os.path.splitext(file_path)[1])
print("Thank you for using Sizematters!")

input("Press Enter to continue...")

webbrowser.open('https://www.google.com/imghp?hl=en&authuser=0&ogbl=')
exit()
