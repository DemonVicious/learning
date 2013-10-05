import re
file = open('/home/oleksandr/repos/learning/task1.txt', 'r')
text = file.read()

wordlist = re.split(' ',text)

output_string = ''

with open('/home/oleksandr/repos/learning/task1_new.txt', 'w') as file_new:
    for word in wordlist:
        if word == ('one'):
            output_string += '1'
        elif word == ('two'):
            output_string += '2'
        elif word == ('three'):
            output_string += '3'
        elif word == ('four'):
            output_string += '4'
        elif word == ('five'):
            output_string += '5'
        elif word == ('six'):
            output_string += '6'
        elif word == ('seven'):
            output_string += '7'
        elif word == ('eight'):
            output_string += '8'
        elif word == ('nine'):
            output_string += '9'
        elif word == ('zero'):
            output_string += '0'
        else:
            output_string += word
print(output_string)
