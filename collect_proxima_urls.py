import urllib.request
import re
import json

urls = []
for page in [1, 2]:
    sitemap_url = f"https://proxima.art/sitemap.xml?page={page}"
    req = urllib.request.Request(sitemap_url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=20) as res:
            xml = res.read().decode('utf-8', errors='ignore')
            locs = re.findall(r'<loc>(https://proxima\.art(?:/en)?/prompt/[^<]+)</loc>', xml)
            # standardize without /en/
            standardized = [l.replace('/en/prompt/', '/prompt/') for l in locs]
            urls.extend(standardized)
            print(f"Page {page} collected: {len(standardized)} prompt URLs")
    except Exception as e:
        print(f"Error on page {page}: {e}")

# Deduplicate preserving order
seen = set()
unique_urls = []
for u in urls:
    if u not in seen:
        seen.add(u)
        unique_urls.append(u)

print(f"Total Unique Proxima Prompt URLs: {len(unique_urls)}")
with open('/home/dhitalsunil/2prompt-gen/proxima_urls.json', 'w') as f:
    json.dump(unique_urls, f, indent=2)
print("Saved to proxima_urls.json")
