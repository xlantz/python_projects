import pandas as pd
import time
from googletrans import Translator

# --- TONE MARK CONVERSION ---
def number_to_tone(pinyin):
    # Mapping of vowels with tone marks
    tone_marks = {
        'a': ['ā', 'á', 'ǎ', 'à'],
        'e': ['ē', 'é', 'ě', 'è'],
        'i': ['ī', 'í', 'ǐ', 'ì'],
        'o': ['ō', 'ó', 'ǒ', 'ò'],
        'u': ['ū', 'ú', 'ǔ', 'ù'],
        'ü': ['ǖ', 'ǘ', 'ǚ', 'ǜ'],
    }

    parts = pinyin.split()
    result = []
    for part in parts:
        if not any(ch.isdigit() for ch in part):
            result.append(part)
            continue
        tone = int(part[-1]) if part[-1].isdigit() else 0
        base = part[:-1]
        if tone in [1,2,3,4]:
            # Priority order for vowels
            for vowel in "a e o i u ü".split():
                if vowel in base:
                    base = base.replace(vowel, tone_marks[vowel][tone-1])
                    break
        result.append(base)
    return " ".join(result)

# --- SCRAPE FREQUENCY LIST ---
base_url = "https://en.wiktionary.org/wiki/Appendix:Mandarin_Frequency_list_{}-{}"
ranges = [(i, i + 999) for i in range(1, 10000, 1000)]

all_dfs = []

for start, end in ranges:
    url = base_url.format(start, end)
    print(f"Scraping {url}...")
    try:
        tables = pd.read_html(url)
        df = tables[0]
        df.columns = [c.strip().capitalize() for c in df.columns]
        expected_cols = ["Rank", "Character", "Pinyin", "English"]
        df = df[[col for col in df.columns if col in expected_cols]]
        all_dfs.append(df)
        time.sleep(1)
    except Exception as e:
        print(f"⚠️ Skipped {url} due to error: {e}")

# Combine all tables
full_df = pd.concat(all_dfs, ignore_index=True)

# --- CLEANUP ---
print("Cleaning pinyin tone marks...")
full_df["Pinyin"] = full_df["Pinyin"].astype(str).apply(number_to_tone)

# --- TRANSLATION ---
print("Translating with Google Translate (this may take several minutes)...")
translator = Translator()

translations = []
for i, word in enumerate(full_df["Character"]):
    try:
        trans = translator.translate(word, src="zh-CN", dest="en").text
        translations.append(trans)
    except Exception as e:
        translations.append("")
    if i % 100 == 0:
        print(f"Translated {i} / {len(full_df)}")
    time.sleep(0.1)

full_df["Translation"] = translations

# --- SAVE TO EXCEL ---
full_df.to_excel("mandarin_frequency_list_translated.xlsx", index=False)
print("✅ Saved to mandarin_frequency_list_translated.xlsx")
