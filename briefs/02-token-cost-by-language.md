# Brief 02: Token cost by language on five tokenizers

Measured by Matthew Wolff Simon of mAIself on 14 October 2026 and rerun on 16 October 2026 with identical output. The scripts, pinned packages, raw counts and checksums are public at https://github.com/WolffSimon/token-premiums, where anyone can rerun the measurement.

Each figure is the number of tokens a tokenizer needs for the full Universal Declaration of Human Rights in a language, divided by the number it needs for English. A figure of 2.00 means twice as many tokens as English for the same text.

| Language | GPT-4 (cl100k) | GPT-4o (o200k) | Llama 3 | Qwen3 | Gemma 3 |
|---|---|---|---|---|---|
| Arabic (MSA) | 2.49 | 1.15 | 1.39 | 1.32 | 1.24 |
| Urdu | 4.21 | 1.63 | 2.89 | 3.15 | 1.51 |
| Hindi | 5.21 | 1.58 | 2.78 | 4.88 | 1.33 |
| Nepali | 4.26 | 1.30 | 2.24 | 4.00 | 1.18 |
| Bengali | 5.47 | 1.60 | 5.42 | 4.74 | 1.13 |
| Tamil | 8.82 | 2.35 | 8.82 | 6.91 | 1.76 |
| Malayalam | 7.89 | 1.73 | 7.81 | 6.45 | 1.55 |
| Tagalog | 2.22 | 1.78 | 2.20 | 2.21 | 1.89 |
| Georgian | 10.05 | 1.65 | 10.05 | 5.40 | 2.08 |
| English tokens (baseline) | 2207 | 2209 | 2207 | 2228 | 2404 |

Every tokenizer decoded its output back to the exact input text in every language.

## What it means for Georgian

Georgian is the most expensive language in the table on GPT-4's and Llama 3's tokenizers, at about ten times English. Llama 3 extends GPT-4's vocabulary, and its extra tokens evidently do not cover Georgian, because the two give identical counts. The tokenizer that arrived with GPT-4o brings Georgian down to 1.65 times. Qwen3 needs 5.40 times and Gemma 3 2.08 times. Since models are priced by the token and generate one token at a time, the choice of tokenizer changes the cost of a Georgian answer, the time it takes, and how much Georgian text fits in a context window, by about six times between the tokenizers measured here.

## Method

- Text: the udhr2 corpus distributed with NLTK, which comes from unicode.org; one complete translation per language, normalised to Unicode NFC.
- Tokenizers: cl100k_base and o200k_base from the gpt-tokenizer package 4.0.0; the Llama 3, Qwen3 and Gemma 3 tokenizer files from the @lenml packages 3.7.2, run with the Hugging Face tokenizers library 0.23.3. No special tokens were added.
- Measure: the parity premium of Petrov et al. (NeurIPS 2023), https://arxiv.org/abs/2305.15425, applied to a different parallel text.

## Agreement with published figures

- The GPT-4 column is within a fifth of Petrov et al.'s FLORES-200 figures for every language; Georgian is 10.05 against their 9.9.
- Hindi on Gemma 3 (1.33) and on Qwen3 (4.88) is close to the September 2026 preprint "The Invisible Language Tax" (1.34 and 4.56).

## Limits

- Claude's and Gemini's tokenizers are not published and were not measured.
- The Universal Declaration is formal legal prose. Conversational Georgian, and Georgian typed in Latin letters, may tokenize differently.
- Megrelian, Svan and Laz were not measured.
