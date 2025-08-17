def get_words_longer_than_five(word):
    return len(word) > 5



words = ["cat", "elephant", "tiger", "lion"]

print(list(filter(get_words_longer_than_five, words)))