import pandas as pd
import time

# --- Pinyin tone mark conversion function ---
def number_to_tone(pinyin):
    tone_marks = {
        'a': ['ā','á','ǎ','à'],
        'e': ['ē','é','ě','è'],
        'i': ['ī','í','ǐ','ì'],
        'o': ['ō','ó','ǒ','ò'],
        'u': ['ū','ú','ǔ','ù'],
        'ü': ['ǖ','ǘ','ǚ','ǜ'],
    }
    parts = pinyin.split()
    result = []
    for part in parts:
        if not any(ch.isdigit() for ch in part):
            result.append(part)
            continue
        tone = int(part[-1])
        base = part[:-1]
        if tone in [1,2,3,4]:
            for vowel in ['a','e','o','i','u','ü']:
                if vowel in base:
                    base = base.replace(vowel, tone_marks[vowel][tone-1])
                    break
        result.append(base)
    return " ".join(result)

# --- Load SUBTLEX-CH word frequency data ---
# Replace the path with the actual extracted file path
input_file = "SUBTLEX-CH-WF.csv"  # or .tsv depending on the download
df = pd.read_csv(input_file, encoding='utf-8')

# Inspect columns
print(df.columns.tolist())

# Example rename (adjust based on actual column names)
# Suppose columns: Word, Pinyin, English, Frequency, etc.
df = df.rename(columns={
    'Word': 'Word',
    'Pinyin': 'PinyinNumbered',
    'English': 'EnglishTranslation',
    'Frequency': 'Frequency'
})

# --- Clean Pinyin column ---
df['PinyinClean'] = df['PinyinNumbered'].astype(str).apply(number_to_tone)

# --- (Optional) Translation refresh ---
# If you want to refresh or fill missing English translations, you can integrate
# a free translation library or API. (See notes below.)

# --- Finalize and save ---
output_file = "subtlex_ch_words_cleaned.xlsx"
df.to_excel(output_file, index=False)
print(f"✅ Saved cleaned data to {output_file}")
