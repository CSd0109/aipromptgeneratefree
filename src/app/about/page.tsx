import type { Metadata } from "next";
import Link from "next/link";
import { ArrowLeft, Sparkles, ShieldCheck, Heart, Users, Globe, Zap, CheckCircle2 } from "lucide-react";

export const metadata: Metadata = {
  title: "About Us | AI Prompt Generate - Free AI Prompts & Engineering Studio",
  description:
    "Learn about AI Prompt Generate, our mission to democratize generative AI prompts for creators worldwide, our founding team, and our zero-login open philosophy.",
  alternates: {
    canonical: "https://aipromptgenerate.xyz/about",
  },
  openGraph: {
    title: "About AI Prompt Generate - 100% Free AI Prompt Studio",
    description: "Democratizing prompt engineering with zero barriers, zero fees, and universal AI tool access.",
    url: "https://aipromptgenerate.xyz/about",
    siteName: "AI Prompt Generate",
    type: "website",
    images: [{ url: "/top1_free_ai_studio.jpg", width: 1200, height: 630, alt: "About AI Prompt Generate" }],
  },
};

const jsonLd = {
  "@context": "https://schema.org",
  "@type": "AboutPage",
  "@id": "https://aipromptgenerate.xyz/about#about",
  "name": "About AI Prompt Generate",
  "url": "https://aipromptgenerate.xyz/about",
  "description": "About AI Prompt Generate, the premier 100% free zero-login AI prompt library and generative tools ecosystem.",
  "mainEntity": {
    "@type": "Organization",
    "name": "AI Prompt Generate",
    "url": "https://aipromptgenerate.xyz",
    "logo": "https://aipromptgenerate.xyz/logo-icon.png",
    "founder": {
      "@type": "Person",
      "name": "Sunil Dhital",
      "jobTitle": "Lead AI Engineer & Founder",
      "url": "https://aipromptgenerate.xyz/about",
      "sameAs": [
        "https://twitter.com/dhitalsunil",
        "https://github.com/dhitalsunil"
      ]
    },
    "sameAs": [
      "https://twitter.com/aipromptgen",
      "https://github.com/dhitalsunil/2prompt-gen",
      "https://www.pinterest.com/aipromptgenerate/"
    ]
  }
};

export default function AboutPage() {
  return (
    <div className="min-h-screen bg-[#f8fafc] text-slate-900 flex flex-col font-sans selection:bg-purple-600 selection:text-white">
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
      />

      {/* Header Bar */}
      <header className="sticky top-0 z-30 bg-white/85 backdrop-blur-md border-b border-slate-200/80 px-4 sm:px-8 py-4 flex items-center justify-between shadow-2xs">
        <Link
          href="/"
          className="flex items-center gap-2 text-sm font-semibold text-slate-700 hover:text-[#8054ff] transition"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Back to Home</span>
        </Link>

        <div className="flex items-center gap-3">
          <span className="px-3 py-1 rounded-full text-xs font-bold bg-emerald-50 text-emerald-700 border border-emerald-200">
            100% Free Forever
          </span>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex-1 w-full max-w-4xl mx-auto px-4 sm:px-8 py-12 sm:py-16">
        
        {/* Hero Title */}
        <div className="text-center space-y-4 mb-12">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-purple-100 text-purple-700 text-xs font-bold uppercase tracking-wider">
            <Sparkles className="w-3.5 h-3.5" />
            <span>Our Mission & Story</span>
          </div>
          <h1 className="text-3xl sm:text-5xl font-extrabold text-[#101828] font-heading tracking-tight leading-tight">
            Democratizing AI Prompt Engineering for Everyone
          </h1>
          <p className="text-base sm:text-lg text-slate-600 max-w-2xl mx-auto leading-relaxed">
            AI Prompt Generate was built on a simple principle: high-fidelity generative AI tools should be open, instantaneous, and accessible without sign-up walls or paywalls.
          </p>
        </div>

        {/* Core Values Grid */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-16">
          <div className="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-3">
            <div className="w-10 h-10 rounded-2xl bg-purple-100 text-purple-600 flex items-center justify-center font-bold">
              <Zap className="w-5 h-5" />
            </div>
            <h3 className="text-lg font-bold text-slate-900 font-heading">Zero Login Barrier</h3>
            <p className="text-xs sm:text-sm text-slate-600 leading-relaxed">
              No account creation, no password tracking, and no paywalls. Every generator, converter, and prompt is ready immediately in your browser.
            </p>
          </div>

          <div className="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-3">
            <div className="w-10 h-10 rounded-2xl bg-blue-100 text-blue-600 flex items-center justify-center font-bold">
              <Globe className="w-5 h-5" />
            </div>
            <h3 className="text-lg font-bold text-slate-900 font-heading">Multi-Model Fidelity</h3>
            <p className="text-xs sm:text-sm text-slate-600 leading-relaxed">
              Tested prompt syntaxes specifically tuned for Midjourney v6.1, Flux 1.1 Pro, ChatGPT-4o, Claude 3.5 Sonnet, DeepSeek V3, and Google Veo 3.
            </p>
          </div>

          <div className="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-3">
            <div className="w-10 h-10 rounded-2xl bg-emerald-100 text-emerald-600 flex items-center justify-center font-bold">
              <ShieldCheck className="w-5 h-5" />
            </div>
            <h3 className="text-lg font-bold text-slate-900 font-heading">Privacy & Speed</h3>
            <p className="text-xs sm:text-sm text-slate-600 leading-relaxed">
              All tools run client-side or on ultra-fast edge infrastructure. We do not store your prompts, uploads, or personal data.
            </p>
          </div>
        </div>

        {/* Narrative / About the Team */}
        <section className="bg-white rounded-3xl p-8 sm:p-10 border border-slate-200 shadow-sm space-y-6 mb-12">
          <h2 className="text-2xl sm:text-3xl font-bold text-slate-900 font-heading tracking-tight">
            Who We Are
          </h2>
          <p className="text-sm sm:text-base text-slate-700 leading-relaxed">
            AI Prompt Generate was created in 2025 by software engineer and AI researcher <strong>Sunil Dhital</strong> alongside a collective of visual designers, photographers, and prompt engineers. Frustrated by existing SaaS prompt marketplaces that charge exorbitant monthly fees and lock basic features behind sign-up forms, the team launched AIPromptGenerate as an open, free alternative.
          </p>
          <p className="text-sm sm:text-base text-slate-700 leading-relaxed">
            Today, our platform serves creators, marketing agencies, software engineers, and digital artists across 140+ countries. We curate, test, and release verified prompt formulas daily, providing direct 1-click copy-paste utility for professional production workflows.
          </p>
        </section>

        {/* Official Channels & Entity Links */}
        <section className="bg-slate-900 text-white rounded-3xl p-8 sm:p-10 shadow-xl space-y-6">
          <h2 className="text-2xl font-bold font-heading tracking-tight">
            Connect & Official Profiles
          </h2>
          <p className="text-slate-300 text-sm leading-relaxed">
            Follow our verified official channels for prompt releases, tutorials, and engineering updates:
          </p>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 pt-2">
            <a
              href="https://twitter.com/aipromptgen"
              target="_blank"
              rel="noopener noreferrer"
              className="p-4 rounded-2xl bg-white/10 hover:bg-white/15 border border-white/10 transition block text-center"
            >
              <span className="font-bold text-white text-sm block">𝕏 / Twitter</span>
              <span className="text-xs text-slate-300 mt-1 block">@aipromptgen</span>
            </a>

            <a
              href="https://github.com/dhitalsunil/2prompt-gen"
              target="_blank"
              rel="noopener noreferrer"
              className="p-4 rounded-2xl bg-white/10 hover:bg-white/15 border border-white/10 transition block text-center"
            >
              <span className="font-bold text-white text-sm block">GitHub Repository</span>
              <span className="text-xs text-slate-300 mt-1 block">Open Source Project</span>
            </a>

            <a
              href="https://www.pinterest.com/aipromptgenerate/"
              target="_blank"
              rel="noopener noreferrer"
              className="p-4 rounded-2xl bg-white/10 hover:bg-white/15 border border-white/10 transition block text-center"
            >
              <span className="font-bold text-white text-sm block">Pinterest Studio</span>
              <span className="text-xs text-slate-300 mt-1 block">@aipromptgenerate</span>
            </a>
          </div>
        </section>

        {/* Footer Navigation */}
        <div className="mt-12 pt-8 border-t border-slate-200 text-center text-xs text-slate-500 space-y-2">
          <p>© {new Date().getFullYear()} AI Prompt Generate • Built for Creators Worldwide</p>
          <div className="flex items-center justify-center gap-4 text-slate-600 font-medium">
            <Link href="/" className="hover:text-purple-600">Home</Link>
            <span>•</span>
            <Link href="/free-ai-prompts-tools" className="hover:text-purple-600">Free Tools</Link>
            <span>•</span>
            <Link href="/privacy-policy" className="hover:text-purple-600">Privacy Policy</Link>
            <span>•</span>
            <Link href="/llms.txt" className="hover:text-purple-600">llms.txt</Link>
          </div>
        </div>

      </main>
    </div>
  );
}
