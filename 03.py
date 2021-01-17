# 03 円周率

import re

str1 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
str2 = re.sub('[.,]', '', str1)
str3 = re.split('\s', str2)
length = []

for word in str3:
    length.append(len(word))

print(length)
