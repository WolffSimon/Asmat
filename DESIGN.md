# Asmat: design considerations for a Georgian language model

Matthew Wolff Simon, mAIself. Version 0.1, 18 October 2026.

Asmat is a Georgian-language model in design at mAIself. This note gathers what the published evidence says about building one. It covers the tokeniser, the training text, the authorship of that text, the training method, evaluation, speech and OCR, and the law. Each section names the research brief it draws on; the briefs are in [briefs/](briefs/) and carry the full citations. Section 9 lists the decisions that are still open.

## 1. Starting position

Georgian is 0.0457% of the pages in Common Crawl. Russian has 146 times as many pages and English 916 times as many (brief 05). Among frontier model cards, only Qwen3 names Georgian as a training language (brief 05).

Tbilisi AI Lab's Kona2 is the only Georgian-first model found. The lab continued pre-training Mistral-Nemo on about 30 billion tokens of Georgian and English, added about 20,000 Georgian tokens to its vocabulary, and then tuned it with supervised fine-tuning and DPO. The weights are released under Apache 2.0. The lab has published no benchmark results, in Georgian or in English, and has not released the pre-training corpus (briefs 01 and 05).

The open web holds roughly 1.5 to 2.5 billion unique words of Georgian after deduplication, by the estimate in brief 01. A compute-optimal model of 7 billion parameters is trained on about 140 billion tokens, at about 20 tokens per parameter (Hoffmann et al. 2022). Georgian text alone cannot supply that, so the realistic route is continued pre-training of an existing multilingual model, which is the route Kona2 took.

## 2. Script and tokeniser

We measured how many tokens each of five tokenisers needs for the Universal Declaration of Human Rights in Georgian, divided by the number it needs for English. GPT-4's tokeniser and Llama 3's need 10.05 times as many. Qwen3 needs 5.40 times, Gemma 3 needs 2.08 times and GPT-4o's tokeniser needs 1.65 times (brief 02). Models are priced by the token and generate one token at a time, so the tokeniser changes the price of a Georgian answer, the time it takes and the amount of Georgian that fits in a context window.

Every Mkhedruli letter takes three bytes in UTF-8, and FineWeb-2's Georgian averages about 17.5 bytes per word (brief 01). Kona2 added Georgian tokens to Mistral-Nemo's vocabulary for this reason. Jais, SambaLingo and an Azerbaijani adaptation also extended their vocabularies, and nobody has tested the trade-off for Georgian script (brief 05).

Mtavruli, the capital forms of Mkhedruli added in Unicode 11, appear in headlines and all-caps text and can be folded to Mkhedruli before tokenising. Asomtavruli and Nuskhuri belong to Old Georgian and should stay intact, or be mapped to Mkhedruli only in a reversible layer (brief 01). Georgians also type their language in Latin letters. Glot500 holds 48,400 rows of romanised Georgian, which script-based detection cannot see (brief 05).

Our measurement used formal legal prose. Conversational Georgian and Latin-script Georgian may tokenise differently, and Claude's and Gemini's tokenisers are not published (brief 02). Any candidate tokeniser should be measured on all three kinds of text before a base model is chosen.

## 3. Training text

Four open web corpora carry most of the Georgian text: FineWeb-2 (1.44 billion words, ODC-By), HPLT 3.0 (7.55 billion Gemma 3 tokens, CC0), CulturaX (2.62 billion tokens, gated) and MADLAD-400 (936,497 documents). All four draw on Common Crawl and overlap heavily, so they must be deduplicated across sets. HPLT's Internet Archive crawls are the main source of material the others lack (brief 01). The corpora count in different units, words in one and tokens in another, so every figure should be quoted with its unit and its snapshot range (brief 05).

The CC0 and ODC-By licences on these corpora apply to the collection. Each crawled page keeps its own copyright, and anyone who trains on it carries that risk (brief 05).

Thompson et al. found that sentences translated into many languages at once score lower on quality, which is the signature of mass machine translation, and that low-resource languages carry more of them. They printed no figure for Georgian. FineWeb-2 does not detect machine translation at all. A manual audit of the mined English-Georgian pairs in WikiMatrix found 11.88% of them usable (brief 05). Kona2's instruction set is also largely machine-translated, with about 350,000 human-verified examples out of 2.6 million (brief 01). Filtering machine translation from Georgian text would need a Georgian translationese classifier, and none has been published.

The Georgian National Corpus holds over 200 million tokens, Ilia State University's Georgian Language Corpus over 100 million word-forms and Georgian Technical University's corpus.ge about 271 million tokens. All three offer a search interface only, and none states an open licence on its own site. The National Library's Iverieli collection holds 566,120 digitised documents, all rights reserved (brief 05). Brief 01 lists whom to approach for each.

RFE/RL, which publishes Radio Tavisupleba, prohibits the use of its content to train AI systems. OC Media is the only Georgian outlet found with a Creative Commons licence, and that licence is non-commercial. Most other news sites state no terms or reserve all rights (brief 05). Georgian Wikipedia has 199,138 articles and 346 active editors, about 575 articles for each editor (brief 05).

Megrelian, Svan and Georgian-script Laz share Mkhedruli with Georgian, and no language-identification model separates them reliably. Web subsets labelled Megrelian are probably mixed with Georgian. Laz in Turkey is written in a Latin alphabet (brief 01). Curated seed sets, such as Ilia State University's Megrelian Language Corpus and the Megrelian Wikipedia, are the starting point for any filter.

## 4. Who wrote the text

No study has measured how much of the text about Georgia was written in Georgia (brief 05). Text in Georgian may have been written or translated elsewhere. Brief 05 estimates that Russian-language web text about Georgia may equal or exceed the whole Georgian-language web subset, and labels that an estimate. In the text datasets audited by the Data Provenance Initiative, creator organisations in North America and Europe account for 93.8% of the tokens (brief 05). English Wikipedia's WikiProject Georgia tracks 12,498 pages, and 51% of its articles are stubs (brief 05).

Brief 05 judges that continued pre-training on general Georgian web text will not carry a Georgian view of history unless the corpus is curated for that content. When AceGPT adapted a model to Arabic, its answers moved towards an Egyptian survey and away from an American one, and the shift arrived together with forgetting (brief 05). Models from the United States, China and Europe gave very similar answers on values, so a model's country of origin does not guarantee a national outlook (brief 05).

Brief 05 sets out a four-stage pipeline for measuring authorship: an entity list for content about Georgia, several proxies for where each document was written, a test for translated origin and a measure of local editing on Wikipedia. Asmat's training mix should record the provenance of each document so that the share written in Georgia can be reported.

## 5. Training method

Continued pre-training raises fluency in the target language at 5 to 50 billion tokens and roughly 1,000 to 16,000 GPU-hours. Every study that measured English afterwards found it had fallen. Replaying about a quarter English data is the main remedy: one study lost 4.75 English points without replay and 1.5 with 25% replay (brief 05). On a tight budget of 8 billion German tokens, adaptation left Mistral-7B weaker in German and 15 to 18 points weaker in English (brief 05). In Armenian, the nearest regional case, continued pre-training on news alone improved fluency and eroded knowledge (brief 05).

CultureLLM tuned a model to a culture for about $6. An independent replication found that tuning on value-survey items made cultures more alike and cut general knowledge scores. Georgia is absent from the seventh wave of the World Values Survey and from every culturally grounded dataset found, so a Georgian fine-tune would need narrative and historical material (brief 05).

Durmus et al. attribute some of the American defaults in models to raters who are mainly North American. No published study has used raters from Georgia or anywhere in the Caucasus (brief 05). Kona2 was tuned with DPO on 387,319 preference pairs, released under ODC-By (brief 05).

## 6. Evaluation

INCLUDE holds 505 questions taken from Georgian exams and is the closest open test of local knowledge (brief 05). GeoLogicQA holds 100 logical-reasoning questions, on which models scored 64 to 83% against a human baseline of 47% (brief 01). Belebele has 900 reading-comprehension items (brief 05). FLORES+ is contaminated for Georgian, and Global-MMLU does not include Georgian (briefs 01 and 05).

Brief 04 sets the method. Native speakers write the items and native speakers grade them. Each task needs a few hundred items per community, because standard methods give error bars that are too narrow on small sets. Agreement between graders is reported as Krippendorff's alpha, with 0.800 for reliable data and 0.667 as the floor for tentative conclusions. A model may act as judge only after it passes a test against the human graders, such as the Alternative Annotator Test.

Across 21 judge models, raw agreement overstated chance-corrected agreement by 33.8 to 41.3 points. The authors propose reporting kappa or alpha, testing both answer orders and running each judgement at least three times (arXiv 2606.19544). Judges also score lower-resource languages more generously. Across 23 languages the correlation between resource level and reward was −0.81, and a per-language offset removed about 61% of the gap (arXiv 2607.14480, COLM 2026). A judge left uncorrected would inflate Georgian scores.

Asmat should be scored in English as well as Georgian, because continued pre-training costs English ability (section 5). Kona2 has no published results, so running INCLUDE, GeoLogicQA and Belebele on Kona2 and on frontier models would give the first public baseline (brief 05).

## 7. Speech and OCR

Common Voice 25.0 holds 323.49 hours of Georgian, of which 167.53 hours are validated, from 2,764 speakers, under CC0. Its terms forbid identifying speakers and re-hosting the data (brief 01). FLEURS adds about six hours. The IARPA Babel set (about 190 hours) and the MATERIAL set (about 79 hours) are conversational telephone speech behind paid LDC licences (briefs 01 and 05). For scale, OpenAI trained Whisper on 680,000 hours of audio across all its languages (Radford et al. 2022). Megrelian has about 11.5 hours in Common Voice, a figure still unverified, and Laz and Svan sets exist at sizes not yet confirmed (brief 01).

Tesseract has shipped Georgian and Old Georgian models since 2015, and they are weak on degraded print. No open dataset exists for recognising Georgian manuscript handwriting (brief 01). The National Library's digitised documents include 169,941 newspaper items, held as PDFs, and the library does not state whether they carry a text layer (brief 05). If the library licensed them, the quality of the OCR would decide how much usable text they yield.

## 8. Law, licensing and governance

Georgia's Law on Personal Data Protection (No. 3144, 2023) applies to controllers outside Georgia who use technical means in Georgia. It excludes processing for academic, artistic or literary purposes, permits processing of data that the subject has made public, and gives a right not to be subject to solely automated decisions. It does not address scraping. Its supervision moved to the State Audit Office on 2 March 2026 (brief 05).

Whether Georgian copyright law has an exception for text and data mining could not be verified. Georgia had no adopted national AI strategy or AI law as of 18 October 2026 (brief 05). If Asmat is offered in the European Union, Article 53 of the EU AI Act requires providers of general-purpose models to publish a summary of their training content and to respect opt-outs from text and data mining (brief 05).

The CARE Principles ask that communities share in the benefit of data about them and hold authority to control it. Masakhane combines open work with a stated commitment to data sovereignty. Te Hiku Media's Kaitiakitanga Licence requires permission before any use. Steven Bird has argued for keeping some corpora closed and tied to their place. Mozilla's Data Collective now allows community-governed or paid terms in place of CC0 alone (brief 05). Brief 04 covers recruitment, pay and credit for native-speaker authors and graders.

## 9. Open decisions

1. The base model: Kona2, which already carries Georgian vocabulary, or another open model, chosen after measuring tokenisers and running the same evaluation on each.
2. The tokeniser: keep the base vocabulary or extend it, judged on formal, conversational and Latin-script Georgian.
3. The web text: which corpora, which deduplication method, and how to filter machine translation.
4. The curated text: whether to seek licences from the Georgian National Corpus, Ilia State University and the National Library, and on what terms.
5. The Kartvelian languages: whether Megrelian, Svan and Laz are in the first version, given that language identification cannot yet separate them from Georgian.
6. The preference data: who rates it, how raters are recruited, paid and credited, and who governs the data afterwards.
7. The release terms for weights, data and evaluation sets.
8. Whether the first version includes speech.

## Sources

The five briefs carry the citations for every claim attributed to them. Four sources are cited here directly:

- Hoffmann et al., "Training Compute-Optimal Large Language Models", arXiv 2203.15556, March 2022, preprint, https://arxiv.org/abs/2203.15556
- Radford et al., "Robust Speech Recognition via Large-Scale Weak Supervision" (Whisper), arXiv 2212.04356, December 2022, preprint, https://arxiv.org/abs/2212.04356
- Judge agreement across 21 judge models and about 541,000 judgements, arXiv 2606.19544, June 2026, preprint, https://arxiv.org/pdf/2606.19544
- Judge leniency towards lower-resource languages, arXiv 2607.14480, COLM August 2026, peer-reviewed, as cited at https://www.alphaxiv.org/abs/2607.14480.md
