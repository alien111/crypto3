import random
import string
from random_word import RandomWords

"""
# random letters
file1 = open('randomletters1.txt', 'w')
file2 = open('randomletters2.txt', 'w')

for i in range(978):
	file1.write(random.choice(string.ascii_letters))
	file2.write(random.choice(string.ascii_letters))

file1.close()
file2.close()
"""

"""
#random words
file1 = open('randomwords1.txt', 'w')
file2 = open('randomwords2.txt', 'w')

r = RandomWords()

for i in range(100):
	file1.write(str(r.get_random_word()))
	file2.write(str(r.get_random_word()))


file1.close()
file2.close()
"""

#random words with separator
file1 = open('randomwordswithseparator.txt', 'w')

r = RandomWords()

for i in range(100):
	file1.write(str(r.get_random_word()) + ' ')


file1.close()