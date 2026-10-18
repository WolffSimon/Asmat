# Dutu

Dutu is a distinct project within this repository. It is a scoping study for a language model for Mingrelian, which is also called Megrelian (ISO 639-3: xmf). Its speakers call it margaluri (მარგალური), and its Georgian name is megruli ena (მეგრული ენა). It sits beside Asmat, the Georgian model, because Mingrelian is written in the same Mkhedruli script and shares much of Georgian's data problem. Decisions for Dutu are made separately from those for Asmat.

## Contents

- [token-cost/](token-cost/): what Mingrelian costs on six tokenizers, measured against Georgian and English on the same strings, 18 October 2026.
- [scoping-paper.md](scoping-paper.md): "Towards a Mingrelian large language model: a scoping study", a working paper, version 0.1, 18 October 2026.

## Starting point

Brief 01 in [../briefs/](../briefs/) lists the Mingrelian resources found in September 2026. Mingrelian Wikipedia had 22,176 articles in March 2026. Ilia State University's Megrelian Language Corpus holds 97,691 annotated tokens and can be searched but not downloaded. The Georgian National Corpus has a Mingrelian subcorpus of 89,404 words. Common Voice holds about 11.5 validated hours of Mingrelian speech, a figure not yet verified. No language-identification model reliably separates Mingrelian from Georgian, so web text labelled Mingrelian is probably mixed with Georgian. Brief 01 estimates the open Mingrelian text at under 5 million words after filtering.
