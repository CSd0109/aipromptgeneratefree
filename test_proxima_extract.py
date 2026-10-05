import urllib.request
import json
import re

test_urls = [
    'https://proxima.art/prompt/grimdark-mercenary-in-battered-iron-armor',
    'https://proxima.art/prompt/high-fashion-underwater-split-shot-portrait',
    'https://proxima.art/prompt/cinematic-golden-hour-swimwear-editorial'
]

for url in test_urls:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=15) as res:
            html = res.read().decode('utf-8', errors='ignore')
            
            # 1. Title
            title_m = re.search(r'<meta property=\"og:title\" content=\"(.*?)\"', html)
            raw_title = title_m.group(1) if title_m else ''
            title = re.sub(r'\s*—.*$', '', raw_title).strip()
            
            # 2. Image
            img_m = re.search(r'<meta property=\"og:image\" content=\"(.*?)\"', html)
            img_url = img_m.group(1) if img_m else ''
            
            # 3. Model
            model_m = re.search(r'href=[\"\']/prompts/model/([^\"\']+)[\"\'][^>]*>(.*?)</a>', html)
            model_name = model_m.group(2).strip() if model_m else 'Midjourney'
            
            # 4. Categories & tags
            cats = re.findall(r'href=[\"\']/prompts/category/([^\"\']+)[\"\'][^>]*>(.*?)</a>', html)
            tags = [c[1].strip() for c in cats]
            
            # 5. Full prompt text from LD+JSON ImageObject description
            ld_m = re.search(r'<script type=\"application/ld\+json\">(.*?)</script>', html, re.DOTALL)
            prompt_text = ''
            if ld_m:
                try:
                    ld_data = json.loads(ld_m.group(1))
                    for item in ld_data:
                        if item.get('@type') == 'ImageObject' and 'description' in item:
                            prompt_text = item['description']
                            break
                except Exception as e:
                    pass
            
            # Fallback for prompt text from og:description
            if not prompt_text:
                desc_m = re.search(r'<meta property=\"og:description\" content=\"(.*?)\"', html)
                prompt_text = desc_m.group(1) if desc_m else title
            
            # Slug / ID
            slug = url.split('/')[-1]
            prompt_id = f"apg-proxima-{slug}"
            
            print(f"ID: {prompt_id}")
            print(f"Title: {title}")
            print(f"Model: {model_name}")
            print(f"Image: {img_url}")
            print(f"Tags: {tags[:4]}")
            print(f"Prompt length: {len(prompt_text)}")
            print(f"Prompt preview: {prompt_text[:120]}...")
            print("-" * 50)
    except Exception as e:
        print(f"Error on {url}: {e}")
