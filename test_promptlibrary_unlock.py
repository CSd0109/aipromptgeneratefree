import urllib.request
import re
import json

# Fetch HTML of quiet-defiance
req = urllib.request.Request('https://www.promptlibrary.space/images/quiet-defiance', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=10) as res:
    html = res.read().decode('utf-8', errors='ignore')

# Search for any string that looks like a prompt description
# "A man in a white shirt sits in a wooden rocking chair holding an open book while resting on a checkered cushion."
# Check imageAltText
m = re.findall(r'\"imageAltText\":\s*\"([^\"]+)\"', html)
print('imageAltText in HTML:', m)

# Let's inspect all keys in the page's Next.js stream
chunks = re.findall(r'self\.__next_f\.push\(\[1,\"(.*?)\"\]\)', html, re.DOTALL)
full = ''.join(chunks).encode('utf-8').decode('unicode_escape', errors='ignore')

# find "imageAltText"
idx = full.find('imageAltText')
if idx != -1:
    print('Context around imageAltText in stream:')
    print(full[max(0, idx-100):min(len(full), idx+500)])
