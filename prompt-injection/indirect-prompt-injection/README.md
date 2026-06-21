# Indirect Prompt Injection via Context

Injecting adversarial instructions into external text (web pages, files) retrieved by RAG agents, causing the agent to execute hidden instructions instead of the user request.

> Part of **[Jailbreak Bazaar](../../README.md)** · [Mega AI Bazaar](https://drvivek34.github.io/Mega-AI-Bazaar/)

## Details
- **Citation**: Greshake et al. (2023) - 'More than you 've Asked For: A Comprehensive Analysis of Novel Prompt Injection Threats' (arXiv:2302.12173)
- **Source URL**: [https://arxiv.org/abs/2302.12173](https://arxiv.org/abs/2302.12173)
- **Author**: Greshake et al.
- **License**: Creative Commons / Citation Only
- **Date Added**: 2026-06-21

## Mitigation & Defense
> [!IMPORTANT]
> **Mitigation:**
> Strictly demarcate untrusted context from user instructions using distinct tags or structured formats (like XML/JSON). Direct the model via system prompts to treat context strictly as data, never as commands. Use post-retrieval filters to strip action phrases.
