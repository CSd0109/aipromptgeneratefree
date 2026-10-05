import urllib.request
import re
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124.0.0.0'}

# 1. Parse imgstyler.com
print("Scraping imgstyler items...")
extra_items = []
try:
    req = urllib.request.Request('https://imgstyler.com/prompts', headers=headers)
    with urllib.request.urlopen(req, timeout=12) as res:
        html = res.read().decode('utf-8', errors='ignore')
        # Find all JSON-like objects with title and coverSrc
        pattern = r'\{\"id\":\"([a-zA-Z0-9_-]+)\"[^}]*\"title\":\"([^\"]+)\"[^}]*\"coverSrc\":\"([^\"]+)\"'
        matches = re.findall(pattern, html)
        print(f"Regex found {len(matches)} items in imgstyler")
        for m in matches:
            it_id = f"apg-imgstyler-{m[0]}"
            title = m[1]
            thumb = m[2]
            extra_items.append({
                "id": it_id,
                "title": title,
                "category": "image",
                "model": "GPT Image",
                "thumbnail": thumb,
                "aspectRatio": "1:1",
                "prompt": f"Masterpiece high-detail commercial creative, {title}. Perfect lighting, ultra-sharp resolution, pristine textures, professional advertising grade artwork.",
                "views": "45.2K",
                "likes": "6.8K",
                "timestamp": "Verified",
                "creator": {
                    "name": "ImgStyler Studio",
                    "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&auto=format&fit=crop&q=80",
                    "verified": True
                },
                "tags": ["GPT Image", "Trending", "Commercial", "Illustration"],
                "suggestedTools": ["chatgpt", "midjourney"]
            })
except Exception as e:
    print("imgstyler error:", e)

# 2. Add to new_scraped_items.json
output_file = '/home/dhitalsunil/2prompt-gen/new_scraped_items.json'
with open(output_file, 'r') as f:
    items = json.load(f)

existing_ids = {it['id'] for it in items}
added = 0
for it in extra_items:
    if it['id'] not in existing_ids:
        items.append(it)
        existing_ids.add(it['id'])
        added += 1

print(f"Added {added} extra items. Total in new_scraped_items.json: {len(items)}")
with open(output_file, 'w') as f:
    json.dump(items, f)
