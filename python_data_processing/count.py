from read import load_data
import re
import collections
rows = load_data()
headlines = rows['headline']
words = ''
for row in headlines:
    lc = str(row).lower()
    words += lc
words = words.split(' ')

print(collections.Counter(words).most_common(100))

