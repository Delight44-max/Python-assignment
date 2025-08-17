def filter_pali(word):
    return word == word[::-1]


words = ["level", "madam", "python"]
print(list(filter(filter_pali, words)))
