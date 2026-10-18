# Brief 01: Kartvelian language resources for AI training and Kartvelology

A verified inventory, September 2026. Compiled with AI research tools from the sources linked in each row; figures marked unverified or secondary were not checked against the primary source and should not be quoted as fact. Tidied for publication on 18 October 2026; the content is otherwise unchanged except where noted.

Georgian is the only Kartvelian language with training-scale open data: roughly 1.4–2.6 billion words of permissively licensed, bulk-downloadable web text (FineWeb-2, HPLT 3.0, CulturaX, MADLAD-400) plus about 168 validated hours of CC0 speech (Common Voice). Megrelian (Mingrelian), Laz and Svan together have well under 1% of that: a Wikipedia, a few hundred thousand tokens of fieldwork and web text, and small Common Voice sets. The richest curated and diachronic Kartvelological material (GNC, GLC, TITUS, MLC) can be searched online but cannot be downloaded in bulk.

## TL;DR

- **Georgian (kat):** Build the pretraining base from FineWeb-2 kat_Geor (1.44B words, ODC-By) and HPLT 3.0 kat_Geor (7.55B Gemma-3 tokens, CC0), and add CulturaX ka (2.62B tokens, 3.12M docs, gated) and MADLAD-400 ka (936,497 docs). They overlap heavily, so deduplicate across all of them. For speech, use Common Voice 25.0 (167.53 validated hours, CC0). For evaluation, use FLORES+/Belebele, GeoLogicQA (100 items) and the 370 case-alignment minimal pairs. The best-annotated data (the GNC's ~200M tokens, GLC, and treebanks of 3,164 and 1,878 sentences) is query-only or small.
- **Megrelian (xmf):** The largest open text sources are Mingrelian Wikipedia (22,176 articles as of March 2026, CC BY-SA), CulturaX xmf (9,706 docs) and Leipzig xmf_wikipedia_2012 (114,288 tokens). The best linguistic resource, the Ilia State University MLC (97,691 glossed tokens), is query-only. Common Voice Mingrelian exists, but the hours are still unverified (an indirect sign points to about 11.5 h).
- **Laz (lzz) and Svan (sva):** Neither has a training-ready corpus. Laz has an open Incubator Wikipedia and Wiktionary, a Common Voice set added in v24 (size unverified) and a public FST analyser whose 111K-token test corpus is private. Svan has the DoReCo annotated audio corpus (CC BY 4.0) and an Incubator Wikipedia. For both, fieldwork archives (TLA, ELAR, TITUS) are the real source, and access has to be negotiated.

## 1. Executive summary per language

**Georgian (Modern, Old, Middle, dialects).** Modern Georgian is a mid-resource language for AI purposes. Measured web text alone is 1.44B words in FineWeb-2 and 2.62B tokens in CulturaX, the Leipzig kat_mixed_2017 corpus adds 642.7M tokens of sentence-shuffled text, and there is a 2.6M-example SFT mix (kona-sft-mix-2.6M, ODC-By). Speech is thinner: 167.53 validated CC0 hours in Common Voice, plus about 190 h (Babel) and about 79 h (MATERIAL) behind LDC licences. Old and Middle Georgian are well curated but locked. TITUS (Frankfurt) carries the principal electronic texts. The GNC reports about 6M Old and 1.4M Middle Georgian tokens, search-only. There are two small Old Georgian UD treebanks (OGLauRo, from the Book of Ezra in the Oshki Bible, CC BY-NC-SA; UD_Old_Georgian-GLC, size unverified). Dialect data sits in the GNC dialect subcorpora (GDC, SSGG) and the Chikobava Institute's resources, all query-only.

**Megrelian (xmf).** This is the best-resourced minority Kartvelian language, but it is still tiny. The Wikipedia has 22,176 articles (March 2026). The MLC holds 97,691 IPA-transcribed, morpheme-glossed tokens with Georgian and English translations, query-only, with a UD treebank in preparation. The GNC Megrelian subcorpus has 89,404 words, unannotated. Web-crawl subsets exist (CulturaX 9,706 docs; FineWeb-2 about 4.12k rows) but are likely contaminated with Georgian, because both languages use Mkhedruli and language-ID models confuse them.

**Laz (lzz).** Almost all Laz text is in a Turkish-based Latin orthography, so Georgian-script pipelines miss it. Open material consists of the Incubator Wikipedia (Wp/lzz, with a Latin-script branch), the Incubator Wiktionary (Wt/lzz, whose category lists 3,837 pages), Common Voice lzz (added in v24, December 2025) and the Önal & Tyers analyser and lexicon. There is no large public corpus. The 111,365-token Bucaklişi test corpus is private.

**Svan (sva).** The main open resource is the DoReCo Svan corpus (Gippert, recorded 2002–2005; CC BY 4.0; time-aligned, with Georgian and English translations). The Incubator Wikipedia (Wp/sva) is open, and no Meta-Wiki request has been filed. Everything else (ECLinG and Tuite materials, the GNC Svan subcorpus, TITUS Svan texts) is in archives or query-only.

## 2. Verification table (earlier figures, reconciled)

| Claim | Verdict | Primary source / note |
|---|---|---|
| FineWeb-2 kat_Geor 1,439,572,993 words; 3,706,659 docs; ODC-By | Verified (first pass) | huggingface.co/datasets/HuggingFaceFW/fineweb-2 |
| FineWeb-2 xmf_Geor ~4.12k rows, likely LID-contaminated | Verified (first pass) | same |
| HPLT 3.0 kat_Geor 6.13M docs; 7.55B Gemma-3 tokens; 17.01B chars; CC0 | Verified (first pass) | hplt-project.org/datasets/v3.0 |
| CulturaX ka size | **New: 3,120,321 docs; 2,617,625,564 tokens.** xmf: 9,706 docs, token count not reported | huggingface.co/datasets/uonlp/CulturaX (gated; access requires accepting terms) |
| MADLAD-400 ka size | **New: 936,497 docs (audit note "ok", kept)** | huggingface.co/datasets/allenai/MADLAD-400. Licence conflict: HF metadata says ODC-By, card text says CC-BY-4.0 |
| MADLAD-400 xmf/lzz/sva | Unverified (not found in the portion of the audit table retrieved) | same |
| Leipzig Georgian corpora | **New: kat_mixed_2017 = 49,542,495 sentences, 642,703,382 tokens; xmf_wikipedia_2012 = 10,191 sentences, 114,288 tokens** | corpora.wortschatz-leipzig.de/en?corpusId=kat_mixed_2017; corpora.uni-leipzig.de/en?corpusId=xmf_wikipedia_2012 |
| Mingrelian Wikipedia article count | **New: 22,176 (6 March 2026); 13,836 (30 April 2020); CC BY-SA 3.0 / GFDL** | Wikidata Q2029239 (imported from xmf.wikipedia.org Special:Statistics) |
| Laz / Svan Wikipedia status | **New: both open test wikis in Wikimedia Incubator. Wp/lzz has a Meta-Wiki request; Wp/sva has none. Wt/lzz category lists 3,837 pages** | incubator.wikimedia.org/wiki/Wp/lzz; /Wp/sva; /Category:Wt/lzz |
| Common Voice 25.0 Georgian 323.49 h / 167.53 h validated / 2,764 speakers / 134,521 sentences | Verified; **adds 227,399 clips** | datacollective.mozillafoundation.org/datasets/cmn2h4m7901gzo1072qn7zoes |
| Common Voice Mingrelian ≈12.63 h / 11.57 h validated / 89 speakers / 1,040 sentences; variants Senak-Martvili, Zugdidi, Samurzaqano | **Still unverified.** An MDC datasheet "A collection of read speech recordings in Mingrelian" exists but renders only via JavaScript. Indirect corroboration: the k2-fsa OmniVoice language list gives Mingrelian (xmf) 11.47 (hours of training data), consistent in magnitude with ~11.5 validated h | github.com/k2-fsa/OmniVoice/blob/master/docs/languages.md (secondary) |
| Common Voice Laz size | Unverified. **Confirmed added in v24 (release post, 18 Dec 2025)**; dataset page datacollective.mozillafoundation.org/datasets/cmj8u3pei00fpnxxb2zv0zgwh | community.mozilladatacollective.com (v24 post) |
| Common Voice 27.0 Georgian | Unverified per language. Corpus-wide v27: 42,593 h total / 29,295 h validated | github.com/common-voice/cv-dataset (release chart) |
| UD_Georgian-GLC 3,164 sentences / 56,174 tokens (UD 2.18) | Verified (first pass). **Reconciled:** the README says 151 GLC sentences (2,123 tokens) + 3,013 Wikipedia sentences (44,030 tokens); 151 + 3,013 = 3,164 sentences, matching. README token totals (46,153) are lower than UD 2.18 statistics; trust the UD release statistics (newer, computed automatically) | github.com/UniversalDependencies/UD_Georgian-GLC; universaldependencies.org/treebanks/ka_glc |
| "151 sentences / 5,809 tokens" | **Partly wrong.** 151 sentences is the GLC sample inside UD_Georgian-GLC (not Old Georgian), but its README gives 2,123 tokens, not 5,809 | same |
| UD_Georgian-GLC first release | **New: debuted in UD 2.13 at 2,335 words** | ELRA Corpora-List UD 2.13 announcement |
| UD_Old_Georgian-GLC size/licence | Still unverified (UD page not retrievable this pass) | universaldependencies.org/treebanks/oge_glc |
| UD_Old_Georgian-OGLauRo | Verified; **new: multiple Zenodo versions (records 19616030, 20168339, 20928957); GitHub chiaweilinunil/UD_Old_Georgian-OGLauRo; base text from TITUS Oshki Bible, with acknowledged guidance from Meurer and Gippert** | zenodo.org/records/20168339 |
| GeoLogicQA item count | **New: 100 questions; LLM accuracy 64–83% vs human baseline 47%** | aclanthology.org/2025.lowresnlp-1.13 |
| Global-MMLU includes Georgian | **New: No.** 42 languages without Georgian; MMLU-ProX (29 languages) also lacks it | cohere.com/research/globalmmlu (42 languages). Note added 18 October 2026: brief 05 reports the Global-MMLU paper (ACL 2025, arxiv.org/abs/2412.03304) as listing 42 languages with no Georgian, Armenian or Azerbaijani. |
| Tesseract kat / kat_old | **New: both added in Tesseract 3.04 (July 2015)**; tessdata also ships script/Georgian.traineddata | github.com/tesseract-ocr/tessdata; tesseract-ocr wiki Data-Files |
| Tsintsadze et al. 2018 handwriting dataset | **New: >200,000 character samples (summary says 200 authors); SNN-CNN >94% accuracy; public availability of the dataset unconfirmed** | sciencedirect.com/science/article/pii/S2405896318329525 |
| OPUS-100 en-ka | **New: 381k rows total (HF viewer)**; split sizes unverified (the design caps train at 1M and dev/test at 2,000 each) | huggingface.co/datasets/Helsinki-NLP/opus-100; opus.nlpl.eu/OPUS-100 |
| OPUS per-corpus en–ka counts | **Unverified**. OPUS API blocked automated access this pass | opus.nlpl.eu/opusapi (query source=en&target=ka) |
| DoReCo Svan tokens/hours; TITUS Laz ~900 tokens; GNC per-subcorpus sizes | Still unverified | doreco.huma-num.fr/languages/svan1243; LINDAT LRT-957/958; gnc.gov.ge |
| "~4.3× UTF-8 byte premium vs English" | **Unverified as stated.** Derived measure: FineWeb-2 kat = 25.23 GB / 1.44B words ≈ 17.5 bytes per word; every Mkhedruli letter is 3 bytes in UTF-8 vs 1 for ASCII | computed from FineWeb-2 card |

## 3. Resource tables by category

Column key: Creator | Variety | Modality | Size | Period/genre | Annotation | Licence | Access | URL | Status | Caveats.

### A. Web-scale monolingual text

| Resource | Creator | Variety | Mod. | Size | Period/genre | Annot. | Licence | Access | URL | Status | Caveats |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FineWeb-2 kat_Geor | Hugging Face | Modern Georgian | text | 1.44B words; 3.71M docs; 25.23 GB | CC 2013–Apr 2024, web | GlotLID, quality filters | ODC-By | HF bulk | huggingface.co/datasets/HuggingFaceFW/fineweb-2 | Verified | Overlaps HPLT and CulturaX |
| FineWeb-2 xmf_Geor | Hugging Face | Megrelian (claimed) | text | ~4.12k rows | web | LID | ODC-By | HF | same | Verified | Likely contaminated with Georgian |
| HPLT 3.0 kat_Geor | HPLT consortium | Modern Georgian | text | 6.13M docs; 7.55B Gemma-3 tokens; 17.01B chars | IA + CC crawls | LID, dedup | CC0 | bulk | hplt-project.org/datasets/v3.0 | Verified | IA crawls add non-CC material |
| CulturaX ka | UONLP (Oregon) | Modern Georgian | text | 3,120,321 docs; 2,617,625,564 tokens | mC4 3.1.0 + OSCAR 20.19–23.01 | MinHash dedup | inherits mC4/OSCAR terms | HF, gated | huggingface.co/datasets/uonlp/CulturaX | Verified (size) | Superset of mC4/OSCAR; overlaps FineWeb-2 |
| CulturaX xmf | UONLP | Megrelian (claimed) | text | 9,706 docs; tokens not reported | same | n/a | same | HF, gated | same | Verified (docs) | LID reliability unknown |
| MADLAD-400 ka | Google / AI2 | Modern Georgian | text | 936,497 docs | CC to Aug 2022 | doc-level LID, audited | CC-BY-4.0 (card text) / ODC-By (metadata) | HF bulk | huggingface.co/datasets/allenai/MADLAD-400 | Verified (docs) | Licence metadata inconsistent |
| Leipzig kat_mixed_2017 | Leipzig Univ. | Modern Georgian | text | 49.54M sentences; 642.70M tokens | mixed web/news 2017 | sentence-level | unverified | download (parts) | corpora.wortschatz-leipzig.de/en?corpusId=kat_mixed_2017 | Verified (size) | Sentence-shuffled; no documents |
| Leipzig xmf_wikipedia_2012 | Leipzig Univ. | Megrelian | text | 10,191 sentences; 114,288 tokens | Wikipedia 2012 | n/a | derived from CC BY-SA | download | corpora.uni-leipzig.de/en?corpusId=xmf_wikipedia_2012 | Verified | Old snapshot |
| Mingrelian Wikipedia | Wikimedia | Megrelian | text | 22,176 articles (Mar 2026) | encyclopedic, since Nov 2011 | n/a | CC BY-SA 3.0 / GFDL | dumps | xmf.wikipedia.org | Verified | Many stubs; standard-Georgian loans |
| Georgian Wikipedia | Wikimedia | Modern Georgian | text | 199,132 articles (19 Sep 2026, per English Wikipedia's "Georgian Wikipedia" article); 191,760 on 6 Mar 2026 (Wikidata Q848974, from Special:Statistics) | encyclopedic, founded Nov 2003 | n/a | CC BY-SA | dumps | ka.wikipedia.org | Verified | Already inside most web crawls |
| Wp/lzz, Wt/lzz (Incubator) | Wikimedia Incubator | Laz | text | Wt/lzz category 3,837 pages | encyclopedic/lexical | n/a | CC BY-SA | Incubator export | incubator.wikimedia.org/wiki/Wp/lzz | Verified (status) | Latin-script branch Wp/lzz/lat |
| Wp/sva (Incubator) | Wikimedia Incubator | Svan | text | unverified | encyclopedic | n/a | CC BY-SA | Incubator | incubator.wikimedia.org/wiki/Wp/sva | Verified (status) | No Meta request filed |
| kaTenTen24 | Sketch Engine | Modern Georgian | text | 1.1B+ tokens; 860M+ words | web Aug–Sep 2024 | genre/topic labels | commercial | paid, query | sketchengine.eu/katenten-georgian-corpus | Verified | Not lemmatised; no download |
| OSCAR 23.01, CC-100, mC4 ka; Glot500-c, GlotCC; Crúbadán | various | Georgian (+xmf?) | text | unverified | CC | n/a | various | HF/bulk | n/a | Unverified | Largely subsumed by CulturaX and FineWeb-2 |

### B. Curated national and reference corpora

| Resource | Creator | Variety | Mod. | Size | Period/genre | Annot. | Licence | Access | URL | Status | Caveats |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Georgian National Corpus (GNC) | Gippert, Meurer, Tandashvili; CLARINO Bergen | Old, Middle, Modern, GRC, Megrelian, Svan, dialects (GDC, SSGG) | text | ~200M Modern, ~6M Old, 1.4M Middle tokens; >202M total (2024 paper) | 5th c.–present | lemma + MSD (core, GRC) | mostly CC BY-NC | query-only | gnc.gov.ge | Verified (aggregate) | Per-subcorpus sizes unverified; "217M words" figure from secondary overview |
| Georgian Language Corpus (GLC) | Ilia State Univ. (Doborjginidze, Lobzhanidze) | Modern (1832–2012), Old, Middle | text | unverified | literary, press, chronicles | lemma, POS | unverified | query-only | corpora.iliauni.edu.ge; oldcorpora.iliauni.edu.ge | Verified (existence) | Bilingual subcorpora: Vepkhistqaosani ka–en; Kartlis Tskhovreba ka–hy |
| TITUS Old Georgian texts | Gippert, Frankfurt | Old Georgian | text | unverified | Bible (incl. Oshki), hagiography | partly | academic use | web pages | titus.uni-frankfurt.de | Verified (existence) | Base text for OGLauRo |
| GREgORI Old Georgian | Louvain (Kindt), Calfa | Old Georgian | text | unverified | patristic | lemma, POS | unverified | on request | calfa.fr/textanalysis | Unverified size | Joint lemmatisation/POS models (LT4HALA 2020) |
| Epigraphic Corpus of Georgia | Ilia State Univ. | Old Georgian inscriptions | text | unverified | epigraphy | EpiDoc | unverified | query | n/a | Unverified | n/a |
| Georgian Dialect Corpus / GEDA | Beridze; Chikobava Institute | Georgian dialects | text, audio | unverified | fieldwork | partial | unverified | query | corpora.co | Unverified | Partly integrated in GNC |

### C. Treebanks and annotated evaluation sets

| Resource | Creator | Variety | Size | Annot. | Licence | Access | URL | Status | Caveats |
|---|---|---|---|---|---|---|---|---|---|
| UD_Georgian-GLC (2.18) | Lobzhanidze et al., Ilia | Modern | 3,164 sents (151 GLC + 3,013 Wikipedia); 56,174 tokens | UD, partly automatic | CC BY-SA 4.0 | GitHub bulk | github.com/UniversalDependencies/UD_Georgian-GLC | Verified | First released in UD 2.13 (2,335 words) |
| UD_Georgian-GNC (2.18) | Meurer | Modern (novels, news) | 1,878 sents; ~23K tokens | FST + CG, manually corrected; masdar lemmas | CC BY-SA 4.0 | GitHub | github.com/UniversalDependencies/UD_Georgian-GNC | Verified | Lemma convention differs from GLC |
| UD_Old_Georgian-GLC | Ilia | Old Georgian | unverified | UD | unverified | GitHub | universaldependencies.org/treebanks/oge_glc | Unverified | New in UD 2.18 |
| UD_Old_Georgian-OGLauRo | Lin & Luinetti (Lausanne) | Old Georgian (Ezra, Oshki Bible) | unverified | LLM-drafted, hand-corrected | CC BY-NC-SA 4.0 | Zenodo/GitHub | zenodo.org/records/20928957 | Verified | NC licence |
| Georgian case-alignment tests | Gallagher & Heyer | Modern | 370 minimal pairs | syntactic | unverified | arXiv | arxiv.org/abs/2602.10661 | Verified | Derived from GLC UD |
| MLC UD treebank | Ilia | Megrelian | in preparation | UD | n/a | n/a | aclanthology.org/2026.lrec-1.255 | Announced | n/a |
| Laz treebank | UDW 2020 | Laz | small, unverified | UD | unverified | unverified | aclanthology.org/2020.udw-1.21 | Unverified size | n/a |

### D. Parallel and MT data

| Resource | Variety | Size | Licence | Access | URL | Status | Caveats |
|---|---|---|---|---|---|---|---|
| OPUS collection (all) | ka paired with many languages | 1,214 corpora, 102.9B sentence pairs overall; en–ka per-corpus counts unverified | per corpus | bulk | opus.nlpl.eu | Partly verified | Georgian present in OpenSubtitles, WikiMatrix, CCMatrix, CCAligned, NLLB, GNOME/KDE4/Ubuntu, QED, Tanzil, Tatoeba, TED2020, bible-uedin (per OPUS listings); counts not retrieved |
| OPUS-100 en-ka | ka–en | 381k rows total | per source | HF bulk | huggingface.co/datasets/Helsinki-NLP/opus-100 | Verified (total) | Dev/test known to overlap in v1.0 (Yang et al. 2021) |
| FLORES+ kat_Geor | ka + 200 langs | 997 dev and 1,012 devtest sentences per language (openlanguagedata/flores_plus card) | CC BY-SA 4.0 | HF, gated | huggingface.co/datasets/openlanguagedata/flores_plus | Verified | Public test set with documented contamination |
| NTREX-128, Belebele, SIB-200 kat_Geor | ka | unverified | various | HF/GitHub | n/a | Unverified | Standard multilingual evals |
| tbilisi-ai-lab/en-ka-human-translated | ka–en | ~5K pairs (unconfirmed) | unverified | HF | huggingface.co/tbilisi-ai-lab | Unverified | n/a |
| GLC bilingual subcorpora | ka–en (Vepkhistqaosani), ka–hy (Kartlis Tskhovreba) | unverified | unverified | query | corpora.iliauni.edu.ge | Verified (existence) | Literary/historical |
| MATERIAL Georgian–English (LDC2025S01) | ka speech + en translation | ~79 h | LDC | paid | catalog.ldc.upenn.edu | Verified | Speech-translation |
| GRUG ka–ru–uk–de parallel treebank | Kapanadze, CLARIN-D | unverified | unverified | CLARIN | n/a | Unverified | n/a |
| xmf / lzz / sva in FLORES/NLLB | n/a | absent (no evidence found otherwise) | n/a | n/a | n/a | Presumed absent | MLC gives xmf–ka–en glossed triples (query-only) |

### E. Instruction, SFT and benchmarks

| Resource | Creator | Size | Licence | Access | URL | Status | Caveats |
|---|---|---|---|---|---|---|---|
| kona-sft-mix-2.6M | Tbilisi AI Lab | 2,606,173 examples; 9.9 GB | ODC-By | HF | huggingface.co/tbilisi-ai-lab | Verified | Mostly machine-translated; ~350K human-verified |
| kona-dpo-mix-387k | Tbilisi AI Lab | 387K preference pairs (the Kona2-12B model card cites "DPO on 387K preference pairs") | unverified | HF | same | Verified | n/a |
| Kona2-12B (model) | Tbilisi AI Lab | Mistral-Nemo + 20K ka tokens; ~30B-token CPT | Apache 2.0 | HF | same | Verified | Reference Georgian-first LLM |
| GeoLogicQA | Koberidze, Elizbarashvili, Tsintsadze | 100 questions | unverified | "public resource" (repo location unverified) | aclanthology.org/2025.lowresnlp-1.13 | Verified (size) | LLMs 64–83% vs human 47% |
| Global-MMLU | Cohere et al. | 42 languages | Apache 2.0 | HF | cohere.com/research/globalmmlu | Verified (no Georgian, secondary) | Georgian MMLU remains a gap |
| Aya, Bactrian-X, xP3x; WikiANN ka; JRC sentiment; toxicity (Lashkarashvili & Tsintsadze 2022) | various | unverified | various | HF | n/a | Unverified | Check dataset cards before use |

### F. Speech

| Resource | Variety | Size | Licence | Access | URL | Status | Caveats |
|---|---|---|---|---|---|---|---|
| Common Voice 25.0 ka (scripted) | Modern Georgian | 227,399 clips; 323.49 h (167.53 h validated); 2,764 speakers; 134,521 sentences | CC0 | MDC download (no re-hosting) | datacollective.mozillafoundation.org/datasets/cmn2h4m7901gzo1072qn7zoes | Verified | Terms forbid speaker identification and re-sharing |
| CV Spontaneous Speech 2.0 ka | Modern Georgian | 118 clips, 7 speakers, ~1 h | CC0 | MDC | datacollective.mozillafoundation.org | Verified | Tiny |
| CV Mingrelian (xmf) | Megrelian | ≈12.63 h / 11.57 h validated / 89 speakers (unverified) | CC0 | MDC | datacollective.mozillafoundation.org | Unverified | OmniVoice lists 11.47 (h) for xmf |
| CV Laz (lzz) | Laz | unverified; added v24 | CC0 | MDC | datacollective.mozillafoundation.org/datasets/cmj8u3pei00fpnxxb2zv0zgwh | Verified (existence) | Script used in prompts not confirmed |
| IARPA Babel Georgian (LDC2016S12) | Eastern/Western dialects | ~190 h of conversational and scripted telephone speech collected 2014–2015 by Appen, speakers aged 16–73 (LDC catalogue); official training split 159 h (arXiv 1705.03152) | LDC | paid | catalog.ldc.upenn.edu | Verified | Conversational |
| MATERIAL (LDC2025S01) | Georgian | ~79 h of conversational telephone speech with transcripts, English translations, annotations and queries (LDC catalogue; Appen, IARPA MATERIAL) | LDC | paid | catalog.ldc.upenn.edu | Verified | n/a |
| DoReCo Svan | Svan | tokens/hours unverified | CC BY 4.0 | download | doreco.huma-num.fr/languages/svan1243 | Verified (licence) | Time-aligned; ka and en translations. Compiled by Jost Gippert 2002–2005 and processed for DoReCo by Ludger Paschen and Matthew Stave 2019–2022 (cite Gippert 2024, DOI 10.34847/nkl.9ba054c3) |
| FLEURS ka_ge; MMS; YODAS; OpenSLR | Georgian (MMS may cover more) | unverified | various | HF | n/a | Unverified | Confirm OpenSLR 153 language before use |

### G. OCR, manuscripts, handwriting

| Resource | Creator | Variety | Size | Licence | Access | URL | Status | Caveats |
|---|---|---|---|---|---|---|---|---|
| Tesseract kat, kat_old, script/Georgian | Tesseract project (Google) | Mkhedruli; Old Georgian | models | Apache 2.0 | GitHub | github.com/tesseract-ocr/tessdata | Verified (added v3.04, July 2015) | Training-data provenance undocumented; weak on degraded prints |
| tesseract-georgian (community) | D. Dohler | Mkhedruli | traineddata + training files; Wikipedia wordlists | Apache 2.0 | GitHub | github.com/ddohler/tesseract-georgian | Verified (2015 forum post) | Tesseract 3.x era |
| Georgian handwritten characters | Tsintsadze et al. 2018 | Mkhedruli | >200,000 character samples | unverified | unverified | sciencedirect.com/science/article/pii/S2405896318329525 | Verified (size) | Dataset release not confirmed |
| Calfa OCR/HTR + Calfa Vision | Calfa (Vidal-Gorène) | Georgian incl. manuscripts (9th–20th c. per Calfa) | models, commercial; annotation tool free | commercial / free tool | web | calfa.fr/ocr | Verified (Georgian supported) | No open Georgian HTR dataset found |
| Transkribus Old Georgian models; Sinai palimpsest imaging | various | Asomtavruli/Nuskhuri | unverified | n/a | n/a | n/a | Unverified | n/a |
| Manuscript image collections (Kekelidze Centre; NPLG Iverieli; BL; Bodleian; Sinai) | institutions | Old/Middle Georgian | unverified | per institution | online viewers | dspace.nplg.gov.ge | Unverified terms | BL holds Khutsuri MSS (e.g. Add. MS 11281) |

### H. Lexical resources

| Resource | Variety | Size | Licence | Access | URL | Status |
|---|---|---|---|---|---|---|
| Explanatory Dictionary of Georgian | Modern Georgian | unverified | unverified | web query | ganmarteba.ge; ena.ge | Unverified |
| Rayfield Comprehensive Georgian–English Dictionary (2006) | ka–en | unverified | copyrighted print | print | n/a | Unverified |
| GeoWordsDatabase | Georgian word list | ~310K words | unverified | GitHub | (listed in awesome-ka-nlp) | Unverified licence |
| Hunspell ka_GE; UniMorph kat; Kartu-Verbs (Lyon) | Georgian | unverified | various | download | n/a | Unverified |
| Kita Tschenkéli Georgisch–Deutsches Wörterbuch | ka–de | lexicon of the GNC analyser | copyrighted | embedded in GNC tools | n/a | Verified (as GNC analyser base) |
| Megrelian FLEx lexeme and morpheme dictionaries (MLC) | xmf–en | unverified | unverified | web | xmf.iliauni.edu.ge | Unverified counts |
| Laz lexicon (Önal & Tyers FST) | Pazar-Atina Laz | public lexicon | open (GitHub) | GitHub | github.com/esraonal/laz-morphological-analyser-fst | Verified |
| Georgian–Megrelian–Laz–Svan–English dictionary (TSU 2015); Kajaia, Kipshidze; Didi Lazuri Nenapuna; Gudjedjiani & Palmaitis; Topuria–Kaldani | xmf/lzz/sva | unverified | copyrighted print/PDF | print/PDF | n/a | Unverified |
| Georgian WordNet | n/a | none found | n/a | n/a | n/a | No evidence of a released resource |

### I–L. Megrelian, Laz, Svan and archive resources

| Resource | Creator | Variety | Size | Licence | Access | URL | Status |
|---|---|---|---|---|---|---|---|
| Megrelian Language Corpus (MLC) | Ilia State Univ. | Megrelian | 97,691 tokens; 60,959 types | unverified | query-only | xmf.iliauni.edu.ge | Verified |
| GNC Megrelian subcorpus | GNC | Megrelian | 89,404 words, unannotated | CC BY-NC (GNC) | query | gnc.gov.ge | Verified |
| Önal & Tyers Laz analyser | Önal, Tyers | Pazar-Atina Laz | 64.9% token coverage; test corpus 111,365 tokens (private) | open code | GitHub | aclanthology.org/R19-1101 | Verified |
| MorphLaz thesis | Boğaziçi | Laz | 78.2% unique-token coverage | thesis | repository | digitalarchive.library.bogazici.edu.tr/handle/123456789/15713 | Verified |
| TITUS Laz / Mingrelian (LINDAT LRT-957 / LRT-958) | Gippert | Laz, Megrelian | Laz ~900 tokens (unverified) | unverified | LINDAT | lindat.cz | Unverified |
| DoReCo Svan | Gippert | Svan | unverified | CC BY 4.0 | download; TLA source archive | doreco.huma-num.fr/languages/svan1243 | Verified |
| TLA (MPI): ECLinG Svan, SSGG, TMK Laz (Şahingöz & Rind-Pawlowski) | MPI Nijmegen | Svan, Laz, dialects | unverified | per deposit | registration | archive.mpi.nl | Unverified |
| ELAR (SOAS) Laz/Svan deposits; Pangloss; OLAC | various | lzz/sva | unverified | per deposit | registration | elararchive.org; olac.ldc.upenn.edu | Unverified |

## 4. Training-ready shortlist (bulk-downloadable, training-permissive)

| Language | Resources | Measured | Estimated post-dedup (label: ESTIMATE) |
|---|---|---|---|
| Georgian text | FineWeb-2 kat (ODC-By), HPLT 3.0 kat (CC0), MADLAD-400 ka (CC-BY-4.0/ODC-By), CulturaX ka (gated), Wikipedia (CC BY-SA), kona-sft-mix (ODC-By) | 1.44B words (FineWeb-2); 7.55B Gemma-3 tokens (HPLT); 2.62B tokens (CulturaX) | **ESTIMATE: ~1.5–2.5B unique words** after cross-set MinHash dedup. All four sets draw on Common Crawl; HPLT's Internet Archive crawls are the main source of new material. Low confidence |
| Georgian speech | Common Voice 25.0 (CC0) | 167.53 h validated; 323.49 h total | ~168 h clean, up to ~323 h if unvalidated clips are filtered by ASR confidence |
| Megrelian text | Wikipedia, CulturaX xmf, FineWeb-2 xmf, Leipzig xmf | 22,176 articles; 9,706 docs; ~4.12k rows; 114,288 tokens | **ESTIMATE: <5M words**, much of it Wikipedia, and only after Georgian-contamination filtering |
| Megrelian speech | CV xmf (CC0) | unverified (~11.5 h indicated) | ~11–12 h |
| Laz | Incubator Wp/Wt lzz (CC BY-SA), CV lzz | 3,837 Wt pages | **ESTIMATE: <1M words**; mostly Latin script |
| Svan | DoReCo Svan (CC BY 4.0), Incubator Wp/sva | unverified | **ESTIMATE: tens of thousands of words**; research-grade, not pretraining-grade |

Before training, exclude or ring-fence the non-permissive sets: CC BY-NC resources (GNC, OGLauRo) and the LDC corpora (Babel, MATERIAL).

## 5. Kartvelology shortlist (curated, annotated, diachronic, dialectal)

1. **GNC** (gnc.gov.ge): the only corpus that spans Old, Middle and Modern Georgian plus Megrelian, Svan and dialects, lemmatised with MSD tags.
2. **TITUS** (titus.uni-frankfurt.de): the scholarly base texts for Old Georgian and for Kartvelian fieldwork texts.
3. **GLC and oldcorpora** (Ilia): Modern texts 1832–2012, plus bilingual literary and historical subcorpora.
4. **UD treebanks**: Georgian-GLC, Georgian-GNC, Old Georgian-GLC, Old Georgian-OGLauRo. These allow cross-period syntactic comparison.
5. **MLC** (xmf.iliauni.edu.ge): the gold standard for Megrelian morphology (IPA, FLEx glossing, trilingual).
6. **DoReCo Svan**: time-aligned, glossed spoken Svan, openly licensed.
7. **Önal & Tyers Laz FST and MorphLaz**: the only computational Laz morphology.
8. **Digital Kartvelology** (journal, digitalkartvelology.adh.ge): the venue for current methods, e.g. Gippert (2025) on palaeographic dating of undated manuscripts.

## 6. Query-only and on-request resources: whom to approach

| Resource | Institution | Contact |
|---|---|---|
| GNC (all subcorpora, analyser) | CLARINO Bergen / Frankfurt / TSU | Paul Meurer (paul.meurer@uib.no); Jost Gippert |
| GLC, MLC, UD Georgian and Old Georgian GLC | Ilia State University | Irina Lobzhanidze |
| TITUS texts, DoReCo Svan source recordings | Goethe University Frankfurt; TLA | Jost Gippert |
| Laz Bucaklişi corpus | Laz Institute / İsmail Bucaklişi via Önal | Esra Önal; Francis Tyers |
| GREgORI Old Georgian | UCLouvain / Calfa | Bastien Kindt; Chahan Vidal-Gorène |
| TMK Laz, ECLinG Svan, SSGG | MPI TLA | via archive.mpi.nl deposit owners |
| kaTenTen24 | Lexical Computing | commercial licence |
| Babel, MATERIAL | LDC | LDC membership |

## 7. Gaps and in-progress projects (2025–2026)

- **Georgian:** There is no Georgian MMLU-style knowledge benchmark (Global-MMLU and MMLU-ProX exclude it), and FLORES+ is contaminated. GeoLogicQA (100 items) says it plans to expand and add a leaderboard, which is an announced intention rather than delivered work. No open Georgian manuscript HTR dataset exists. No Georgian WordNet has been released. The UD_Old_Georgian-GLC figures still need confirming.
- **Megrelian:** The MLC UD treebank is in preparation (LREC 2026). The CV xmf figures need confirming. No LID model reliably separates Megrelian from Georgian, so any web-derived xmf set needs manual auditing.
- **Laz:** Common Voice lzz is new (v24). The Incubator Wikipedia is still in test. The main text corpus is private, and script is split between Latin (Turkey) and Georgian (Georgia).
- **Svan:** Only DoReCo is openly licensed. The Incubator Wikipedia has no Meta request. No MT or LID resources were found. A Common Voice Svan set appears to exist: the Mozilla Data Collective lists "A collection of read speech recordings in Svan" among the related datasets on its Common Voice 25.0 Georgian datasheet. Its size is unverified.

## 8. Practical notes for Georgian-script AI training

- **Unicode blocks:** Georgian U+10A0–10FF (Asomtavruli U+10A0–10C5, Mkhedruli U+10D0–10FF), Georgian Supplement U+2D00–2D2F (Nuskhuri) and Georgian Extended U+1C90–1CBF (Mtavruli, the Mkhedruli capitals added in Unicode 11). Normalise Mtavruli to Mkhedruli with a case-fold mapping for training text; Mtavruli appears in headlines and all-caps. Keep Asomtavruli and Nuskhuri intact for Old Georgian work, or map them to Mkhedruli only as an explicit, reversible layer.
- **Byte and tokenizer cost:** Every Mkhedruli letter takes 3 bytes in UTF-8. FineWeb-2 kat works out to about 17.5 bytes per word, and HPLT kat to about 2.25 characters per Gemma-3 token. An ACL ARR 2024 submission on a Georgian corpus built from CulturaX found GPT-3.5/4 tokenizers spend about 2 tokens per Georgian character and GPT-3 about 3. This is why Kona2 added 20K Georgian vocabulary tokens. Plan for vocabulary extension or a Georgian-heavy tokenizer. The "~4.3× byte premium" figure is unverified; measure it on FLORES+ parallel text before quoting it.
- **Language ID:** Megrelian, Svan and Georgian-script Laz share Mkhedruli with Georgian, so web LID (GlotLID, CLD3, MADLAD's SSLID) will mislabel them. Use curated seed sets (MLC, Wikipedia) and character n-gram rules for Zan and Svan features, such as Megrelian ǯ-rich morphology and Svan vowel-length and umlaut diacritics.
- **Transliteration:** Laz in Turkey uses a Turkish-based Latin alphabet (with ç̌, ǩ, p̌, ť, ʒ, ǯ and similar), as in Wp/lzz/lat. Megrelian and Svan are normally written in Mkhedruli with extra letters and diacritics (e.g. ჷ, ჸ, ჲ, ჵ), and academic sources such as the MLC use IPA. Keep the original script and add a normalised parallel field. Do not transliterate destructively.

## Caveats

- OPUS per-corpus en–ka counts, CV xmf/lzz/v27 figures, the UD_Old_Georgian-GLC size, DoReCo Svan size, TITUS token counts and GNC per-subcorpus sizes were not retrievable this pass. They are marked unverified and should not be quoted as fact.
- The CulturaX, MADLAD-400 and Leipzig counts use different units (tokens, documents, whitespace tokens), so they cannot be summed. The post-dedup totals are estimates.
- Several pointers (GeoWordsDatabase, Global-MMLU's lack of Georgian, NVIDIA FastConformer WER) come from secondary lists such as awesome-ka-nlp or EasyGeorgian and are flagged as such.
- MADLAD-400's licence is stated inconsistently on its own card. Treat it as requiring attribution under either reading.