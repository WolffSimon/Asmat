# Research briefs

These five briefs are the evidence behind [DESIGN.md](../DESIGN.md). Brief 02 is a measurement, and its code and data are public. The other four were compiled with AI research tools from the sources they cite, between September and October 2026, and tidied for publication on 18 October 2026. Each brief's opening paragraph says when it was compiled and what was changed.

| Brief | Subject | Compiled |
|---|---|---|
| [01](01-kartvelian-language-resources.md) | Kartvelian language resources for AI training and Kartvelology: text, speech, OCR and lexical resources for Georgian, Megrelian, Laz and Svan, with sizes, licences, access and contacts | September 2026 |
| [02](02-token-cost-by-language.md) | Token cost by language on five tokenizers, measured on the Universal Declaration of Human Rights | 14 October 2026, rerun 16 October 2026 |
| [03](03-tokenisation-errors-and-coverage.md) | Tokenisation, language errors and language coverage in eleven languages, Georgian among them | 14 October 2026 |
| [04](04-benchmark-methods.md) | Designing and running model benchmarks for languages and cultures | 14 October 2026 |
| [05](05-georgian-text-sources-and-licensing.md) | Georgian text sources, provenance and licensing | 17 and 18 October 2026 |

## Labels

The briefs label each source as peer-reviewed, preprint, vendor claim (dataset and model cards included), practitioner (NGO, media, government or community) or leaderboard. "Secondary" means the source was seen only in a summary or a citing page. Figures marked unverified or secondary were not checked against the primary source and should not be quoted as fact.

## Where the briefs disagree

- **Georgian National Corpus licence.** Brief 01 lists the corpus as CC BY-NC. Brief 05 found no licence on the corpus's own pages, and its CLARINO record says "unspecified". Until the holders state terms, the corpus should be treated as unlicensed for training.
- **Georgian National Corpus size.** A 2024 paper gives "more than 202 million tokens" and a community list gives "~217M words" (brief 05). Brief 01 uses about 200 million tokens.
- **Megrelian Wikipedia.** Brief 01 gives 22,176 articles in March 2026, and brief 05 gives 22,458 from a secondary source in September 2026. The two are consistent with growth.
- **Megrelian Language Corpus licence.** Brief 01 marks it unverified. Brief 05 notes that the eLex 2025 paper names two different licences.
- **Global-MMLU.** Brief 01 first reported, from a secondary source, that Global-MMLU excludes Georgian. Brief 05 confirms this from the Global-MMLU paper (ACL 2025), which lists 42 languages without Georgian, Armenian or Azerbaijani.
