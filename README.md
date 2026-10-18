# Asmat

Asmat is a Georgian-language model in design at mAIself. This repository holds the design note and the research behind it. It publishes no model, training data or evaluation items.

## Contents

- [DESIGN.md](DESIGN.md): design considerations for a Georgian language model, version 0.1 of 18 October 2026. It covers the tokeniser, training text and its authorship, training method, evaluation, speech and OCR, and the law, and it ends with the decisions still open.
- [briefs/](briefs/): five research briefs on Kartvelian language resources, token cost by language, tokenisation and language coverage, benchmark methods, and Georgian text sources and licensing. [briefs/README.md](briefs/README.md) explains how they were compiled and where they disagree.
- [dutu/](dutu/): Dutu, a distinct project within this repository, which scopes a model for Megrelian (Mingrelian). It starts with a measurement of what Megrelian costs on six tokenizers.

## Related work

- [WolffSimon/token-premiums](https://github.com/WolffSimon/token-premiums) holds the code and data behind brief 02.

## Licence

The text and data in this repository are released under the Creative Commons Attribution 4.0 International licence; see [LICENSE](LICENSE). The scripts in dutu/token-cost/ are released under the MIT licence; see [LICENSE-CODE](LICENSE-CODE). Copyright 2026 Matthew Wolff Simon. The works cited in the briefs keep their own terms.

Suggested credit: Matthew Wolff Simon, mAIself, "Asmat: design considerations for a Georgian language model", October 2026.

## About

mAIself is an AI assistant that chooses a model for each question by its language and task. Its line is "AI for the next billion". https://maiself.io
