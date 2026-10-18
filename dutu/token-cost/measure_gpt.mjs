// Token counts for the aligned Common Voice strings on OpenAI's cl100k_base and o200k_base.
import fs from 'fs';
import * as o200k from 'gpt-tokenizer/encoding/o200k_base';
import * as cl100k from 'gpt-tokenizer/encoding/cl100k_base';
const langs = ["en", "ka", "xmf"];
const extra = ["ჷ", "ჸ", "ჲ", "ჵ", "ჶ", "ჳ"];
const out = { counts: {}, letters: {} };
for (const [name, enc] of [["cl100k", cl100k], ["o200k", o200k]]) {
  out.counts[name] = {};
  for (const l of langs) {
    const t = fs.readFileSync(`aligned/${l}.txt`, 'utf8').normalize('NFC');
    const ids = enc.encode(t);
    out.counts[name][l] = { tokens: ids.length, roundtrip: enc.decode(ids) === t };
  }
  // the Megrelian strings with the three letters Georgian lacks (ჷ, ჸ, ჲ) removed
  const noExtra = fs.readFileSync('aligned/xmf.txt', 'utf8').normalize('NFC').replace(/[ჷჸჲ]/g, '');
  out.counts[name].xmf_without_extra_letters = { tokens: enc.encode(noExtra).length, roundtrip: true };
  out.letters[name] = Object.fromEntries(extra.map(c => [c, enc.encode(c).length]));
}
fs.writeFileSync('gpt_counts.json', JSON.stringify(out, null, 1));
console.log(JSON.stringify(out));
