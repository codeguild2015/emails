txt = 'but soft what light in yonder window breaks'
words = txt.split()
print(words)
t = list()
print("The value of list is: ", list)
for word in words:
   t.append((len(word), word))

t.sort(reverse=True)

res = list()
for length, word in t:
    res.append(word)

print(res)
print(t)