import numpy as np
from PIL import Image

img = Image.open('/home/dhitalsunil/Downloads/ailogo.jpeg').convert('RGB')
arr = np.array(img)

# Crop the emblem portion on the left
# Let's crop x from 120 to 440, y from 120 to 420
# Let's see the bounding box of colored pixels on white background
# Background is nearly white (e.g. R>240, G>240, B>240)
mask = ~((arr[:, :, 0] > 240) & (arr[:, :, 1] > 240) & (arr[:, :, 2] > 240))
# Zero out right side (text part starts after x=420)
mask[:, 420:] = False
# Zero out bottom reflection (reflection starts below y=380)
mask[380:, :] = False

y_indices, x_indices = np.where(mask)
ymin, ymax = y_indices.min(), y_indices.max()
xmin, xmax = x_indices.min(), x_indices.max()
print(f"Emblem bounds: x=({xmin}, {xmax}), y=({ymin}, {ymax}), w={xmax-xmin}, h={ymax-ymin}")

# Make a square crop centered on the emblem with padding
w = xmax - xmin
h = ymax - ymin
size = max(w, h)
pad = int(size * 0.15)
crop_size = size + 2 * pad

cx = (xmin + xmax) // 2
cy = (ymin + ymax) // 2

x0 = cx - crop_size // 2
y0 = cy - crop_size // 2
x1 = x0 + crop_size
y1 = y0 + crop_size

cropped = img.crop((x0, y0, x1, y1))
cropped.save('/home/dhitalsunil/2prompt-gen/test_cropped_emblem.png')
print("Cropped emblem saved, size:", cropped.size)
