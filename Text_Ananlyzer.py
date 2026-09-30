import re
import string
from collections import Counter

def get_words(text):
    return re.findall(r"\b[a-zA-Z0-9']+\b", text.lower())


def get_sentences(text):
    return [s for s in re.split(r"[.!?]+", text) if s.strip()]


def analyze_text(text):
    words = get_words(text)
    sentences = get_sentences(text)
    paragraphs = [p for p in text.split("\n") if p.strip()]
    lines = [line for line in text.split("\n") if line.strip()]

    total_words = len(words)
    unique_words = set(words)
    word_count = Counter(words)

    letters = [char for char in text if char.isalpha()]
    vowels = sum(char.lower() in "aeiou" for char in letters)
    consonants = len(letters) - vowels

    digits = sum(char.isdigit() for char in text)
    spaces = sum(char.isspace() for char in text)
    punctuation = sum(char in string.punctuation for char in text)

    characters = len(text)
    characters_no_spaces = sum(not char.isspace() for char in text)

    longest = max(words, key=len) if words else "None"
    shortest = min(words, key=len) if words else "None"

    average_word = (
        sum(len(word) for word in words) / total_words
        if total_words else 0
    )

    average_sentence = (
        total_words / len(sentences)
        if sentences else 0
    )

    reading_time = total_words / 200

    print("\n" + "=" * 35)
    print("         TEXT ANALYSIS")
    print("=" * 35)

    print("\nBASIC STATISTICS")
    print("-" * 35)
    print("Words:", total_words)
    print("Unique words:", len(unique_words))
    print("Characters:", characters)
    print("Characters without spaces:", characters_no_spaces)
    print("Lines:", len(lines))
    print("Paragraphs:", len(paragraphs))
    print("Sentences:", len(sentences))

    print("\nWORD STATISTICS")
    print("-" * 35)
    print("Longest word:", longest)
    print("Shortest word:", shortest)
    print(f"Average word length: {average_word:.2f}")
    print(f"Average sentence length: {average_sentence:.2f} words")

    if total_words:
        print(f"Vocabulary diversity: {len(unique_words) / total_words * 100:.2f}%")

    print("\nCHARACTER STATISTICS")
    print("-" * 35)
    print("Letters:", len(letters))
    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("Digits:", digits)
    print("Spaces:", spaces)
    print("Punctuation marks:", punctuation)
    print("Uppercase letters:", sum(c.isupper() for c in letters))
    print("Lowercase letters:", sum(c.islower() for c in letters))

    print("\nREADING TIME")
    print("-" * 35)
    print(f"Estimated reading time: {reading_time:.1f} minutes")

    print("\nMOST COMMON WORDS")
    print("-" * 35)

    for word, count in word_count.most_common(10):
        print(f"{word}: {count}")

    print("\nLEAST COMMON WORDS")
    print("-" * 35)

    if word_count:
        least_count = min(word_count.values())
        least_common = [
            word for word, count in word_count.items()
            if count == least_count
        ]

        for word in sorted(least_common):
            print(f"{word}: {least_count}")

    print("\n" + "=" * 35)


print("TEXT ANALYZER")
print("=" * 35)
print("Enter your text below.")
print("Press Enter twice to finish.\n")

lines = []

while True:
    line = input()

    if line == "":
        if lines and lines[-1] == "":
            break
        lines.append(line)
    else:
        lines.append(line)

text = "\n".join(lines).strip()

if text:
    analyze_text(text)
else:
    print("No text entered.")