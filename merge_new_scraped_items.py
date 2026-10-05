import json

# 1. Load existing prompts from src/lib/prompts.json
with open('/home/dhitalsunil/2prompt-gen/src/lib/prompts.json', 'r') as f:
    existing_prompts = json.load(f)

print(f"Current prompts in database: {len(existing_prompts)}")

# 2. Load newly scraped items (4,312 prompts)
with open('/home/dhitalsunil/2prompt-gen/new_scraped_items.json', 'r') as f:
    new_items = json.load(f)

print(f"Newly scraped prompts to merge: {len(new_items)}")

# User Rule 1: "suru ma ti images show hunwxan jun aile 10% trending ra daily life ma kam lagne xan ra manxe le badi khojxan"
# Daily life & trending priority keywords: portrait, selfie, fashion, casual, street, beach, couple, aesthetic
trending_keywords = [
    "selfie", "portrait", "mirror", "fashion", "street", "casual", 
    "lifestyle", "beach", "bikini", "hoodie", "editorial", "beauty"
]

def get_priority_score(item):
    text = (item['title'] + " " + " ".join(item['tags']) + " " + item['prompt']).lower()
    score = 0
    for kw in trending_keywords:
        if kw in text:
            score += 2
    return score

# Sort new items so the top trending selfies/daily-life portraits are at the top!
sorted_new_items = sorted(new_items, key=get_priority_score, reverse=True)

# Combine: Put top trending items at the very top of the feed!
merged = []
seen_ids = set()

# First add sorted new items
for it in sorted_new_items:
    if it['id'] not in seen_ids:
        merged.append(it)
        seen_ids.add(it['id'])

# Then add existing items
for it in existing_prompts:
    if it['id'] not in seen_ids:
        merged.append(it)
        seen_ids.add(it['id'])

print(f"Total Combined Prompts after deduplication: {len(merged)}")

# Save to src/lib/prompts.json and public/prompts.json
with open('/home/dhitalsunil/2prompt-gen/src/lib/prompts.json', 'w') as f:
    json.dump(merged, f)

with open('/home/dhitalsunil/2prompt-gen/public/prompts.json', 'w') as f:
    json.dump(merged, f)

print("Saved merged prompts successfully to src/lib/prompts.json and public/prompts.json!")
