![Safeimagekit-th-1022288424](https://user-images.githubusercontent.com/43219706/173714284-72763e0b-19e5-4e51-866d-d743e082efc9.jpg)

# Size Matters in image searching. Based off tested variations applied to reverse image searching.
See the full article below.

NOTE: I am not a good dev and did not create a requirements text or package this properly......but will eventually.

The tool will:
1. Open up your file explorer for you.
2. Take any photo, and convert it into 7 different sizes.
3. Ask you if you need a custom size.
4. Open up Google Image search in your default browser for you.
5. Thank you and self terminate the console.

To do:
1. Change default sizes to known standards.
2. Open up each image in a new browswer tab.
3. Place them in a folder vs desktop.
4. Change the auto label placed by Google that affects the image search as well.

## To modify the default image sizes:
1. Go to the code itself and change the numbers only in each of the groups.
2. You need to make sure to change all the numbers in the sections you make changes or the code will fail.

**Here is an example:**
**(50x50 and I want it to default to 1200 x 1200)**

**(50x50) Original code:**
img = cv2.imread(file_path, cv2.IMREAD_UNCHANGED) # read image
dim = (50, 50) # set dimensions
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA) # resize image
cv2.imwrite(os.path.splitext(file_path)[0] + "_50x50" + os.path.splitext(file_path)[1], resized)

**(1200x1200) Modified Code**
img = cv2.imread(file_path, cv2.IMREAD_UNCHANGED) # read image
dim = (1200, 1200) # set dimensions
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA) # resize image
cv2.imwrite(os.path.splitext(file_path)[0] + "_1200x1200" + os.path.splitext(file_path)[1], resized)

**You will get a different "print" message unless you change it there as well.**
**Here is an example:**
print("Your file has been converted to 50x50(change 1200x1200) and 100x100 and 200x200 and 400x400 and 600x600 and 800x800 and 1000x1000 and Your Custom Selection and is located at: " + os.path.splitext(file_path)[0] + "_100x100" + os.path.splitext(file_path)[1])

### Help improve reverse image searching - Because apparently, size matters!

#### Jake Crepes mentioned in a post by:
Irina Shamaeva Twitter = @braingain:
(Full Article Below if you get bored)

Reverse Image Search is a favorite way to find online traces of someone by their social profile photo.

But if you search by image on Google, you may be missing some results. Here is why and how to overcome that.

#1. When you upload an image, Google (annoyingly) shows its “explanations” – sometimes even offensive – like “hair loss.” For my friend @Infosourcer‘s Twitter profile picture in two different dimensions, it decides on “wildlife biologist” on one and “leisure” on the other. (Who needs this feature as it is?)
The “explanation” keywords is not an “innocent” addition, though – they affect your reverse image search.

Change the automatically appeared keywords to something meaningless – just “a” would work – to stop the results from being filtered. Or change them to the person’s name (or other terms) to “guide” the search.

#2. Did you notice how, in the example above, Google’s “approach” to searching by the same image in different sizes is inconsistent – it interprets the images differently? (Also note that “Find other sizes of this image” that you may see, as in the screenshot above, usually finds little.)

Searching by the same image from different sites or in different sizes often produces complementary results.

Let me demonstrate that using my business partner David’s LinkedIn profile photo as an example.
If I search by the profile photo, I find LinkedIn and a few other sites, including our CSE book on Amazon – but not the Twitter profile (which has the same picture).

But if I resize David’s LinkedIn photo to 200×200 pixels (as above) using a simple image editor, new results show up – including Twitter! If I search by the 200×200 image from Twitter, results vary again.

Summary for reverse image search on Google:

1. Remove or change Google’s guess
2. Use different image dimensions and the same image from different sites to uncover more results.

Bonus point –

How to see a LinkedIn photo without a frame

Some LinkedIn profile photos have #opentowork or #hiring frames. For reverse image search, these “stand in the way.” Images on public profiles have no frames, but LinkedIn often would not let you open the profiles without logging in. There are fun ways to see an incognito profile, such as view it with Google Mobile-Friendly Test.

But to find the image only, you can X-Ray the person’s profile in images, like so:

site:linkedin.com/in/[username] imagesize:200×200.


https://booleanstrings.com/2021/07/27/dimensions-of-reverse-image-search/
