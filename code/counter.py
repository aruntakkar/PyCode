from collections import Counter

text = "In February 2014, I made a recommendation to my co - founders at" \
    "Ballistiq that I wanted to cancel development of ArtStation." \
    "The project was in development hell. It wasn’t going anywhere." \
    "I was unhappy with it and just couldn’t see a path for it to be a"\
    "successful product. Two months later we managed to launch it," \
    "and two years later it is the leading network for professional games."

words = text.split()

Counter = Counter(words)

top_three = Counter.most_common(3)

print(top_three)
