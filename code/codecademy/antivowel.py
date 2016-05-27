def anti_vowel(text):
    new_text = ""
    for i in text:
        if i not in "aeiouAEIOU":
            new_text += i
    print(new_text)
    return new_text


anti_vowel("arun")
