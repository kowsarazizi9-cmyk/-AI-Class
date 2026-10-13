words ={
    "eye": "چشم",
    "shoulder": "شانه",
    "blood": "خون",
    "young": "جوان",
    "pain": "درد",
    "strong": "قوی",
    "heart": "قلب",
    "bone": "استخوان",
    "i" : "من",
    "am" : "هستم"
}
sentence ="i am young boy"
word_list =sentence.lower().split()

translate = []

for word in word_list:
    if word in words:
        translate.append(words[word])
    else:
        translate.append(f"[{word}]")
print(" ".join(translate))

translate_count = 0
untranslate_count = 0

for word in word_list:
    if word in words:
        translate_count = translate_count + 1
    else:
        untranslate_count = untranslate_count + 1

print("translated: ", translate_count)
print("untranslate: ", untranslate_count)
