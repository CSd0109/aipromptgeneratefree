import numpy as np
from PIL import Image

# Load original high-res ailogo.jpeg
img = Image.open('/home/dhitalsunil/Downloads/ailogo.jpeg').convert('RGB')
arr = np.array(img)

# Corner background color
bg = arr[0, 0]
diff = np.sqrt(np.sum((arr.astype(float) - bg.astype(float))**2, axis=2))

mask = diff > 25
# Stop strictly at x=381 to eliminate any dot/letter on the right
mask[:, 381:] = False
mask[374:, :] = False

y_indices, x_indices = np.where(mask)
ymin, ymax = y_indices.min(), y_indices.max()
xmin, xmax = x_indices.min(), x_indices.max()

emblem = img.crop((xmin, ymin, xmax, ymax))

master_size = 512
master = Image.new('RGBA', (master_size, master_size), (255, 255, 255, 255))

ew, eh = emblem.size
max_dim = int(master_size * 0.86)
scale = max_dim / max(ew, eh)
new_w = int(ew * scale)
new_h = int(eh * scale)

resized_emblem = emblem.resize((new_w, new_h), Image.Resampling.LANCZOS)

offset_x = (master_size - new_w) // 2
offset_y = (master_size - new_h) // 2
master.paste(resized_emblem, (offset_x, offset_y))

# Save all favicon formats across public and src/app/
master.save('/home/dhitalsunil/2prompt-gen/public/android-chrome-512x512.png', 'PNG')
master.save('/home/dhitalsunil/2prompt-gen/public/logo-icon.png', 'PNG')
master.save('/home/dhitalsunil/2prompt-gen/src/app/icon.png', 'PNG')

icon_192 = master.resize((192, 192), Image.Resampling.LANCZOS)
icon_192.save('/home/dhitalsunil/2prompt-gen/public/android-chrome-192x192.png', 'PNG')
icon_192.save('/home/dhitalsunil/2prompt-gen/public/icon-192.png', 'PNG')

icon_180 = master.resize((180, 180), Image.Resampling.LANCZOS)
icon_180.save('/home/dhitalsunil/2prompt-gen/public/apple-touch-icon.png', 'PNG')
icon_180.save('/home/dhitalsunil/2prompt-gen/src/app/apple-icon.png', 'PNG')

icon_48 = master.resize((48, 48), Image.Resampling.LANCZOS)
icon_48.save('/home/dhitalsunil/2prompt-gen/public/favicon-48x48.png', 'PNG')

icon_32 = master.resize((32, 32), Image.Resampling.LANCZOS)
icon_32.save('/home/dhitalsunil/2prompt-gen/public/favicon-32x32.png', 'PNG')

icon_16 = master.resize((16, 16), Image.Resampling.LANCZOS)
icon_16.save('/home/dhitalsunil/2prompt-gen/public/favicon-16x16.png', 'PNG')

# Standard ICO with 16, 32, 48
master.save(
    '/home/dhitalsunil/2prompt-gen/public/favicon.ico',
    format='ICO',
    sizes=[(16, 16), (32, 32), (48, 48)]
)

master.save(
    '/home/dhitalsunil/2prompt-gen/src/app/favicon.ico',
    format='ICO',
    sizes=[(16, 16), (32, 32), (48, 48)]
)

print("Saved all icons and updated logo-icon.png!")
