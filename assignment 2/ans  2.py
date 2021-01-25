#program to remove duplicates from a sentence
from collections import Counter


def remove_duplicates(sentence):
    sentence = sentence.split(" ")
    for i in range(0, len(sentence)):
        sentence[i] = "".join(sentence[i])

    uniq_w = Counter(sentence)
    s = " ".join(uniq_w.keys())
    print(s)


if __name__ == "__main__":
    sentence = 'Python is great and Java is also great'
    remove_duplicates(sentence)
