def censor(text, word):
    for x in text.split():
        if x == word:
            new_text = text.replace(word, ("*" * len(word)))
    print(new_text)
    return new_text

censor("this hack is wack hack", "hack")
