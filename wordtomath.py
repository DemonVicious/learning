import re
file = open('/home/demon/task1.txt', 'r')
text = file.read()
print(text)
wordlist = re.split(' |\n',text)
print(wordlist)
with open('/home/demon/task1_new.txt', 'w') as file_new:
    for word in wordlist:
        if word == ('one'):
            word = 1
            print(word, file = file_new)
        elif word == ('two'):
            word = 2
            print(word, file = file_new)
        elif word == ('three'):
            word = 3
            print(word, file = file_new)
        elif word == ('four'):
            word = 4
            print(word, file = file_new)
        elif word == ('five'):
            word = 5
            print(word, file = file_new)
        elif word == ('six'):
            word = 6
            print(word, file = file_new)
        elif word == ('seven'):
            word = 7
            print(word, file = file_new)
        elif word == ('eight'):
            word = 8
            print(word, file = file_new)
        elif word == ('nine'):
            word = 9
            print(word, file = file_new)
        elif word == ('zero'):
            word = 0
            print(word, file = file_new)
        else:
            print(word, file = file_new)
