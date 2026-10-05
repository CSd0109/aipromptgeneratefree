import json
import re

# Load proxima scraped items
with open('/home/dhitalsunil/2prompt-gen/proxima_scraped_items.json', 'r') as f:
    proxima_items = json.load(f)

print(f"Loaded {len(proxima_items)} Proxima prompts.")

# User's Rule 1: "suru ma ti images show hunwxan jun aile 10% trending ra daily life ma kam lagne xan ra manxe le badi khojxan"
# High-demand / everyday keywords: portrait, fashion, editorial, product, selfie, aesthetic, travel, streetwear, jewelry, landscape, sunset, cinematic
priority_keywords = [
    "portrait", "editorial", "fashion", "headshot", "cinematic", "beauty", 
    "street", "lifestyle", "nature", "landscape", "photography", "aesthetic"
]

def score_item(item):
    text = (item['title'] + " " + " ".join(item['tags']) + " " + item['prompt']).lower()
    score = 0
    for kw in priority_keywords:
        if kw in text:
            score += 1
    # also slightly favor higher views
    try:
        views_val = float(item['views'].replace('K', ''))
        score += views_val * 0.01
    except:
        pass
    return score

# Sort Proxima items so the top trending / daily-life useful 10% are right at the front!
sorted_proxima = sorted(proxima_items, key=score_item, reverse=True)
print(f"Top 5 Proxima Prompts sorted by trending priority:")
for i in range(5):
    print(f"  {i+1}. {sorted_proxima[i]['title']} ({sorted_proxima[i]['model']}) - Tags: {sorted_proxima[i]['tags'][:3]}")

# Read existing data.ts
with open('/home/dhitalsunil/2prompt-gen/src/lib/data.ts', 'r') as f:
    content = f.read()

# Locate SAMPLE_PROMPTS = [
match = re.search(r'export const SAMPLE_PROMPTS: PromptItem\[\] = \[\s*', content)
if not match:
    print("Could not find SAMPLE_PROMPTS declaration!")
    exit(1)

start_idx = match.end()

# Prepare JSON string for proxima items (without outer brackets)
proxima_json_str = ",\n".join(json.dumps(it, indent=2) for it in sorted_proxima) + ",\n"

# Check if any proxima items already in data.ts to avoid duplicates
existing_ids = set(re.findall(r'\"id\":\s*\"(apg-proxima-[^\"]+)\"', content))
if existing_ids:
    print(f"Already found {len(existing_ids)} proxima items in data.ts. Filtering out...")
    filtered_proxima = [it for it in sorted_proxima if it['id'] not in existing_ids]
    if not filtered_proxima:
        print("All proxima items already merged!")
        exit(0)
    proxima_json_str = ",\n".join(json.dumps(it, indent=2) for it in filtered_proxima) + ",\n"
    print(f"Appending {len(filtered_proxima)} new proxima items.")
else:
    print(f"Prepending all {len(sorted_proxima)} Proxima prompts to the FRONT of SAMPLE_PROMPTS.")

# Insert at the beginning of SAMPLE_PROMPTS array so they display prominently in the top trending feed!
new_content = content[:start_idx] + proxima_json_str + content[start_idx:]

with open('/home/dhitalsunil/2prompt-gen/src/lib/data.ts', 'w') as f:
    f.write(new_content)

# Verify new count
new_total_ids = re.findall(r'\"id\":\s*\"([^\"]+)\"', new_content)
print(f"SUCCESS! Total prompts now in data.ts: {len(new_total_ids)}")
