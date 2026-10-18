# Brief 03: Tokenisation, language errors and language coverage (October 2026)

A literature review covering eleven languages: Modern Standard and Gulf Arabic, Hindi, Urdu, Bengali, Tamil, Malayalam, Nepali, Sinhala, Tagalog and Georgian. Compiled with AI research tools on 14 October 2026. Each claim gives its source, date and one of four labels: peer-reviewed, preprint, vendor claim or leaderboard. "Secondary" means the source was seen only in a summary. Tidied for publication on 18 October 2026: two sections outside the scope of this repository were removed, the section on running tokenisers now points to the measurement in brief 02, and a statement about Global-MMLU was corrected.

## Short answer

For the same content, current tokenisers charge these languages anywhere from a little over English to more than ten times English. Models fail outside English in ways that differ by language. Vendor claims of language support often have no independent measurement behind them. For Georgian in particular, independent evaluation is thin: INCLUDE carries Georgian exam questions, while Global-MMLU does not include Georgian, and the Georgian-first model Kona2 publishes only its developers' own description.

## TL;DR

- **The token gap is large and depends on the model.** On FLORES-200, Llama-3.1's tokeniser uses 16.16 tokens per Malayalam word against 1.24 for English. Gemma-3 uses 3.33 (BrahmicTokenizer-131K preprint, May 2026). Qwen3 needs 4.56 times as many tokens for Hindi as for English, where Gemma 3 needs 1.34 times (Invisible Language Tax preprint, September 2026). Routing by tokeniser efficiency alone can change cost, latency and usable context several-fold for Indic users.
- **Measured quality in these languages is patchy.** Independent evidence exists for Hindi, Bengali, Tamil, Malayalam, Nepali, Sinhala, Urdu, Tagalog/Filipino, Modern Standard Arabic and Georgian, through Global-MMLU, INCLUDE, SEA-HELM and SinhalaMMLU (Georgian through INCLUDE only). For Gulf Arabic the review found no independent current benchmark. For Kona2 (Georgian) and Sarvam-105B's Indic results, the review found only the developers' own figures.

## 1. Tokenisation

### 1.1 Foundational work, verified

- **Petrov, La Malfa, Torr and Bibi, "Language Model Tokenizers Introduce Unfairness Between Languages", NeurIPS 2023 (peer-reviewed; arXiv May 2023).**
  - **Measure:** "premium", the ratio of token counts for the same parallel sentence in two languages. A premium of 1.0 is parity.
  - **Corpus:** FLORES-200.
  - **Findings:**
    - Tokenised lengths of the same content differ by up to 15 times.
    - On the ChatGPT/GPT-4 tokeniser, Italian needs about 1.6 times the tokens of English, Arabic about 3 times, and Shan as much as 15 times.
    - Even the cheapest languages for that tokeniser (Portuguese, Pangasinan, German) pay about 50% more than English.
    - Byte-level and character-level schemes are not fair either: CANINE shows a 4.58 premium and ByT5 3.94.
    - Character-level and byte-level models still show over four-fold differences, and the authors estimate that users of some languages pay at least 2.5 times more than English users for the same task.
- **Ahia et al., "Do All Languages Cost the Same? Tokenization in the Era of Commercial Language Models", EMNLP 2023 (peer-reviewed; Singapore, December 2023).**
  - **Scope:** OpenAI's API tested across 22 typologically diverse languages, measuring both cost and quality.
  - **Main finding, a "double unfairness":** in the authors' words, "speakers of a large number of the supported languages are overcharged while obtaining poorer results".
  - **Size of the gap:** mid-resource Indic languages in non-Latin scripts can cost up to five times as much as English for the same information.
  - **Georgian:** a secondary summary of the paper on alphaXiv lists Georgian, Telugu and Thai among the most expensive languages. The review did not check the exact Georgian multiplier against the PDF.

### 1.2 Published figures since 2023 for current tokenisers

| Language | Tokeniser | Measure | Value | Corpus | Source and label |
|---|---|---|---|---|---|
| English (baseline) | o200k_base | tokens per word | 1.232 | FLORES-200 | BrahmicTokenizer-131K, arXiv 2605.29379, 28 May 2026, preprint |
| English | Llama-3.1 | tokens per word | 1.24 | FLORES-200 dev+devtest | same |
| Hindi | Llama-3.1 / Gemma-3 | tokens per word | 2.67 / 1.39 | FLORES-200 dev+devtest | same |
| Bengali | Llama-3.1 / Gemma-3 | tokens per word | 7.99 / 1.68 | FLORES-200 dev+devtest | same |
| Tamil | Llama-3.1 / Gemma-3 | tokens per word | 12.28 / 2.36 | FLORES-200 dev+devtest | same |
| Malayalam | Llama-3.1 / Gemma-3 | tokens per word | 16.16 / 3.33 | FLORES-200 dev+devtest | same |
| Nepali | o200k / Llama-3 / Gemma-2 | tokens per word (bytes per token) | 2.32 (7.84) / 3.76 (4.84) / 3.13 (5.81) | FLORES-200 devtest | "Vowel Signs Are Not Letters", arXiv 2608.26449, 2026, preprint |
| English | o200k / Llama-3 / Gemma-2 | tokens per word | 1.23 / 1.24 / 1.28 | FLORES-200 devtest | same |
| Hindi | o200k / Llama 3 / Qwen3 / DeepSeek / Gemma 3 / Tekken | premium vs English | 1.61 / 2.63 / 4.56 / 2.90 / 1.34 / 1.84 | parallel corpus (exact corpus not confirmed in the excerpt I read) | "The Invisible Language Tax", arXiv 2609.39001, September 2026, preprint |
| Arabic (MSA) | o200k / Llama 3 / Qwen3 / DeepSeek / Gemma 3 / Tekken | premium vs English | 1.43 / 1.73 / 1.66 / 1.70 / 1.52 / 1.30 | same | same |
| Arabic (MSA) | Jais (2023) vs Llama 2 | tokens per word | 1.926 vs 5.384 | 39-million-word Arabic corpus | "Second Language (Arabic) Acquisition of LLMs via Progressive Vocabulary Expansion", arXiv 2412.12310, December 2024, preprint |
| Urdu | cl100k_base (older OpenAI) | word-fertility ratio vs English | about 3.4 | not stated in excerpt | "The Tokenizer Tax", arXiv 2607.24276, 2026, preprint |

Notes on the table:

- **Odia shows how large the extremes are.** Llama-3.1 reaches 16.78 tokens per word, Tekken/Sarvam-m 18.18 and GPT-OSS-120B (which uses o200k) 6.79 (BrahmicTokenizer-131K, May 2026, preprint).
- **Sarvam's own tokenisers are the most efficient in that panel.** On mean Brahmic fertility, the Sarvam-30B tokeniser (262K vocabulary) and Sarvam-1 (68K) both rank above Gemma-3, whose mean is 2.70. The same paper reports that Sarvam-1's English fertility is 15.9% worse than its own tokeniser's. The review could not confirm whether Sarvam-105B uses the Sarvam-30B tokeniser.

**What the vendors publish themselves**

- **Claude:** Anthropic does not publish the tokeniser. It offers a token-counting endpoint instead (secondary developer sources, 2026). The Invisible Language Tax preprint (September 2026) reports Claude 5 premiums for French (1.45) and Chinese (1.15) only. The review found no published Claude figure for any of these languages.
- **Fanar:** QCRI's report (arXiv 2501.13944, January 2025, preprint) describes a morphology-aware "MorphBPE" Arabic tokeniser. It says the tokeniser keeps reasonable fertility while aligning best with Arabic morphology. The fertility values are shown only in a figure; the review found no table.
- **Jais 2:** a new 150,272-token BPE vocabulary weighted towards Arabic and English, with Hindi and French in smaller amounts (Jais 2 technical report, arXiv 2608.13580, 7 July 2026, preprint). It publishes no per-language fertility figure.
- **Kona2:** adds 20,000 Georgian tokens to a Mistral-architecture base (Tbilisi AI Lab model card, Hugging Face, 2025, vendor claim). No fertility figure.
- **Llama 4:** a 200K vocabulary according to a 2026 preprint on 25 European languages (arXiv 2605.24718, preprint). The review found no figure for these languages.
- **Gemini:** The review found no figure for Gemini's own tokeniser. The Gemma 3 and Gemma 4 tokenisers are often used as a stand-in, but Google does not confirm that they are identical.

**Gaps.** The review found no 2024 to 2026 per-tokeniser figures for Sinhala, Tagalog, Georgian (beyond Ahia's 2023 OpenAI tokeniser), Gulf Arabic or Urdu on current tokenisers.

### 1.3 What the gap means for cost, latency and context

- **Measure caution.** Tokens per word overstates the gap for agglutinative languages such as Malayalam, Tamil and Georgian, because they express the same content in fewer, longer words. The fair measure of "same content" is Petrov's parity premium on parallel sentences. Treat the tokens-per-word ratios above as upper-bound indicators.
- **Cost.** Under per-token pricing, the premium multiplies cost directly. A Hindi exchange on a Qwen3-tokenised model needs about 4.56 times the tokens of the English equivalent, against 1.34 times on Gemma 3 (Invisible Language Tax, September 2026, preprint). For the same price per token, that is roughly a 3.4-fold cost difference for Hindi between those two tokenisers.
- **Latency.** Models generate one token at a time, so time to finish an answer scales roughly with the number of output tokens. The same premium therefore lengthens Hindi or Malayalam answers in wall-clock time. Petrov et al. (NeurIPS 2023) note that this premium also affects latency and processing time.
- **Usable context.** A 128K-token window holds about 128K divided by the premium in English-equivalent content. That is about 95K English-equivalent tokens for Hindi on Gemma 3, against about 28K on Qwen3. The Tokenizer Tax preprint (arXiv 2607.24276, 2026) frames this as Hindi or Tamil users effectively getting "a smaller window" for identical content.

### 1.4 Measuring the tokenisers directly

The authors of this report could not run tokenisers in their research environment. mAIself has since measured nine of these languages on five tokenisers, using the full Universal Declaration of Human Rights as parallel text: see brief 02 and https://github.com/WolffSimon/token-premiums. FLORES-200 devtest remains the better corpus for a fuller measurement, with Unicode NFC normalisation, special tokens switched off, and a check that each tokeniser decodes its output back to the input. Megrelian, Svan and Laz need curated seed text, because language identification confuses them with Georgian (brief 01).

## 2. Language errors outside English

**Safety gaps**

- **Yong, Menghini and Bach, "Low-Resource Languages Jailbreak GPT-4" (arXiv 2310.02446, October 2023; NeurIPS 2023 SoLaR workshop spotlight; workshop paper, so lighter review than the main conference).**
  - **Method:** AdvBench harmful prompts were translated with Google Translate into 12 languages of low, mid and high resource, then sent to gpt-4-0613.
  - **Result:** translating English inputs into low-resource languages raised the chance of bypassing GPT-4's safety filter from under 1% to 79% (79.04% for the combined low-resource attack).
  - **Comparison:** high- and mid-resource languages had much lower success rates.
- **Yong et al., "The State of Multilingual LLM Safety Research", EMNLP 2025 (peer-reviewed, November 2025).** A follow-up survey that maps the gap between English and other languages in safety research. The review saw only the citation, not the paper's figures.
- **"Multilingual jailbreaking of LLMs using low-resource languages" (arXiv 2605.18239, 2026, preprint).** Shows the problem is still being studied in 2026. The review has not verified its figures.

**Cultural default errors.** Naous et al. (ACL 2024, peer-reviewed) find that multilingual and Arabic-only models prefer Western entities in Arabic contexts across eight categories, such as person names, food, beverages and religion. An example is suggesting alcohol after a reference to Islamic prayer. They also find unfair results in named-entity recognition and sentiment analysis on Arab versus Western entities.

**Translationese and translated benchmarks**

- SinhalaMMLU (arXiv 2509.03162, September 2025, preprint) found that native Sinhala questions scored 97.3 for linguistic fluency against 71.07 for questions machine-translated from Global-MMLU. Translated test sets therefore carry translationese, which can distort scores.
- The Global-MMLU authors (arXiv 2412.03304, December 2024, preprint) report two related problems with the original MMLU. 28% of its questions need culturally sensitive knowledge, and 84.9% of its geographic questions concern North America or Europe. Translating such a test does not make it culturally neutral.

**Answering in English instead of the local language.** BLEnD (NeurIPS 2024 Datasets and Benchmarks, peer-reviewed) found that for low-resource languages, models gave better answers in English than in the local language. For mid- and high-resource languages the reverse held. This affects whether a system should answer a Nepali or Sinhala question in the local language or translate internally.

**Script and dialect mixing.**
- Sarvam says its 105B model is trained on native-script, romanised and code-mixed input (Sarvam documentation, March 2026, vendor claim). That implies the vendor sees mixed input as a main pattern for Indian users.
- Jais 2 includes dialectal Arabic and Arabizi in its training and offers Arabic dialect identification as a task (Jais 2 report, July 2026, preprint).
- The review found no independent rate at which frontier models drift into the wrong script or dialect in these languages.

**Gaps**

- **Morphology and Georgian.** Arnett and Bergen, "Why do language models perform worse for morphologically complex languages?" (COLING 2025, peer-reviewed), addresses the question directly. The review saw only the citation, and the review found no Georgian-specific study of grammatical errors.
- **Hallucination rates by language.** The review found no study from 2024 onwards giving factual hallucination rates for these eleven languages.
- **Error taxonomies.** The review did not retrieve a primary source for MQM (Multidimensional Quality Metrics) or other error taxonomies, so the review makes no claims about them here.

**What would fill these gaps.**
- Ask native-speaker annotators to label 200 to 500 answers per language and model with a fixed error taxonomy, for example MQM-style categories plus "wrong script", "wrong dialect" and "wrong register".
- Pair this with a jailbreak test that translates AdvBench or similar prompts into Nepali, Sinhala, Tagalog and Georgian.

## 3. Languages served: claims and measurements

### 3.1 Vendor claims that could be verified

| Model | Claimed languages | Source and label |
|---|---|---|
| Fanar-1-9B-Instruct (QCRI) | Arabic, English | Hugging Face model card, 2025, vendor claim |
| Jais 2 (8B, 70B) | Arabic (MSA, regional dialects, Arabizi) and English | Jais 2 report, arXiv 2608.13580, 7 July 2026, preprint |
| Sarvam-105B | "10 most-spoken Indian languages + English" (Sarvam docs); "22 Indian languages" (Hugging Face card) | Sarvam docs and Hugging Face card, March 2026, vendor claim. **The two pages conflict.** |
| SEA-LION v4 (Gemma 27B) | Training data in Burmese, English, Mandarin, Indonesian, Khmer, Lao, Malay, Tagalog, Tamil, Thai, Vietnamese | AI Singapore blog, August 2025, vendor claim |
| Qwen-SEA-LION-v4 | Inherits Qwen3's "over 100 languages" | AI Singapore blog, 2025, vendor claim |
| Kona2-12B | Georgian, English, "other (limited)" | Tbilisi AI Lab model card, 2025, vendor claim |
| Llama 3 | Officially eight languages | as reported in Omnilingual SONAR, arXiv 2603.16606, 2026, preprint |

**Not verified in this pass:** the official language lists for Claude, GPT-5.x, Gemini, Llama 4, Mistral, Mistral Saba, DeepSeek, Grok, Kimi, ALLaM and Falcon. Before quoting any of them, take each list from the vendor's current model card.

### 3.2 Independent measurements in these languages

- **Global-MMLU (Singh et al., Cohere For AI with EPFL, Hugging Face, AI Singapore and others; arXiv 2412.03304, December 2024, preprint).**
  - Covers 42 languages, classed as 20 high-, 9 mid- and 13 low-resource.
  - Nepali and Sinhala are classed as low-resource.
  - Translations are a mix of human and machine, with human post-editing.
  - About 2,850 questions per language are tagged "culturally sensitive" or "culturally agnostic".
  - The authors evaluated 14 open-weight and proprietary models from 9 model families.
- **INCLUDE (arXiv 2411.19799, November 2024, preprint).**
  - 197,243 multiple-choice questions drawn from 1,926 local exams.
  - Covers 44 languages, 15 scripts and 52 countries.
  - Includes Georgian, Nepali and Tagalog items written natively rather than translated.
- **SEA-HELM (AI Singapore leaderboard, live October 2026).**
  - Covers Burmese, Filipino, Indonesian, Malay, Tamil, Thai and Vietnamese.
  - SEA-LION v4 (Gemma) 27B scores 59.84 ± 0.05 overall and 68.10 ± 0.14 in Tagalog (leaderboard).
  - At release, AI Singapore said SEA-LION v4 was the number one model for Tamil and Filipino and ranked 4th of 55 overall (Google DeepMind Gemmaverse page, 2025, vendor claim).
  - SEA-LION v4.8 (Nemotron 120B) raised the overall SEA-HELM score from 49.30 to 63.44 (arXiv 2609.18310, September 2026, preprint). The authors note that live leaderboard scores may change.
  - SEA-HELM is built by the SEA-LION developers. It is public and reproducible, but it is not neutral.
- **SinhalaMMLU (arXiv 2509.03162, September 2025, preprint).** Native Sinhala curriculum questions. Claude 3.5 Sonnet scored highest at 67.65%. Claude also gained more than GPT-4o when told the subject of each question.
- **MMLU-ProX (arXiv 2503.10497, 2025, preprint).** Covers Hindi, Bengali, Urdu and Nepali, among others. Reports up to 24.3% performance gaps between languages.
- **MILU (arXiv 2411.02538, November 2024, preprint).** An Indic benchmark covering Bengali, Hindi, Malayalam, Tamil and other Indic languages.
- **Arabic.**
  - Fanar-1-9B's model card reports results on OALL and OALL v2, ArabicMMLU, Belebele (Arabic) and the AraDiCE dialect sets: Egyptian and Levantine (vendor-run evaluation on public benchmarks, 2025).
  - Jais 2 reports "leading results among the evaluated open models on OALL2 and AraGen" (July 2026, preprint, self-reported).
  - The review could not reach the live Open Arabic LLM Leaderboard to confirm current rankings for Jais 2, ALLaM or Fanar.

### 3.3 Claims of support with no independent measurement behind them

- **Sarvam-105B.** Its Indic quality claim is a 90% average pairwise win rate, judged by Gemini 3 as an LLM judge, on prompts translated into 22 languages (Sarvam blog, February to March 2026, vendor claim). An independent review notes that Sarvam-105B reports only its in-house IndiVibe benchmark and not MILU. It also notes that most Indian model results are developer-reported (arXiv 2608.11891, 2026, preprint).
- **Kona2 (Georgian).** The review found no independent Georgian benchmark result.
- **Gulf Arabic, for every model.** The dialect evaluations the review found (AraDiCE) cover Egyptian and Levantine, not Gulf.
- **Nepali, Sinhala and Georgian on frontier models.** Nepali and Sinhala appear in Global-MMLU, and Georgian, Nepali and Tagalog in INCLUDE (Global-MMLU does not include Georgian; see brief 01), but the review did not retrieve current 2026 per-model scores for Claude, GPT-5.x, Gemini, Grok or Kimi.
- **Mistral Saba, ALLaM, Falcon (Arabic) and Llama 4.** The review retrieved no independent scores in these languages.

**Contamination.** The Microsoft Research survey "The State and Fate of Multilingual, Contextual Evaluation in the NLP World" (April 2026, under review for COLM 2026) audited 51 benchmarks and, across seven recent models, flagged contamination signals in two older benchmarks: 45.5% of model-language pairs on MGSM and 67.9% on PAWS-X. Newer benchmarks showed far fewer: MILU 0.0%, INCLUDE 1.0% and Global-MMLU 1.7%. Prefer INCLUDE, Global-MMLU and MILU over MGSM when comparing models.

**What would fill the gaps.** Run INCLUDE, Global-MMLU (full or Lite), Belebele and FLORES-200 translation in both directions across all 17 models, using one harness and one date. Add a small native-authored Gulf Arabic set and a Georgian instruction-following set.

## 5. Comparative benchmarks by task type

All standings come from leaderboards and move every week. Model names are as shown on the pages and may differ from the names used elsewhere. For example, Artificial Analysis now lists "GPT-6 Astra" alongside GPT-5.x models.

| Task | Benchmarks and leaderboards | Current standing found (date, label) | Caveat |
|---|---|---|---|
| Overall and cost/speed | Artificial Analysis Intelligence Index v4.3.2 (10 evaluations, including Terminal-Bench 4.0, HLE, GDPval-AA) | Claude Opus 5.5 (max) 58, cost per task $5.98, about 95 tokens/s; Claude Sonnet 5.5 (max) 56, $5.46, about 137 tokens/s; Meta Muse Wonder Full (max) 56; GPT-6 Astra (max) 53, $3.26, about 61 tokens/s; Gemini 4 Argon (high) 53, $1.99; best open-weights model MiMo-V2.6-Pro 46, $0.13 per task (page undated, accessed October 2026, leaderboard) | The page shows cost per task, not blended price per million tokens. Column alignment needs checking on the live page |
| General chat (Arena Text) | Arena (formerly LMArena) | gemini-4-argon-high 1525 ± 9 (preliminary), muse-wonder-max 1513, claude-opus-5.5-high 1508 (13 October 2026, leaderboard) | Overlapping confidence intervals; style control on by default |
| Copywriting and creative writing | Arena Creative Writing category; EQ-Bench Creative Writing; WritingBench | Not retrieved | Gap: fetch the Arena category page |
| Personal and relationship advice | EQ-Bench (emotional intelligence) | Not retrieved | No dedicated advice benchmark found |
| Mathematics | AIME, HMMT, MATH-500, FrontierMath | Sarvam-105B: MATH-500 98.6, AIME 25 88.3 (96.7 with tools), HMMT 85.8 (Sarvam, March 2026, vendor claim) | MATH-500 is close to saturated. AIME items leak after each contest |
| Quantitative analysis over data | DABench, GDPval-AA (inside the AA index) | Not retrieved separately | Gap |
| Long documents | LongBench v2, RULER, Fiction.LiveBench | Not retrieved | Gap. For non-English, also discount by the token premium (Section 1.3) |
| Coding and interactive software | SWE-bench Verified; Arena WebDev | SWE-bench Verified on vals.ai (mini-SWE-agent harness, archived 1 September 2026, leaderboard): Claude Opus 5 97.0%, DeepSeek V4 Pro 96.4%, GPT-5.6 Sol 96.2%. Arena WebDev (8 October 2026, leaderboard): claude-opus-5.5-max 1813 ± 15, gpt-6-astra-max 1786 ± 11; best open model kimi-k3-max 1674 | SWE-bench Verified is effectively saturated. A secondary site says Kimi K3 led WebDev on 12 October, which conflicts with the 8 October primary page |
| Image generation | Arena Text-to-Image | gpt-image-2.5-sunburst (OpenAI) 1421 ± 13 at #1 (7 September 2026, leaderboard) | Only the lab-level view was retrieved |
| Speech recognition | Hugging Face Open ASR Leaderboard (mean WER) | Edge0/ARK-ASR-3B 4.76, MOSS-Transcribe-preview-2B 4.87, cohere-transcribe-03-2026 5.42 (dataset page, undated, leaderboard) | Mostly English test sets; says nothing about Malayalam, Sinhala or Gulf Arabic |
| Translation | WMT general task; FLORES-200 | Not retrieved | Gap |
| Instruction following | IFEval, IFBench, SEA-IFEval (inside SEA-HELM) | Jais 2 reports Arabic instruction-following results (July 2026, preprint) | IFEval is near saturation for frontier models |
| Agentic tool use | tau2-bench, Terminal-Bench, BrowseComp | Sarvam-105B BrowseComp 49.5; Sarvam says it leads its comparison set on tau2 (March 2026, vendor claim). tbench.ai official table not retrieved | Terminal-Bench 2.1 fixed 28 of 89 tasks in 2.0, so older scores are not comparable |

**Speed for Arabic.** Jais 2 70B runs on Cerebras hardware at "up to 2,000 tokens per second" (Jais 2 report, July 2026, vendor claim). For Arabic, that partly offsets the token premium.

## Caveats

- **Search budget.** Several primary pages were not reachable within the research budget:
  - vendor language lists for most frontier models;
  - the live Open Arabic LLM Leaderboard;
  - the Arena Creative Writing category;
  - swebench.com and tbench.ai;
  - EQ-Bench and long-context leaderboards.
  The relevant rows are marked as gaps rather than filled from memory.
- **Conflicting aggregators.** Secondary aggregator sites give conflicting October 2026 rankings, naming for example "Claude Mythos 5" or "Claude Fable 5" as number one. The review used primary leaderboard pages wherever it could and did not use aggregators for standings.
- **Mostly preprints.** Most post-2024 tokenisation evidence is in preprints from 2026. The numbers are consistent across papers in direction, but not in exact values, because their measures and corpora differ.
