# Builds an aligned English-Georgian-Mingrelian text from the Common Voice interface strings.
# Input: corpus/cv/<locale>/**/*.ftl, taken from github.com/common-voice/common-voice at the commit in COMMIT.
# Output: aligned/<locale>.txt (one message per line, same order in every file) and aligned/stats.json.
import json, re, sys, unicodedata, pathlib
from fluent.syntax import parse, ast
LOCALES = ["en", "ka", "xmf"]
GEO = re.compile(r"[Ⴀ-ჿᲐ-Ჿⴀ-⴯]")

def pattern_text(p):
    out = []
    for el in p.elements:
        if isinstance(el, ast.TextElement):
            out.append(el.value)
        elif isinstance(el, ast.Placeable) and isinstance(el.expression, ast.SelectExpression):
            default = next(v for v in el.expression.variants if v.default)
            out.append(pattern_text(default.value))
        # other placeables ({ $var }, { -term }) are dropped
    return "".join(out)

def clean(s):
    s = re.sub(r"<[^>]+>", " ", s)             # markup such as <strong> and <lineBreak></lineBreak>
    s = re.sub(r"\s+", " ", s).strip()
    return unicodedata.normalize("NFC", s)

def load(loc):
    msgs = {}
    for f in sorted(pathlib.Path(f"corpus/cv/{loc}").rglob("*.ftl")):
        rel = f.relative_to(f"corpus/cv/{loc}").as_posix()
        for e in parse(f.read_text(encoding="utf8")).body:
            if isinstance(e, ast.Message):
                if e.value is not None:
                    msgs[(rel, e.id.name, "")] = clean(pattern_text(e.value))
                for a in e.attributes:
                    msgs[(rel, e.id.name, a.id.name)] = clean(pattern_text(a.value))
    return msgs

data = {l: load(l) for l in LOCALES}
keys = sorted(set.intersection(*(set(d) for d in data.values())))
stats = {"messages": {l: len(d) for l, d in data.items()}, "in_all_three": len(keys)}
drop = {"empty": 0, "not_georgian_script": 0, "xmf_same_as_en": 0, "xmf_same_as_ka": 0}
kept = []
for k in keys:
    en, ka, xmf = (data[l][k] for l in LOCALES)
    if not en or not ka or not xmf: drop["empty"] += 1; continue
    if xmf == en: drop["xmf_same_as_en"] += 1; continue
    if not GEO.search(ka) or not GEO.search(xmf): drop["not_georgian_script"] += 1; continue
    if xmf == ka: drop["xmf_same_as_ka"] += 1; continue
    kept.append(k)
stats["dropped"] = drop
stats["kept"] = len(kept)
pathlib.Path("aligned").mkdir(exist_ok=True)
for l in LOCALES:
    pathlib.Path(f"aligned/{l}.txt").write_text("\n".join(data[l][k] for k in kept) + "\n", encoding="utf8")
    stats.setdefault("characters", {})[l] = sum(len(data[l][k]) for k in kept)
    stats.setdefault("words", {})[l] = sum(len(data[l][k].split()) for k in kept)
json.dump(stats, open("aligned/stats.json", "w"), indent=1)
print(json.dumps(stats, indent=1))
