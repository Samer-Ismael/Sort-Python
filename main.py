
word = input("Enter the numbers: ")
word1 = ""

for x in range(len(word)):
    if word[x] == "+":
        continue
    word1 = word1 + (word[x])
sort = sorted(word1)
final = ""
for i in range(len(sort)):
    final += sort[i]
    if 0 <= i < len(sort) - 1:
        final += "+"

print(final)
