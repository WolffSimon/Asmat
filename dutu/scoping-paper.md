# Towards a Mingrelian large language model: a scoping study

Matthew Wolff Simon, mAIself. Working paper, version 0.1, 18 October 2026.

This is a working draft. The measurement of Georgian content in web text and the first baseline are planned for the next version. Figures marked unverified have not yet been checked against their primary sources.

## Abstract

Mingrelian (Megrelian; margaluri in Mingrelian, megruli ena in Georgian; ISO 639-3 xmf) belongs to the Kartvelian family. Estimates of its speakers range from about 300,000 to 500,000, and very little of it is digitised. This paper sets out what it would take to build a text language model for it.

The open text amounts to a few million words at most. It consists of one Wikipedia, two expert corpora of about 90,000 to 100,000 tokens each, small samples drawn from Wikipedia, and web-crawl subsets whose Georgian content nobody has measured. We measured the token cost: on tokenisers that handle Georgian well, Mingrelian needs 13 to 37% more tokens than Georgian for the same messages. We found no published accuracy on Mingrelian for any language-identification model, and no public evaluation set that includes it.

Evidence from Faroese and the Sorbian languages favours adapting a model trained on the closest large relative. For Mingrelian that means Kona2, an open Georgian model, trained further with Georgian text mixed back in and no new vocabulary. We propose four stages: measure the Georgian content of the web text, build an evaluation set written and graded by Mingrelian speakers, assemble a corpus by provenance, and only then compare training methods.

## Introduction

Published estimates put Mingrelian's speakers between about 300,000 and 500,000. The best-attested figure is Ethnologue's 345,530 from 2015 (Ethnologue, via Wikidata). None comes from a census question: the last census to record Mingrelian speakers was the Soviet census of 1926 (Sichinava, 2020).

The vitality ratings disagree. UNESCO's atlas rates Mingrelian definitely endangered, and the Endangered Languages Project rates it at risk. Ethnologue rates it stable, while noting that "direct evidence is lacking" (Ethnologue, 2026). Recent fieldwork by Ilia State University found that Georgian has replaced Mingrelian in the everyday language of children and young adults, with "a significant gap in generational transmission" (Lobzhanidze and Gersamia, 2025).

Language models are trained on digitised text, and very little Mingrelian is digitised. Mingrelian has had limited publication (Wikipedia, 2026), and nobody has counted how much of its printed record is digitised. No study has evaluated a language model on it. A model that reads and writes Mingrelian could support the corpus and dictionary work already in progress, and it would give speakers and learners a tool in their own language.

This paper asks five questions. What Mingrelian text exists, and how much of it is really Mingrelian? What does the language cost on current tokenisers? Which methods work for a language with little data and a close, larger relative? How should a model be evaluated? How should the work be shared with the people who speak the language?

The study covers text only. Speech is out of scope. It belongs to Dutu, a project in the Asmat repository, which also holds the design note for Asmat, a Georgian model (Simon, 2026).

## Writing and status

Mingrelian is written in the Georgian Mkhedruli script with a few extra letters. The most cited is ჷ (U+10F7), a schwa, whose use varies by dialect. Ilia State University's own data uses ჲ as well. In the Common Voice interface strings, ჷ, ჸ and ჲ together appear in 3% of Mingrelian words (Simon, 2026). No study has measured how consistently writers use them.

Mingrelian has no standard orthography, and we found no body that maintains one. One of the translators of the Gospel of Matthew, published in 2023, said that "there are no common grammar and spelling standards". The team chose to follow Georgian grammar while attending to the spoken language (Jehovah's Witnesses, 2023). We found no study of Mingrelian written in Latin letters, or of how much informal Mingrelian appears on social media.

The lack of a standard matters for every later step. A tokeniser, a language-identification model and an evaluation set all depend on how words are spelled. Spelling should therefore be surveyed across Wikipedia, published texts and social media before any normalisation is chosen.

Sources describe Mingrelian's relation to Georgian and Laz in different ways. ISO 639-3 lists it as an individual language with the code xmf, and the Georgian scholarly tradition groups Mingrelian and Laz together as Zan. This paper takes no position on these questions and uses the code xmf.

## Text resources

The largest openly measured Mingrelian training set is Goldfish's, at 1,367,040 tokens, or 5.44 MB after the project's byte-premium scaling against 1,000 MB for Georgian (Chang et al., 2026). No other downloadable resource has a published token count. The table lists what we found, and marks the figures we have not verified.

| Resource | What it is | Size | Licence | Access | Georgian content |
| --- | --- | --- | --- | --- | --- |
| Mingrelian Wikipedia | Encyclopedia, begun 2011 | 22,176 articles, 6 March 2026 (via Wikidata; unverified) | CC BY-SA | Dumps | Not measured; share of stubs unknown |
| Megrelian Language Corpus, Ilia State University | Fieldwork recordings transcribed in IPA, glossed, with Georgian and English translations | 97,691 tokens; 60,959 types | Given as both CC BY-SA 4.0 and CC BY-NC-SA 4.0 | Search interface; no bulk download found | Expert-made; low |
| Georgian National Corpus, Mingrelian subcorpus | Unannotated texts collected in the 20th century | 89,404 words | Reported as CC BY-NC (unverified) | Online query | Curated; low |
| Goldfish training set | Text assembled for the Goldfish models | 1,367,040 tokens | Not checked | Through the Goldfish project | Authors cannot rule it out |
| CulturaX, xmf subset | Web crawl drawn from mC4 and OSCAR | 9,706 documents | mC4 and OSCAR terms | Hugging Face, gated | Likely; not measured |
| FineWeb-2, xmf subset | Web crawl filtered by GlotLID | About 4,120 rows (unverified) | ODC-By 1.0 | Hugging Face | Likely; not measured |
| Leipzig Corpora, xmf\_wikipedia\_2012 | Sentences from Wikipedia | 10,191 sentences; 114,288 tokens | Leipzig terms | Download | As Wikipedia |
| Tatoeba, xmf | Single sentences with translations | Over 1,000 sentences (unverified) | CC BY 2.0 FR; part CC0 | Download | Low |
| Common Voice sentence corpus | Sentences written for recording | Not verified | CC0 | Mozilla Data Collective | Not measured |
| Gospel of Matthew, 2023 | Scripture, the first book of the Bible published in Mingrelian | One book | Presumed copyright | Web and print | Low |

**The printed record.** The digital resources are a small part of what has been printed. The oldest texts are 19th-century ethnographic material. Mkhedruli was used in Mingrelian publications from 1866 to 1906 and again in the 1930s, and several Mingrelian newspapers appeared between 1930 and 1938. Grammars followed in 1914 and 1920. Recent decades have added poetry collections, the journal Skani and religious publications (Wikipedia, 2026). Nobody has counted this record or checked how much of it is digitised.

**The expert corpora.** The Megrelian Language Corpus is the best-documented resource, built from fieldwork in Samegrelo between 2022 and 2024 (Megrelian Language Corpus team, 2026). Its narratives were transcribed first into IPA, so it cannot serve as Mkhedruli training text until a converter back to Mkhedruli is shown to be reliable. A 2025 paper by the same team states the licence as CC BY-SA 4.0 and abbreviates it as CC BY-NC-SA 4.0 (Lobzhanidze and Gersamia, 2025). The team needs to confirm which applies before anyone builds on it.

**Wikipedia.** Wikidata records 22,176 articles in Mingrelian Wikipedia in March 2026 (Wikidata, Q2029239). A journalist in Zugdidi has described it as full of "basic mistakes in vocabulary, syntax and grammar" (openDemocracy, n.d.). Its stubs, its bot-made articles and its Georgian content all need measuring before it counts as training text.

**Dictionaries and grammars.** Printed dictionaries include Kipshidze (1914), Kajaia's four-volume Mingrelian–Georgian dictionary (2000 to 2009) and Kobalia's, published online in 2010 and 2020. Ilia State University has built two online Mingrelian–English dictionaries from its corpus, one of lexemes and one of morphemes. They are the most useful aid for the dictionary-in-context method in the section on options.

## Our measurements

We have one measurement and propose two more. The first is complete and public. The second and third are planned for the next version of this paper.

### Token cost (complete)

On the three tokenisers that handle Georgian well, Mingrelian needs 13 to 37% more tokens than Georgian for the same messages. On the three that handle Georgian badly, the two cost about the same, at five to ten times English.

| Tokeniser | Georgian, against English | Mingrelian, against English | Mingrelian against Georgian |
| --- | --- | --- | --- |
| GPT-4o (o200k) | 1.84 | 2.52 | 1.37 |
| Gemma 3 | 2.24 | 2.67 | 1.19 |
| Mistral Nemo | 2.51 | 2.85 | 1.13 |
| Qwen3 | 5.18 | 4.99 | 0.96 |
| GPT-4 (cl100k) | 9.67 | 9.25 | 0.96 |
| Llama 3 | 9.67 | 9.25 | 0.96 |

The text is the Common Voice interface strings that exist in English, Georgian and Mingrelian. We excluded 107 Mingrelian strings that were identical to the Georgian, so that Georgian text is not counted as Mingrelian. The letters ჷ, ჸ and ჲ explain little of the gap: removing them lowers the Mingrelian count by 1.4% or less on every tokeniser. The scripts, counts and limits are public (Simon, 2026). Kona2's tokeniser, which adds about 20,000 Georgian vocabulary entries to Mistral Nemo's, has not been measured yet.

### Georgian content of web text (planned)

Nobody has measured how much of the web text labelled Mingrelian is Georgian. We propose to draw about 500 documents at random from each of CulturaX, FineWeb-2 and Wikipedia. Mingrelian speakers would label each as Mingrelian, Georgian or mixed. An automatic first pass would use the extra letters and Mingrelian-specific words and endings, and the speakers' labels would show how well it works. We will report each rate with a confidence interval.

### A first baseline (planned)

No study has measured how current models handle Mingrelian. We propose a small pilot test on sentences written and graded by native speakers, ahead of the full evaluation set: translation from Mingrelian into Georgian and English, scored by chrF and by native graders, and a set of comprehension questions. It would compare three systems: Kona2 with no help; Kona2 given the Ilia State University dictionary and retrieved example sentences in its prompt; and Goldfish's small Mingrelian model, by perplexity.

## Language identification

Two widely used language-identification models carry a Mingrelian label, and we found no published accuracy for either on Mingrelian. We found no published method for separating Mingrelian from Georgian text. FineWeb-2 was filtered with GlotLID, and CulturaX inherits the language identification of mC4 and OSCAR, so the web text labelled Mingrelian is only as reliable as these filters.

| Model | Mingrelian label | Published Mingrelian accuracy |
| --- | --- | --- |
| fastText lid.176 | Yes | None found |
| GlotLID v3 | Yes | None found |
| OpenLID | Probably not | Not applicable |
| MADLAD-400 | No | Not applicable |
| CLD3 | No | Not applicable |

fastText's model was trained on Wikipedia, Tatoeba and SETimes, so its Mingrelian label is learned mainly from Mingrelian Wikipedia and Tatoeba. Any Georgian in those sources becomes part of what the model treats as Mingrelian.

We propose a dedicated classifier. It would be a character n-gram model trained on the cleanest Mingrelian available against Georgian text. Its training text would be the Georgian National Corpus subcorpus, Tatoeba, the Gospel of Matthew and, once converted from IPA, the Megrelian Language Corpus. The extra letters and Mingrelian-specific endings would be its first features. We would test it, GlotLID and lid.176 on the speaker-labelled sample from the contamination study.

## Lessons from related pairs

In the cases we could verify, transfer from a close relative worked best. For Faroese it beat XLM-R, a massively multilingual model, on every task (Snæbjarnarson et al., 2023), and the two best Upper Sorbian systems relied on it (Libovický and Fraser, 2021). The organisers of the 2021 shared task on Sorbian concluded that "pre-training on parallel data in related language is important and that carefully applying known tricks can to a large extent compensate for using smaller datasets" (Libovický and Fraser, 2021).

| Small language | Related language | Target data | Method | Result |
| --- | --- | --- | --- | --- |
| Faroese | Icelandic, Danish, Norwegian, Swedish | 9 million words of web text | Encoders trained on Scandinavian languages, then trained further on Faroese | Best scores on named entities (91.4 F1) and sentence similarity (76.5); the tokeniser that never saw Faroese did best (Snæbjarnarson et al., 2023) |
| Upper Sorbian | Czech, with German | 147,000 parallel lines; 696,000 monolingual lines | German–Czech translation model fine-tuned on Sorbian, with back-translation | 67.3 BLEU into German and 66.3 BLEU from German, for the NRC-CNRC system (Libovický and Fraser, 2021) |
| Lower Sorbian | Upper Sorbian, Czech | 145,000 monolingual sentences; no parallel text | Started from the Upper Sorbian model, then iterative back-translation | 33.5 BLEU into German and 29.9 BLEU from German, for the NRC-CNRC system (Libovický and Fraser, 2021) |
| Kalamang (an unrelated control) | None | Fewer than 25,000 tokens, a grammar book and a word list | The whole grammar, word list and example sentences given to the model in its prompt | 44.7 and 45.8 chrF, against 51.6 and 57.0 for a person who learned from the same book (Tanzer et al., 2024) |

**Distance.** Georgian and Zan, the branch to which Mingrelian belongs, "diverged in the early Iron Age" (Gavashelishvili et al., 2023). No study has measured how much written Mingrelian a Georgian reader understands. Words that share roots with Georgian may be recognisable, and nearly all Mingrelian speakers also speak Georgian, so understanding probably runs mainly one way. A small intelligibility test with Georgian readers, using the word-translation and gap-filling tasks developed for closely related European languages (Gooskens et al., 2018), would measure it. It would also suggest how much a Georgian model can transfer without training. The shared script still gives the two languages many subwords in common. No published figure gives the share of vocabulary that Mingrelian and Georgian share. It can be computed from the 736 cognate sets in Gavashelishvili et al.'s supplementary data and from pairs of dictionary entries.

**A caution about Wikipedia.** In 2020 it emerged that one contributor who did not speak Scots had written about half of Scots Wikipedia, mostly in English with occasional Scots words (Engadget, 2020). Any small-language Wikipedia used as training text needs a check by speakers first.

## Options for building a model

The evidence supports starting from Kona2 and training it further on verified Mingrelian text, with Georgian mixed back in and the tokeniser left as it is. Kona2 is Tbilisi AI Lab's open Georgian model: Mistral Nemo with about 20,000 Georgian vocabulary entries added, trained further on about 30 billion tokens, then instruction-tuned and preference-tuned, with an Apache 2.0 licence (Tbilisi AI Lab, 2025). Five choices follow, cheapest first.

1. **A dictionary and examples in the prompt.** Kona2 or a frontier model receives entries from the Ilia State University dictionary and retrieved example sentences with each request. In the Kalamang work, retrieved parallel sentences helped most, word-list entries next and grammar passages least (Tanzer et al., 2024). This needs no training and can be tested at once. Its results for a language in Georgian script are untested.
2. **Further training of Kona2.** Kona2's base model is trained further on the verified Mingrelian corpus, with Georgian and English text mixed in. Training on the target language alone "markedly compromises" the model's English (Zhao et al., 2024), and the same risk applies to its Georgian. Low-rank adapters (LoRA) and full fine-tuning should both be tried: for Faroese, LoRA did better on grammatical acceptability and full fine-tuning on comprehension (Kunz et al., 2025).
3. **No new vocabulary.** For Faroese, the model whose tokeniser never saw Faroese did best (Snæbjarnarson et al., 2023). With about 1.4 million tokens of Mingrelian, new vocabulary entries would be poorly trained. Kona2 has already added Georgian-script entries, so its tokeniser should be measured on Mingrelian before anything changes.
4. **Synthetic text from Georgian, as an experiment.** We found no rule-based Georgian–Mingrelian translation system, so synthetic text would come from a language model or a dictionary. It risks producing Georgian in Mingrelian spelling. Any such text needs review by speakers before it enters training.
5. **A small model trained from scratch, as a baseline only.** Goldfish already provides a small Mingrelian model trained on its 1,367,040 tokens (Chang et al., 2026). It serves as a point of comparison.

## Evaluation plan

The evaluation set comes before any training, because without it nobody can show whether a Mingrelian model works. We found no public evaluation set that includes Mingrelian. Its absence from FLORES+, Belebele, SIB-200 and Global MMLU still needs confirming.

**Items.** We propose about 1,000 sentences that Mingrelian speakers translate from Georgian, following the FLORES design, so that translation can be scored in both directions. A few hundred minimal pairs would test the points of Mingrelian grammar that differ from Georgian. A set of comprehension questions would be written in Mingrelian from the start.

**Grading.** Two native graders mark every item, after calibration on a shared subset. Coarse rubrics may be easier to make reliable: in the Faroese work, two graders agreed at r = 0.879 on coarse summary scores and at r = 0.546 on fine-grained scores (Kunz et al., 2025). We will report chance-corrected agreement before settling any disagreement.

**Release.** The full set stays private, so that models cannot be trained on it. A sample is published with a marker string, and every item is dated. Authors and graders are paid and credited by name. We found no published pay rates or costs per item from comparable projects, so the budget will be set with the speakers and institutions that take part.

## Community, licensing and governance

The people who hold the cleanest data and the deepest knowledge of Mingrelian should shape the work and share in what it produces. The team at Ilia State University built the Megrelian Language Corpus and its dictionaries with funding from the Shota Rustaveli National Science Foundation (grant FR-21-993-3, 2021 to 2025). The Georgian National Corpus holds the 20th-century texts.

**Licences.** The licences limit what can be built. The corpus licence needs confirming: ShareAlike would require derived datasets to carry the same licence, and NonCommercial would bar commercial use. The Georgian National Corpus subcorpus is reported as non-commercial. The Gospel of Matthew is presumably still in copyright. Wikipedia is CC BY-SA.

**Models from other communities.** Te Hiku Media licenses te reo Māori data through its Kaitiakitanga licence, which treats data as held in guardianship, with benefits returning to the community. In 2022 the licence had not yet been used by any other organisation, and questions remained about its enforceability (MIT Technology Review, 2022). Masakhane built translation benchmarks for over 30 African languages through open participation, and credited contributors as co-authors (Nekoto et al., 2020).

**What we propose.** Contributors are paid and credited by name. The evaluation sample, the classifier, the measurements and the scripts are published with open licences. The speakers and institutions taking part decide how the full test set and any assembled corpus may be used. We found no published evidence on how speakers view technology for Mingrelian, so the work should ask them early.

## A staged plan, and gaps

The work runs in four stages, and the results of each stage show whether the next is worth doing.

1. **Measure.** Label the 500-document samples for Georgian content. Measure Kona2's tokeniser on Mingrelian. Compute the share of vocabulary that Mingrelian and Georgian share from the cognate data. Survey spelling. Test how much written Mingrelian Georgian readers understand. Compile a bibliography of printed Mingrelian and note what is digitised. Run the first baseline, including the dictionary-in-the-prompt method.
2. **Build the evaluation set.** Commission the translated sentences, the minimal pairs and the comprehension questions, and calibrate the graders.
3. **Assemble the corpus by provenance.** Start from the expert corpora, with their holders' permission and after conversion from IPA. Add audited Wikipedia articles and named publications. Digitise printed texts whose rights allow it, with text recognition trained on the extra letters. Use the new classifier on web text, and report what share it removes.
4. **Compare training methods.** Train Kona2's base model further on the corpus, with Georgian and English mixed in and no new vocabulary, by LoRA and by full fine-tuning. Test synthetic text as a separate experiment. Compare every result with the baseline and with Goldfish's model.

We have not estimated costs. Kona2's training compute is not published, and we found no annotator pay rates from comparable projects. Costs will be estimated once stage 1 shows how much clean text exists.

**Figures not yet verified.**

- Wikipedia's current article count, active editors and share of stubs need checking on its own statistics page.
- The sizes of the FineWeb-2 subset, the Tatoeba collection and the Common Voice sentence corpus are unconfirmed.
- GlotLID's published accuracy for each label may include Mingrelian.
- We have not confirmed whether FLORES+, Belebele, SIB-200 and Global MMLU include Mingrelian.
- The licences of the Megrelian Language Corpus and of the Georgian National Corpus subcorpus need confirming with their holders.
- The authors of the 2026 paper on the Megrelian Language Corpus, and the title of the 2025 Faroese study, are unconfirmed.

## References

- Chang et al. (2026). Goldfish: monolingual language models for 350 languages. LREC 2026. [arXiv 2408.10441](https://arxiv.org/html/2408.10441v2)
- CulturaX dataset card. [Hugging Face](https://huggingface.co/datasets/uonlp/CulturaX)
- Endangered Languages Project. Mingrelian. [Link](https://endangeredlanguages.com/elp-language/10906)
- Engadget (2020). Report on Scots Wikipedia. [Link](https://www.engadget.com/scots-wikipedia-230210674.html)
- Ethnologue (2026). Mingrelian. [Link](https://www.ethnologue.com/language/xmf/)
- fastText language identification (lid.176). [Link](https://fasttext.cc)
- FineWeb-2 dataset card. [Hugging Face](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2)
- Gavashelishvili et al. (2023). Scientific Reports. [PMC10689496](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10689496/)
- GlotLID. [Hugging Face](https://huggingface.co/cis-lmu/glotlid)
- Gooskens et al. (2018). Mutual intelligibility between closely related languages in Europe. International Journal of Multilingualism.
- Jehovah's Witnesses (2023). Book of Matthew released in Mingrelian. [Link](https://www.jw.org/en/news/region/georgia/Book-of-Matthew-Released-in-Mingrelian/)
- Kunz et al. (2025). Preprint on Faroese language models. [arXiv 2510.00810](https://arxiv.org/html/2510.00810)
- Leipzig Corpora Collection. xmf\_wikipedia\_2012. [Link](https://corpora.uni-leipzig.de/en?corpusId=xmf_wikipedia_2012)
- Libovický and Fraser (2021). Findings of the WMT 2021 shared tasks in unsupervised MT and very low resource supervised MT. WMT 2021. [Link](https://aclanthology.org/2021.wmt-1.72.pdf)
- Lobzhanidze and Gersamia (2025). eLex 2025. [Link](https://elex.link/elex2025/wp-content/uploads/eLex2025-34-LobzhanidzeGersamia.pdf)
- Megrelian Language Corpus, Ilia State University. [Link](https://xmf.iliauni.edu.ge/)
- Megrelian Language Corpus team (2026). Paper on the Megrelian Language Corpus. LREC 2026, pages 3250 to 3256. [Link](https://aclanthology.org/2026.lrec-1.255/)
- MIT Technology Review (2022). Artificial intelligence for the people. [Link](https://www.technologyreview.com/2022/04/22/1050394/artificial-intelligence-for-the-people/)
- Nekoto et al. (2020). Participatory research for low-resourced machine translation. Findings of EMNLP 2020. [Link](https://aclanthology.org/2020.findings-emnlp.195.pdf)
- openDemocracy (n.d.). Do you speak Mingrelian?
- Sichinava (2020). Lost in the census: Mingrelian and Svan languages face extinction in Georgia. CRRC Georgia. [Link](https://crrc.ge/en/lost-in-the-census-mingrelian-and-svan-languages-face-extinction-in-georgia/)
- Simon, M. W. (2026). Asmat and Dutu, with the Mingrelian token-cost measurement. [GitHub](https://github.com/WolffSimon/Asmat)
- Snæbjarnarson et al. (2023). Transfer to a low-resource language via close relatives: the case study on Faroese. NoDaLiDa 2023. [arXiv 2304.08823](https://arxiv.org/pdf/2304.08823)
- Tanzer et al. (2024). A benchmark for learning to translate a new language from one grammar book. ICLR 2024. [arXiv 2309.16575](https://arxiv.org/abs/2309.16575)
- Tbilisi AI Lab (2025). Kona2-12B model card. [Hugging Face](https://huggingface.co/tbilisi-ai-lab/kona2-12B)
- Wikidata. Mingrelian (Q13359), for the Ethnologue and UNESCO ratings. [Link](https://www.wikidata.org/wiki/Q13359)
- Wikidata. Mingrelian Wikipedia (Q2029239), for its article count. [Link](https://www.wikidata.org/wiki/Q2029239)
- Wikipedia (2026). Mingrelian language, accessed 18 October 2026, for the history of written Mingrelian. [Link](https://en.wikipedia.org/wiki/Mingrelian_language)
- Zhao et al. (2024). LLaMA beyond English: an empirical study on language capability transfer. Preprint. [arXiv 2401.01055](https://arxiv.org/abs/2401.01055)
