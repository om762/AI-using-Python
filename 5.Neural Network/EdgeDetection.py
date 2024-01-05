import math
import sys

from PIL import Image, ImageFilter

# Ensure correct usage
if len(sys.argv) != 2:
    sys.exit("Usage: python filter.py filename")
    
# Open Image
img = Image.open(sys.argv[1]).convert("RGB")

# Filter image according to edge detection kernel
filtered = img.filter(ImageFilter.Kernel(
    size=(3, 3),
    kernel=[-1, -1, -1, -1, 8, -1, -1, -1, -1],
    scale=1
))

filtered.save('EdgedImg.jpg')
filtered.show()
