import read
from collections import Counter
import re

data = read.load_data()
big_headline = ""

for line in data["headline"]:
    big_headline += str(line) + " "

big_headline = big_headline.lower()
words = re.findall(r'\w+', big_headline)
print(Counter(words).most_common(100))