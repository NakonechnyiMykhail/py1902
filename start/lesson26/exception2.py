import sys

List = ['a',0,2]

for entry in List:
    try:
        print('Entry is ', entry)
        value = 1 / int(entry)
        break
    except:
        print('Oops!', sys.exc_info()[0])
        print('Go next')
        print()

print('The reciprocal of ', entry, ' is ', value)