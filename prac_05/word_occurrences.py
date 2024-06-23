word_to_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1
sorted_words = sorted(word_to_count.keys())
max_length = max(len(word) for word in sorted_words)
for word in sorted_words:
    print(f"{word:{max_length}} : {word_to_count[word]}")
