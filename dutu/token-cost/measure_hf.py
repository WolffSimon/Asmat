# Token counts for the aligned Common Voice strings on the Llama 3, Qwen3, Gemma 3 and Mistral-Nemo tokenizers.
import json, unicodedata
from tokenizers import Tokenizer
langs = ["en", "ka", "xmf"]
extra = ["ჷ", "ჸ", "ჲ", "ჵ", "ჶ", "ჳ"]
texts = {l: unicodedata.normalize("NFC", open(f"aligned/{l}.txt", encoding="utf8").read()) for l in langs}
out = {"counts": {}, "letters": {}}
for m in ["llama3", "qwen3", "gemma3", "mistral_nemo"]:
    tk = Tokenizer.from_file(f"node_modules/@lenml/tokenizer-{m}/models/tokenizer.json")
    res = {}
    for l, t in texts.items():
        enc = tk.encode(t, add_special_tokens=False)
        res[l] = {"tokens": len(enc.ids), "roundtrip": tk.decode(enc.ids, skip_special_tokens=False) == t}
    no_extra = texts["xmf"].replace("ჷ", "").replace("ჸ", "").replace("ჲ", "")
    res["xmf_without_extra_letters"] = {"tokens": len(tk.encode(no_extra, add_special_tokens=False).ids), "roundtrip": True}
    out["counts"][m] = res
    out["letters"][m] = {c: len(tk.encode(c, add_special_tokens=False).ids) for c in extra}
json.dump(out, open("hf_counts.json", "w"), indent=1)
print(json.dumps(out))
