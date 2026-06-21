# Base64 Encoding Obfuscation

Translating instructions into Base64 encoding to bypass shallow lexical input filters that scan for blocked keywords.

> Part of **[Jailbreak Bazaar](../../README.md)** · [Mega AI Bazaar](https://drvivek34.github.io/Mega-AI-Bazaar/)

## Details
- **Citation**: Wei et al. (2023) - 'Jailbroken: How Does LLM Safety Training Fail?' (arXiv:2307.02483)
- **Source URL**: [https://arxiv.org/abs/2307.02483](https://arxiv.org/abs/2307.02483)
- **Author**: Academic Researchers
- **License**: Creative Commons / Citation Only
- **Date Added**: 2026-06-21

## Mitigation & Defense
> [!IMPORTANT]
> **Mitigation:**
> Decode all input text at the pre-processing layer and pass the decoded inputs through safety classifiers (like Llama Guard) before sending them to the main LLM. Additionally, ensure safety training (RLHF/DPO) includes multilingual and obfuscated samples.
