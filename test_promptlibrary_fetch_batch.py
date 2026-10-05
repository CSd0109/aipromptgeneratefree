import urllib.request
import json

url = "https://www.promptlibrary.space/api/prompts?limit=50&page=2"
headers = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=12) as res:
    data = json.loads(res.read().decode('utf-8'))
    print(f"Page 2 items count: {len(data.get('items', []))}")
    print("Page 2 First item:", data.get('items', [])[0]['title'])
