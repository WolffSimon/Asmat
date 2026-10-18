# Parity premium: tokens for a language divided by tokens for English on the same strings and tokenizer.
import json
c = {**json.load(open("gpt_counts.json"))["counts"], **json.load(open("hf_counts.json"))["counts"]}
order = ["cl100k", "o200k", "llama3", "qwen3", "gemma3", "mistral_nemo"]
assert all(v["roundtrip"] for m in c.values() for v in m.values()), "a tokenizer failed to round-trip"
prem = {m: {"ka": round(c[m]["ka"]["tokens"] / c[m]["en"]["tokens"], 2),
            "xmf": round(c[m]["xmf"]["tokens"] / c[m]["en"]["tokens"], 2),
            "xmf_over_ka": round(c[m]["xmf"]["tokens"] / c[m]["ka"]["tokens"], 2),
            "xmf_without_extra_letters": round(c[m]["xmf_without_extra_letters"]["tokens"] / c[m]["en"]["tokens"], 2)} for m in order}
json.dump(prem, open("premiums.json", "w"), indent=1)
with open("premiums.csv", "w") as f:
    f.write("tokenizer,english_tokens,georgian_tokens,megrelian_tokens,georgian_premium,megrelian_premium,megrelian_over_georgian,megrelian_premium_without_extra_letters\n")
    for m in order:
        f.write(f"{m},{c[m]['en']['tokens']},{c[m]['ka']['tokens']},{c[m]['xmf']['tokens']},{prem[m]['ka']},{prem[m]['xmf']},{prem[m]['xmf_over_ka']},{prem[m]['xmf_without_extra_letters']}\n")
print(open("premiums.csv").read())
