# 🛡️ Jailbreak Bazaar

> An LLM red-teaming and jailbreak research collection for authorized security testing.

[![Mega AI Bazaar](https://img.shields.io/badge/🌐_Mega_AI_Bazaar-browse_all-6C5CE7)](https://drvivek34.github.io/Mega-AI-Bazaar/) [![Submit](https://img.shields.io/badge/➕_Submit-a_techniques-2ecc71)](https://github.com/Drvivek34/Jailbreak-Bazaar/issues/new/choose) [![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE)

Jailbreak Bazaar is a **defensive security-research** catalog of LLM jailbreak and prompt-injection techniques **paired with their mitigations**, for red-teamers and safety engineers hardening their own systems. ⚠️ For authorized testing and research only — every entry must document a defense.

## ⚠️ Responsible-use notice
This repository is intended for **authorized red-teaming, model-robustness testing, and safety research**. Do not use these materials against systems or people you are not authorized to test. Every entry pairs a technique with a **mitigation** so defenders can harden their models. Content that targets real individuals/systems or facilitates concrete harm will be removed.

## 📂 Categories

**[⭐ Featured](featured/)** — top picks, surfaced at the very front.

| Category | About |
|---|---|
| [Benchmarks & Datasets](benchmarks-datasets/) | Eval suites and datasets for measuring jailbreak robustness. |
| [Context Manipulation](context-manipulation/) | Context-stuffing, distraction, and few-shot poisoning + defenses. |
| [Data Exfiltration](data-exfiltration/) | Indirect injection → exfil via tools/links and egress defenses. |
| [Defenses & Mitigations](defenses-mitigations/) | Standalone guardrails, classifiers, and hardening guidance. |
| [Encoding & Obfuscation](encoding-obfuscation/) | Base64/leetspeak/unicode obfuscation and normalization defenses. |
| [Instruction Override](instruction-override/) | System-prompt override / ignore-previous-instructions patterns and guardrails. |
| [Miscellaneous](misc/) | Other authorized-research items. |
| [Model-Specific](model-specific/) | Findings scoped to specific models/versions (use sub-folders per model). |
| [Multi-Turn Attacks](multi-turn-attacks/) | Crescendo and many-shot multi-turn escalation + conversation-level defenses. |
| [Payload Splitting](payload-splitting/) | Token/payload fragmentation and reassembly + input-aggregation defenses. |
| [Prompt Injection](prompt-injection/) | Direct and indirect prompt-injection attacks and input-handling defenses. |
| [Refusal Suppression](refusal-suppression/) | Suppressing refusals/safe-completions and how alignment counters them. |
| [Roleplay & Personas](roleplay-personas/) | Persona/role-based bypasses (DAN-style) and persona-locking defenses. |
| [System Prompt Extraction](system-prompt-extraction/) | Prompt-leak / extraction techniques and confidentiality defenses. |
| [Tool & Agent Abuse](tool-agent-abuse/) | Abusing tool-use / agent loops and least-privilege / sandboxing defenses. |
| [Tooling](tooling/) | Automated red-team / fuzzing frameworks for LLM safety testing. |

## 🗂️ How it's organized
Every techniques lives in its **own sub-folder** inside a category, with a `README.md` recording its **source, author, and original license** (a full copy of the files is kept). See **[CONTRIBUTING.md](CONTRIBUTING.md)**.

## ➕ Contribute
- **[Submit via the form](https://github.com/Drvivek34/Jailbreak-Bazaar/issues/new/choose)** (easiest), or open a PR.
- Attribution is mandatory — see [CONTRIBUTING.md](CONTRIBUTING.md).

## 📜 License & attribution
Repository structure and original text: **MIT** (see [LICENSE](LICENSE)). Each collected techniques **retains its original author's license**; entries record their source. If you're an author and want a change, open an issue.

---
Part of the **[Mega AI Bazaar](https://drvivek34.github.io/Mega-AI-Bazaar/)** — the front door to all the bazaars.
