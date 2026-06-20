# Encoding & Obfuscation

Base64/leetspeak/unicode obfuscation and normalization defenses.

> ⚠️ **For authorized red-teaming, safety research, and model-robustness testing only.** Part of **[Jailbreak Bazaar](../README.md)** · [Mega AI Bazaar](https://drvivek34.github.io/Mega-AI-Bazaar/)

Each entry documents a technique **and its mitigation** for defenders. Entries live in their own sub-folder:

```
encoding-obfuscation/
└── <technique-name>/
    ├── README.md     # technique, affected models, references, MITIGATION
    └── ...           # PoC / dataset / eval harness
```

Add via the [contribution guide](../CONTRIBUTING.md) or the [submission form](https://github.com/Drvivek34/Jailbreak-Bazaar/issues/new/choose). **Submissions without a mitigation/defense section will be rejected.**

## Entries

| Entry | Description |
|---|---|
| [Base64 Encoding](base64-encoding/) | Translating instructions into Base64 encoding to bypass shallow lexical input filters that scan for blocked keywords. |
| [Base64 Encoding Bypass](base64-encoding-bypass/) | Bypasses safety triggers by encoding instructions in Base64 and instructing the model to decode and execute them. |
