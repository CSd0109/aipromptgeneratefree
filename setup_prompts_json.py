import re
import json

# Read data.ts to extract all objects
with open('/home/dhitalsunil/2prompt-gen/src/lib/data.ts', 'r') as f:
    content = f.read()

# Match the SAMPLE_PROMPTS array definition
m = re.search(r'export const SAMPLE_PROMPTS:\s*any\[\]\s*=\s*(\[\s*\{.*\}\s*\]);', content, re.DOTALL)
if not m:
    # try matching without semicolon
    m = re.search(r'export const SAMPLE_PROMPTS:\s*any\[\]\s*=\s*(\[\s*\{.*\}\s*\])', content, re.DOTALL)

if m:
    raw_array = m.group(1)
    prompts = json.loads(raw_array)
    print(f"Extracted {len(prompts)} prompts from data.ts.")
    
    # Save directly to public/prompts.json and src/lib/prompts.json
    with open('/home/dhitalsunil/2prompt-gen/src/lib/prompts.json', 'w') as f_out:
        json.dump(prompts, f_out)
    print("Saved src/lib/prompts.json")
    
    # Write clean data.ts
    data_ts_code = '''import promptsData from "./prompts.json";

export interface PromptItem {
  id: string;
  title: string;
  category: "image" | "video" | "ui";
  model: string;
  thumbnail: string;
  aspectRatio: string;
  prompt: string;
  negativePrompt?: string;
  systemPrompt?: string;
  views: string;
  likes: string;
  timestamp: string;
  creator: {
    name: string;
    avatar: string;
    verified: boolean;
  };
  tags: string[];
  suggestedTools: string[];
}

export const SAMPLE_PROMPTS: PromptItem[] = promptsData as PromptItem[];

export const AI_MODELS = [
  { id: "all", name: "All Models" },
  { id: "krea-2", name: "Krea 2" },
  { id: "proxima-aurelia-2", name: "Proxima Aurelia 2" },
  { id: "qwen-image-2512", name: "Qwen Image 2512" },
  { id: "ideogram-4", name: "Ideogram 4" },
  { id: "z-image-base", name: "Z-Image Base" },
  { id: "midjourney", name: "Midjourney v6.1" },
  { id: "flux", name: "Flux.1 Schnell" },
  { id: "chatgpt", name: "ChatGPT-4o" },
  { id: "gemini", name: "Gemini 2.5 Flash" },
  { id: "claude", name: "Claude 3.7 Sonnet" },
  { id: "deepseek", name: "DeepSeek R1" },
  { id: "nano-banana", name: "Nano Banana Pro" },
  { id: "veo", name: "Google Veo 3" },
  { id: "seadance", name: "SeaDance 2.2" },
  { id: "sora", name: "Sora Video" }
];
'''
    with open('/home/dhitalsunil/2prompt-gen/src/lib/data.ts', 'w') as f_out:
        f_out.write(data_ts_code)
    print("Updated data.ts cleanly!")
else:
    print("Failed to find SAMPLE_PROMPTS regex match")
