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

translate =[]
for word in word_list:
    if word in words:
        translate.append(words[word])
    else:
        translate.append(f"[{word}]")
print(" ".join(translate))

translate_count =len(word_list) - sum(1 for word in word_list if word not in words)
untranslate_count =len(word_list) - translate_count
print("translateed: ", translate_count)
print("untranslate: ", untranslate_count)
