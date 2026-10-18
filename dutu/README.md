# Dutu

Dutu is a distinct project within this repository. It is a scoping study for a language model for Megrelian (ISO 639-3: xmf), which is also called Mingrelian. It sits beside Asmat, the Georgian model, because Megrelian is written in the same Mkhedruli script and shares much of Georgian's data problem. Decisions for Dutu are made separately from those for Asmat.

## Contents

- [token-cost/](token-cost/): what Megrelian costs on six tokenizers, measured against Georgian and English on the same strings, 18 October 2026.
- The scoping paper, "Towards a Mingrelian LLM", will be added here.

## Starting point

Brief 01 in [../briefs/](../briefs/) lists the Megrelian resources found in September 2026. Mingrelian Wikipedia had 22,176 articles in March 2026. Ilia State University's Megrelian Language Corpus holds 97,691 annotated tokens and can be searched but not downloaded. The Georgian National Corpus has a Megrelian subcorpus of 89,404 words. Common Voice holds about 11.5 validated hours of Mingrelian speech, a figure not yet verified. No language-identification model reliably separates Megrelian from Georgian, so web text labelled Megrelian is probably mixed with Georgian. Brief 01 estimates the open Megrelian text at under 5 million words after filtering.
