import pprint
'''Counting the frequency of letter in a given message'''
message = "I am working everyday on Python programming"
count = {}

for char in message:
    count.setdefault(char,0)
    count[char] = count[char] + 1
pprint.pprint(count)

