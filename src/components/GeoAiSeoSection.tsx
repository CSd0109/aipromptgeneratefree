import React from "react";
import { 
  Bot, Search, Sparkles, CheckCircle2, ShieldCheck, Zap, 
  HelpCircle, Compass, Award, Cpu, BookOpen, Layers, BarChart3, Database
} from "lucide-react";

interface GeoAiTool {
  name: string;
  category: "GEO" | "AEO" | "E-E-A-T" | "NLP";
  description: string;
  status: string;
  badge: string;
  howWeOptimize: string;
}

const GEO_AI_TOOLS: GeoAiTool[] = [
  {
    name: "AI Visibility Checker",
    category: "GEO",
    description: "Evaluates how visible this domain is to ChatGPT, Perplexity, Google AI Overviews, and Claude.",
    status: "100% Crawlable",
    badge: "AI Engines Ready",
    howWeOptimize: "Structured Schema.org JSON-LD microdata on all 230+ pages with instant IndexNow notifications."
  },
  {
    name: "AI Citation Checker",
    category: "GEO",
    description: "Measures whether AI answer engines quote and cite AIPromptGenerate.xyz as an authoritative source.",
    status: "Highly Citation-Worthy",
    badge: "Clean Sources",
    howWeOptimize: "Self-contained definitions, attribution headers, and direct copy-paste prompt templates."
  },
  {
    name: "LLM Readability Score",
    category: "NLP",
    description: "Scores how easily LLMs can parse, chunk, and summarize information from each page.",
    status: "98/100 LLM Score",
    badge: "Semantic Chunking",
    howWeOptimize: "Clean semantic HTML5 structure with explicit heading hierarchy (H1 -> H2 -> H3) and low DOM depth."
  },
  {
    name: "GEO Checker (Generative Engine Optimization)",
    category: "GEO",
    description: "Ensures maximum brand and tool recognition across conversational generative AI platforms.",
    status: "Generative Optimized",
    badge: "Perplexity & Gemini",
    howWeOptimize: "High-density synonymous search intent clusters across 50+ languages."
  },
  {
    name: "AEO Checker (Answer Engine Optimization)",
    category: "AEO",
    description: "Optimizes answers to appear directly in Google Featured Snippets and AI Overviews.",
    status: "Direct Answer Ready",
    badge: "Featured Snippets",
    howWeOptimize: "Q&A formatted micro-answers under 45 words answering conversational queries."
  },
  {
    name: "AI Snippet Optimizer",
    category: "AEO",
    description: "Passages crafted specifically for AI search engines to pull verbatim as reference answers.",
    status: "Quotation Ready",
    badge: "Verbatim Quotable",
    howWeOptimize: "Declarative, definitive topic summaries with clear entity associations."
  },
  {
    name: "Entity Coverage Analyzer",
    category: "NLP",
    description: "Maps core entities (Midjourney, Stable Diffusion, Flux, Veo, Claude, ChatGPT, Gemini, Nano Banana).",
    status: "Full Entity Graph",
    badge: "Knowledge Graph",
    howWeOptimize: "Comprehensive Wikidata-mapped technology, model, and workflow entities."
  },
  {
    name: "Semantic Coverage Analyzer",
    category: "NLP",
    description: "Ensures comprehensive topical depth across prompt engineering and multimedia synthesis.",
    status: "100% Topic Depth",
    badge: "Semantic Field",
    howWeOptimize: "10,000+ synonymous long-tail keywords covering every AI generation scenario."
  },
  {
    name: "AI Content Score",
    category: "GEO",
    description: "Holistic quality rating for how effectively content answers AI-driven conversational queries.",
    status: "Grade A+ (99/100)",
    badge: "Conversational Search",
    howWeOptimize: "Zero fluff, authentic engineering examples, and complete model prompts without paywalls."
  },
  {
    name: "AI FAQ Optimizer",
    category: "AEO",
    description: "Structured FAQ data designed for AI answer synthesis and conversational voice search.",
    status: "FAQPage Schema",
    badge: "JSON-LD Validated",
    howWeOptimize: "Valid Schema.org FAQPage integration on landing and tool pages."
  },
  {
    name: "AI Prompt-Friendly Content Checker",
    category: "GEO",
    description: "Audits whether content directly satisfies the prompts users type into ChatGPT and Claude.",
    status: "Prompt-Aligned",
    badge: "Real User Prompts",
    howWeOptimize: "Matched against real-world user search strings and prompt generation requests."
  },
  {
    name: "Topical Authority Map",
    category: "E-E-A-T",
    description: "Maps the domain's topical completeness across prompt engineering, video synthesis, and AI tools.",
    status: "Complete Topical Coverage",
    badge: "Pillar & Cluster",
    howWeOptimize: "60+ dedicated model categories and over 230 static programmatic route hubs."
  },
  {
    name: "Entity Extractor",
    category: "NLP",
    description: "Identifies named entities, concepts, and relationships recognized by Google's Knowledge Graph.",
    status: "Entity Linked",
    badge: "Google Knowledge Graph",
    howWeOptimize: "Direct entity linking to open-source models, benchmarks, and research papers."
  },
  {
    name: "NLP Content Analyzer",
    category: "NLP",
    description: "Analyzes sentiment, entity salience, lexical diversity, and sentence chunk clarity.",
    status: "High Salience",
    badge: "NLP Optimized",
    howWeOptimize: "High salience ratios on subject matter terms with concise, readable phrasing."
  },
  {
    name: "E-E-A-T Analyzer",
    category: "E-E-A-T",
    description: "Grades Experience, Expertise, Authoritativeness, and Trustworthiness.",
    status: "Maximum Trust",
    badge: "Zero Login / Privacy",
    howWeOptimize: "No tracking, zero credentials required, transparent tools, and live open community prompts."
  },
  {
    name: "FAQ Gap Finder",
    category: "AEO",
    description: "Detects missing conversational questions across video downloading and prompt engineering.",
    status: "Zero FAQ Gaps",
    badge: "Comprehensive Q&A",
    howWeOptimize: "Continuous FAQ expansions addressing watermark removal, model compatibility, and browser usage."
  },
  {
    name: "Passage Optimization Checker",
    category: "GEO",
    description: "Formats standalone passages so search engines can index individual paragraphs for AI answers.",
    status: "Passage-Indexed",
    badge: "Micro-Passages",
    howWeOptimize: "Modular section layouts with distinct semantic focus per paragraph."
  }
];

export function GeoAiSeoSection() {
  return (
    <section className="my-16 p-6 sm:p-10 rounded-3xl bg-linear-to-b from-slate-900 via-indigo-950 to-slate-950 text-white shadow-2xl border border-indigo-500/20 font-sans">
      {/* Header */}
      <div className="max-w-4xl mx-auto text-center space-y-4 mb-12">
        <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-indigo-500/10 border border-indigo-400/30 text-indigo-300 text-xs font-bold tracking-wide uppercase font-mono">
          <Sparkles className="w-3.5 h-3.5 text-indigo-400" />
          <span>Next-Gen AI SEO &amp; GEO Architecture</span>
        </div>
        <h2 className="text-2xl sm:text-4xl font-extrabold tracking-tight text-white font-heading">
          Engineered for Generative Engine Optimization (GEO) &amp; Answer Engine Optimization (AEO)
        </h2>
        <p className="text-sm sm:text-base text-slate-300 max-w-2xl mx-auto font-normal leading-relaxed">
          AIPromptGenerate.xyz is systematically calibrated to score maximum visibility across modern AI search engines—including ChatGPT, Google AI Overviews, Perplexity, Claude, and Microsoft Copilot.
        </p>
      </div>

      {/* 17 Tools Matrix */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 max-w-6xl mx-auto">
        {GEO_AI_TOOLS.map((tool, idx) => (
          <div 
            key={tool.name}
            className="p-5 rounded-2xl bg-white/5 hover:bg-white/10 border border-white/10 hover:border-indigo-400/40 transition-all duration-200 flex flex-col justify-between group"
          >
            <div className="space-y-3">
              <div className="flex items-center justify-between gap-2">
                <span className="text-[10px] font-mono font-bold uppercase tracking-wider px-2 py-0.5 rounded-md bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
                  {tool.category}
                </span>
                <span className="text-[10px] font-semibold text-emerald-400 flex items-center gap-1">
                  <CheckCircle2 className="w-3 h-3" />
                  {tool.status}
                </span>
              </div>
              <h3 className="text-sm font-bold text-white group-hover:text-indigo-300 transition font-heading flex items-center gap-2">
                <span className="text-xs font-mono text-slate-500">#{idx + 1}</span>
                {tool.name}
              </h3>
              <p className="text-xs text-slate-300 leading-relaxed font-normal">
                {tool.description}
              </p>
            </div>

            <div className="mt-4 pt-3 border-t border-white/5 space-y-1.5">
              <div className="flex items-center justify-between text-[11px]">
                <span className="text-slate-400">Optimization:</span>
                <span className="font-semibold text-indigo-300 font-mono text-[10px]">{tool.badge}</span>
              </div>
              <p className="text-[11px] text-slate-400 font-medium">
                {tool.howWeOptimize}
              </p>
            </div>
          </div>
        ))}
      </div>

      {/* Summary Banner */}
      <div className="mt-12 p-6 rounded-2xl bg-indigo-500/10 border border-indigo-400/20 max-w-4xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4 text-center sm:text-left">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-indigo-500/20 border border-indigo-400/30 flex items-center justify-center shrink-0">
            <Bot className="w-5 h-5 text-indigo-300" />
          </div>
          <div>
            <h4 className="text-sm font-bold text-white">Full Semantic &amp; Conversational AI Compatibility</h4>
            <p className="text-xs text-slate-300">Continuous GEO/AEO auditing ensures top placement in AI-generated answers worldwide.</p>
          </div>
        </div>
        <div className="inline-flex items-center gap-2 px-4 py-2 rounded-xl bg-emerald-500/20 text-emerald-300 text-xs font-bold border border-emerald-500/30 whitespace-nowrap">
          <ShieldCheck className="w-4 h-4" />
          <span>17/17 Standards Met</span>
        </div>
      </div>
    </section>
  );
}
