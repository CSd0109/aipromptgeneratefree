import urllib.request
import re
import json
import time
import os
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

with open('/home/dhitalsunil/2prompt-gen/proxima_urls.json', 'r') as f:
    urls = json.load(f)

output_file = '/home/dhitalsunil/2prompt-gen/proxima_scraped_items.json'

# Load existing progress if script is resumed
existing_items = {}
if os.path.exists(output_file):
    try:
        with open(output_file, 'r') as f:
            data = json.load(f)
            for item in data:
                existing_items[item['id']] = item
        print(f"Resuming with {len(existing_items)} already scraped items.")
    except Exception as e:
        print("Starting fresh:", e)

def scrape_single(url):
    slug = url.split('/')[-1]
    prompt_id = f"apg-proxima-{slug}"
    
    if prompt_id in existing_items:
        return existing_items[prompt_id]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    req = urllib.request.Request(url, headers=headers)
    
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=12) as res:
                html = res.read().decode('utf-8', errors='ignore')
                
                # 1. Title
                title_m = re.search(r'<meta property=\"og:title\" content=\"(.*?)\"', html)
                raw_title = title_m.group(1) if title_m else ''
                title = re.sub(r'\s*—.*$', '', raw_title).strip()
                if not title:
                    title = slug.replace('-', ' ').title()

                # 2. Image
                img_m = re.search(r'<meta property=\"og:image\" content=\"(.*?)\"', html)
                thumbnail = img_m.group(1) if img_m else ''
                if not thumbnail or not thumbnail.startswith('http'):
                    return None

                # 3. Model
                model_m = re.search(r'href=[\"\']/prompts/model/([^\"\']+)[\"\'][^>]*>(.*?)</a>', html)
                model = model_m.group(2).strip() if model_m else 'Midjourney'

                # 4. Tags & Categories
                cats = re.findall(r'href=[\"\']/prompts/category/([^\"\']+)[\"\'][^>]*>(.*?)</a>', html)
                raw_tags = [c[1].strip() for c in cats]
                tags = list(dict.fromkeys([model, "Proxima", "Trending", "Photorealistic"] + raw_tags[:5]))

                # 5. Full prompt text
                prompt_text = ""
                # Priority A: "Full prompt:" section
                m_fp = re.search(r'Full prompt:\s*</[^>]+>\s*<[^>]+>(.*?)</', html, re.DOTALL | re.IGNORECASE)
                if m_fp:
                    prompt_text = re.sub(r'<[^>]+>', ' ', m_fp.group(1)).strip()
                
                # Priority B: LD+JSON description
                if not prompt_text:
                    ld_m = re.search(r'<script type=\"application/ld\+json\">(.*?)</script>', html, re.DOTALL)
                    if ld_m:
                        try:
                            ld_data = json.loads(ld_m.group(1))
                            for item in ld_data:
                                if item.get('@type') == 'ImageObject' and 'description' in item:
                                    prompt_text = item['description'].strip()
                                    break
                        except Exception:
                            pass
                
                # Priority C: og:description fallback
                if not prompt_text:
                    desc_m = re.search(r'<meta property=\"og:description\" content=\"(.*?)\"', html)
                    if desc_m:
                        prompt_text = desc_m.group(1).strip()
                
                if not prompt_text:
                    prompt_text = f"Photorealistic 8k render, {title}, detailed lighting, high-contrast atmospheric composition."

                # Clean whitespace
                prompt_text = re.sub(r'\s+', ' ', prompt_text).strip()

                # Aspect ratio: inspect style or default to 1:1 or 3:4
                aspect_ratio = "3:4" if any(k in prompt_text.lower() for k in ["portrait", "editorial", "vertical", "full body", "lookbook"]) else "1:1"

                # Dynamic engagement stats
                views_num = random.randint(18, 95)
                likes_num = round(views_num * random.uniform(0.12, 0.22), 1)

                item = {
                    "id": prompt_id,
                    "title": title,
                    "category": "image",
                    "model": model,
                    "thumbnail": thumbnail,
                    "aspectRatio": aspect_ratio,
                    "prompt": prompt_text,
                    "views": f"{views_num}.{random.randint(1, 9)}K",
                    "likes": f"{likes_num}K",
                    "timestamp": "Verified",
                    "creator": {
                        "name": "Proxima Studio",
                        "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=150&auto=format&fit=crop&q=80",
                        "verified": True
                    },
                    "tags": tags,
                    "suggestedTools": ["proxima", "midjourney", "flux"]
                }
                return item
        except Exception as e:
            time.sleep(0.5)
    return None

print(f"Starting concurrent scraping of {len(urls)} items...")
results = list(existing_items.values())
saved_ids = set(existing_items.keys())

# Run in threads for high speed without overloading
batch_size = 50
counter = 0

with ThreadPoolExecutor(max_workers=12) as executor:
    futures = {executor.submit(scrape_single, u): u for u in urls if f"apg-proxima-{u.split('/')[-1]}" not in saved_ids}
    for f in as_completed(futures):
        res = f.result()
        if res and res['id'] not in saved_ids:
            results.append(res)
            saved_ids.add(res['id'])
            counter += 1
            if counter % 50 == 0:
                print(f"Scraped {len(results)} / {len(urls)} prompts...")
                with open(output_file, 'w') as f_out:
                    json.dump(results, f_out, indent=2)

# Final save
with open(output_file, 'w') as f_out:
    json.dump(results, f_out, indent=2)

print(f"Scraping completed! Total successfully extracted prompts: {len(results)}")
