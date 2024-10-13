#Program for list of words
def sort_by_length(words):
    return sorted(words, key=len)


words = ['apple', 'banana', 'kiwi', 'cherry', 'pea', 'orange', 'blueberry']
sorted_words = sort_by_length(words)
print(sorted_words)

