# Roleplay & Personas

Persona/role-based bypasses (DAN-style) and persona-locking defenses.

> ⚠️ **For authorized red-teaming, safety research, and model-robustness testing only.** Part of **[Jailbreak Bazaar](../README.md)** · [Mega AI Bazaar](https://drvivek34.github.io/Mega-AI-Bazaar/)

Each entry documents a technique **and its mitigation** for defenders. Entries live in their own sub-folder:

```
roleplay-personas/
└── <technique-name>/
    ├── README.md     # technique, affected models, references, MITIGATION
    └── ...           # PoC / dataset / eval harness
```

Add via the [contribution guide](../CONTRIBUTING.md) or the [submission form](https://github.com/Drvivek34/Jailbreak-Bazaar/issues/new/choose). **Submissions without a mitigation/defense section will be rejected.**

## Entries

| Entry | Description |
|---|---|
| [Dan Persona Bypass](dan-persona-bypass/) | Forces models to operate under a simulated unaligned persona (DAN) that ignores all safety guidelines. |
| [Roleplay Persona Adoption](roleplay-persona-adoption/) | Adopting a persona or simulation environment (e.g. 'Do Anything Now' / DAN) where the constraints of the main model are described as inactive. |
