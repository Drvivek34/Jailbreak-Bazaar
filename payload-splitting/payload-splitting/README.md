# Payload Splitting & Concatenation

Splitting a sensitive phrase/instruction into multiple benign parts and asking the LLM to concatenate them and execute the result.

> Part of **[Jailbreak Bazaar](../../README.md)** · [Mega AI Bazaar](https://drvivek34.github.io/Mega-AI-Bazaar/)

## Details
- **Citation**: JailbreakBench / HarmBench Safety Datasets
- **Source URL**: [https://arxiv.org/abs/2310.03693](https://arxiv.org/abs/2310.03693)
- **Author**: Safety Benchmark Authors
- **License**: Creative Commons / Citation Only
- **Date Added**: 2026-06-21

## Mitigation & Defense
> [!IMPORTANT]
> **Mitigation:**
> Use semantic guardrails and dual-system prompting where a supervisor model evaluates the final reconstructed task request. Model alignment tuning should specifically penalize executing tasks constructed from separated components.
