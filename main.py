# Find a common substring between two strings in Python

from difflib import SequenceMatcher

string1 = 'one two three four'
string2 = 'one two nine ten'

match = SequenceMatcher(None, string1, string2).find_longest_match(
    0, len(string1), 0, len(string2))

print(match)  # 👉️ Match(a=0, b=0, size=8)

# 👇️ one two
print(string1[match.a:match.a + match.size])

# 👇️ one two
print(string2[match.b:match.b + match.size])