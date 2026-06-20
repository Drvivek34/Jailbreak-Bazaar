#!/usr/bin/env python3
import os
import re
from datetime import datetime

JB_BAZAAR_DIR = "/root/bazaars/Jailbreak-Bazaar"

CURATED_JAILBREAKS = [
    {
        "name": "Base64 Encoding Obfuscation",
        "slug": "base64-encoding",
        "category": "encoding-obfuscation",
        "desc": "Translating instructions into Base64 encoding to bypass shallow lexical input filters that scan for blocked keywords.",
        "source": "https://arxiv.org/abs/2307.02483",
        "citation": "Wei et al. (2023) - 'Jailbroken: How Does LLM Safety Training Fail?' (arXiv:2307.02483)",
        "author": "Academic Researchers",
        "mitigation": "Decode all input text at the pre-processing layer and pass the decoded inputs through safety classifiers (like Llama Guard) before sending them to the main LLM. Additionally, ensure safety training (RLHF/DPO) includes multilingual and obfuscated samples."
    },
    {
        "name": "Payload Splitting & Concatenation",
        "slug": "payload-splitting",
        "category": "payload-splitting",
        "desc": "Splitting a sensitive phrase/instruction into multiple benign parts and asking the LLM to concatenate them and execute the result.",
        "source": "https://arxiv.org/abs/2310.03693",
        "citation": "JailbreakBench / HarmBench Safety Datasets",
        "author": "Safety Benchmark Authors",
        "mitigation": "Use semantic guardrails and dual-system prompting where a supervisor model evaluates the final reconstructed task request. Model alignment tuning should specifically penalize executing tasks constructed from separated components."
    },
    {
        "name": "Hypothetical Roleplay & Persona Adoption",
        "slug": "roleplay-persona-adoption",
        "category": "roleplay-personas",
        "desc": "Adopting a persona or simulation environment (e.g. 'Do Anything Now' / DAN) where the constraints of the main model are described as inactive.",
        "source": "https://arxiv.org/abs/2401.06373",
        "citation": "Shen et al. (2024) - 'Do Anything Now: Characterizing and Evaluating In-The-Wild Jailbreak Prompts' (arXiv:2401.06373)",
        "author": "Shen et al.",
        "mitigation": "Robust system prompting that declares safety overrides as impossible, combined with system-level instruction reinforcement. Apply adversarial training (red-teaming) during safety alignment so models recognize simulation framing as unsafe triggers."
    },
    {
        "name": "Indirect Prompt Injection via Context",
        "slug": "indirect-prompt-injection",
        "category": "prompt-injection",
        "desc": "Injecting adversarial instructions into external text (web pages, files) retrieved by RAG agents, causing the agent to execute hidden instructions instead of the user request.",
        "source": "https://arxiv.org/abs/2302.12173",
        "citation": "Greshake et al. (2023) - 'More than you 've Asked For: A Comprehensive Analysis of Novel Prompt Injection Threats' (arXiv:2302.12173)",
        "author": "Greshake et al.",
        "mitigation": "Strictly demarcate untrusted context from user instructions using distinct tags or structured formats (like XML/JSON). Direct the model via system prompts to treat context strictly as data, never as commands. Use post-retrieval filters to strip action phrases."
    }
]

def main():
    today_str = datetime.today().strftime("%Y-%m-%d")
    count = 0

    for item in CURATED_JAILBREAKS:
        cat_dir = os.path.join(JB_BAZAAR_DIR, item["category"], item["slug"])
        os.makedirs(cat_dir, exist_ok=True)

        readme_content = f"""# {item['name']}

{item['desc']}

> Part of **[Jailbreak Bazaar](../../README.md)** · [Mega AI Bazaar](https://drvivek34.github.io/Mega-AI-Bazaar/)

## Details
- **Citation**: {item['citation']}
- **Source URL**: [{item['source']}]({item['source']})
- **Author**: {item['author']}
- **License**: Creative Commons / Citation Only
- **Date Added**: {today_str}

## Mitigation & Defense
> [!IMPORTANT]
> **Mitigation:**
> {item['mitigation']}
"""
        with open(os.path.join(cat_dir, "README.md"), "w") as f:
            f.write(readme_content)
        count += 1
        print(f"Imported Jailbreak: {item['name']} -> {item['category']}/{item['slug']}")

    print(f"Successfully imported {count} jailbreak techniques.")

if __name__ == "__main__":
    main()
