import openpyxl
from googletrans import Translator
from deep_translator import GoogleTranslator
from pypinyin import pinyin, Style
import jieba.posseg as pseg
import os

# ---------------------------
# 1. SETUP TRANSLATORS
# ---------------------------
translator_primary = Translator()
translator_backup = GoogleTranslator(source='zh-CN', target='en')

# ---------------------------
# 2. LOAD EXCEL FILE
# ---------------------------
input_file = r"C:\Users\xlant\OneDrive\Desktop\SUBTLEX-CH-WF(1).xlsx"
output_file = r"C:\Users\xlant\OneDrive\Desktop\SUBTLEX-CH-WF-enriched.xlsx"

wb = openpyxl.load_workbook(input_file)
ws = wb.active

# Ensure headers exist
ws["B1"] = "Pinyin"
ws["C1"] = "English Translation"
ws["D1"] = "Part of Speech"
ws["E1"] = "Frequency Rank"

# ---------------------------
# 3. HELPER FUNCTIONS
# ---------------------------

def get_pinyin(text):
    """Return pinyin with tone marks"""
    return " ".join([item[0] for item in pinyin(text, style=Style.TONE3)])

def get_part_of_speech(word):
    """Return simplified POS using jieba"""
    words = pseg.cut(word)
    pos_tags = [f"{w.word}/{w.flag}" for w in words]
    return " ".join(pos_tags)

def translate_word(word):
    """Try googletrans first, fallback to deep-translator"""
    try:
        return translator_primary.translate(word, src='zh-CN', dest='en').text
    except Exception:
        try:
            return translator_backup.translate(word)
        except Exception:
            return "N/A"

def get_frequency_rank(word, freq_dict):
    """Look up frequency rank if you have a dictionary"""
    return freq_dict.get(word, "N/A")

# Optional: load frequency dictionary from CSV or manually
freq_dict = {}  # Example: {"我":1, "你":2}

# ---------------------------
# 4. MAIN LOOP
# ---------------------------
for row in range(2, ws.max_row + 1):
    word = ws[f"A{row}"].value
    if not word:
        continue

    # Pinyin
    ws[f"B{row}"] = get_pinyin(word)

    # Translation
    ws[f"C{row}"] = translate_word(word)

    # Part of speech
    ws[f"D{row}"] = get_part_of_speech(word)

    # Frequency
    ws[f"E{row}"] = get_frequency_rank(word, freq_dict)

    print(f"{word} → {ws[f'C{row}'].value} ({ws[f'D{row}'].value}) [{ws[f'E{row}'].value}]")

# ---------------------------
# 5. SAVE OUTPUT
# ---------------------------
wb.save(output_file)
print(f"✅ Enriched file saved as {output_file}")
