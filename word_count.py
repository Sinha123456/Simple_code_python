book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}
# first word count method.
for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1
print(word_counter)

# second word count method
word_count = {}
for word in book_title:
  word_count[word] = word_count.get(word, 0) + 1
print(word_count)