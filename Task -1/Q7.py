s = 'Happiness can be found even in the darkest of times '         #str(input())
sentence_split = s.split()
print(sentence_split)
print(max(sentence_split, key=len )) # without len it will return the longest lexicographicly