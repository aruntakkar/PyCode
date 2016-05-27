def reverse(text):
    x = ""
    for i in range(len(text)):
        x = x + text[len(text) - i - 1]
    return x

reverse("arun")
