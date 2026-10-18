# Token cost of Megrelian on six tokenizers

Measured by Matthew Wolff Simon of mAIself on 18 October 2026, and rerun from a clean folder the same day with identical output.

Each figure is the number of tokens a tokenizer needs for a set of strings in one language, divided by the number it needs for the same strings in English. A figure of 2.00 means twice as many tokens as English. The strings are the 1,067 interface messages of Mozilla Common Voice that exist in English, Georgian and Megrelian.

| Tokenizer | Georgian | Megrelian | Megrelian ÷ Georgian | English tokens (baseline) |
|---|---|---|---|---|
| GPT-4 (cl100k) | 9.67 | 9.25 | 0.96 | 12,233 |
| GPT-4o (o200k) | 1.84 | 2.52 | 1.37 | 12,121 |
| Llama 3 | 9.67 | 9.25 | 0.96 | 12,229 |
| Qwen3 | 5.18 | 4.99 | 0.96 | 12,286 |
| Gemma 3 | 2.24 | 2.67 | 1.19 | 12,775 |
| Mistral-Nemo | 2.51 | 2.85 | 1.13 | 12,479 |

Every tokenizer decoded its output back to the exact input text in every language.

## What it shows

Megrelian costs more than Georgian on the three tokenizers that handle Georgian well. On GPT-4o's tokenizer Megrelian needs 2.52 times English and Georgian needs 1.84 times, a difference of 37%. The difference is 19% on Gemma 3 and 13% on Mistral-Nemo.

On the three tokenizers that handle Georgian badly, Megrelian and Georgian cost about the same: between nine and ten times English on GPT-4's and Llama 3's tokenizers, and about five times on Qwen3's. Megrelian comes out 4% cheaper there because its strings are 4% shorter, at 62,431 characters against 64,960.

Three letters in the Megrelian strings do not occur in Georgian: ჷ, ჸ and ჲ. They appear in 3% of Megrelian words. Removing them lowers Megrelian's token count by 1.4% or less on every tokenizer. Most of the extra cost therefore comes from Megrelian word forms that the tokenizers did not learn. A vocabulary extended for Megrelian would need those word forms as well as the letters.

Mistral-Nemo is the base model of Kona2, the Georgian-first model from Tbilisi AI Lab. Before Kona2 added its 20,000 Georgian tokens, Mistral-Nemo's tokenizer needed 2.51 times English for Georgian and 2.85 times for Megrelian. Kona2's own tokenizer was not measured (see Limits).

## Agreement with the Georgian measurement

The Georgian figures here are close to those measured on the Universal Declaration of Human Rights in [WolffSimon/token-premiums](https://github.com/WolffSimon/token-premiums): 9.67 against 10.05 on GPT-4's tokenizer, 1.84 against 1.65 on GPT-4o's, 5.18 against 5.40 on Qwen3's and 2.24 against 2.08 on Gemma 3's. For Georgian, the interface strings and the formal prose of the Declaration give a similar picture.

## Method

- **Text.** The Fluent (.ftl) localisation files for English (en), Georgian (ka) and Megrelian (xmf) in [github.com/common-voice/common-voice](https://github.com/common-voice/common-voice) at commit 96aff6ac498817e0cb6b0c6422d349812d4768c6 (18 October 2026). Mozilla publishes them under the Mozilla Public License 2.0. fetch_cv.sh fetches them, and they are not copied into this repository.
- **Alignment.** extract_cv.py keeps a message, or a message attribute, when all three locales have it: 1,186 messages. It drops variables and references, keeps the default variant of each plural or select expression, removes markup tags, collapses whitespace and normalises the text to Unicode NFC.
- **Exclusions.** 107 Megrelian strings were identical to the Georgian and were excluded, so that Georgian text is not counted as Megrelian. Nine had no Georgian-script text in the Georgian or Megrelian version, two Megrelian strings were identical to the English, and one was empty. 1,067 strings remain, with 9,770 English words, 7,749 Georgian words and 7,516 Megrelian words. aligned_stats.json holds these counts and aligned.sha256 the checksums of the aligned texts.
- **Tokenizers.** cl100k_base and o200k_base from the gpt-tokenizer package 4.1.0. The Llama 3, Qwen3, Gemma 3 and Mistral-Nemo tokenizer files from the @lenml packages 3.7.2, run with the Hugging Face tokenizers library 0.23.3. No special tokens were added. package-lock.json pins every version.
- **Measure.** The parity premium of Petrov et al. (NeurIPS 2023), https://arxiv.org/abs/2305.15425.
- **Letters check.** The scripts also count the Megrelian text with ჷ, ჸ and ჲ removed. The result is the last column of premiums.csv.

To rerun, with Node.js and Python 3, fluent.syntax and tokenizers 0.23.3 installed:

```
./fetch_cv.sh
npm ci
python3 extract_cv.py
node measure_gpt.mjs
python3 measure_hf.py
python3 compute_premiums.py
```

## Limits

- Interface text is short and practical, and volunteers translated it from English, so its word order and vocabulary may follow English. It is one register of each language.
- The sample is small, at about 12,000 English tokens.
- Some of the 107 excluded strings will be words that Megrelian and Georgian share, and some may be Georgian left untranslated. The measurement cannot tell them apart.
- Kona2's tokenizer was not measured, and neither was Megrelian text from other sources such as Wikipedia, because Hugging Face and Wikipedia could not be reached from the environment where the measurement ran.
- Claude's and Gemini's tokenizers are not published and were not measured.

## Licence

The scripts and package files are released under the MIT licence (see [../../LICENSE-CODE](../../LICENSE-CODE)). The counts, premiums and this README are released under CC BY 4.0 (see [../../LICENSE](../../LICENSE)). Copyright 2026 Matthew Wolff Simon.
