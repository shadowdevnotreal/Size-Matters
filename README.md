![Safeimagekit-th-1022288424](https://user-images.githubusercontent.com/43219706/173714284-72763e0b-19e5-4e51-866d-d743e082efc9.jpg)

# Size Matters in image searching. Based off tested variations applied to reverse image searching.

See the Wiki for the full logic of why this works:
https://github.com/shadowdevnotreal/Size-Matters/wiki

NOTE: I am not a good dev and did not create a requirements text or package this properly......but will eventually.

## It Creates the files VERY quickly.

The tool will:
1. Open up your file explorer for you.
2. Take any photo, and convert it into 7 different sizes.
3. Ask you if you need a custom size.
4. Open up Google Image search in your default browser for you.
5. Thank you and self terminate the console.

### To modify the default image sizes:
Go to the code itself and change the numbers only in each of the groups.
You need to make sure to change all the numbers in the sections you make changes or the code will fail.
Here is an example: (50x50 and I want it to default to 1200 x 1200)

(50x50) Original code: img = cv2.imread(file_path, cv2.IMREAD_UNCHANGED) # read image dim = (50, 50) # set dimensions resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA) # resize image cv2.imwrite(os.path.splitext(file_path)[0] + "_50x50" + os.path.splitext(file_path)[1], resized)

(1200x1200) Modified Code img = cv2.imread(file_path, cv2.IMREAD_UNCHANGED) # read image dim = (1200, 1200) # set dimensions resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA) # resize image cv2.imwrite(os.path.splitext(file_path)[0] + "_1200x1200" + os.path.splitext(file_path)[1], resized)

You will get a different "print" message unless you change it there as well. Here is an example: print("Your file has been converted to 50x50(change 1200x1200) and 100x100 and 200x200 and 400x400 and 600x600 and 800x800 and 1000x1000 and Your Custom Selection and is located at: " + os.path.splitext(file_path)[0] + "_100x100" + os.path.splitext(file_path)[1])
