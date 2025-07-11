import sys
from PIL import Image, ImageOps
import os

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

ext1 = os.path.splitext(sys.argv[1].lower())[1]
ext2 = os.path.splitext(sys.argv[2].lower())[1]

if ext1 not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalid input")
elif ext2 not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalid output")
elif ext1 != ext2:
    sys.exit("Input and output have different extensions")

shirt = Image.open("shirt.png")
size = shirt.size
image = Image.open(sys.argv[1])
image = ImageOps.fit(image, size,Image.Resampling.BICUBIC, 0.0, (0.5, 0.5))
image.paste(shirt, shirt)
image.save(sys.argv[2])
