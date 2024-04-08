
from PIL import Image
import glob
import os

lst_imgs = [i for i in glob.glob("*.png")]

# It creates a folder called ltl if does't exist
if not "happy" in os.listdir():
	os.mkdir("happy")

print(lst_imgs)
for i in lst_imgs:
	img = Image.open(i)
	img = img.resize((176, 220), Image.LANCZOS)
	img.save("happy\\" + i[:-4] + ".png")


print("Done")
os.startfile("happy")
