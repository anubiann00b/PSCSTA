problemName = 'shuffle'

#file = open('..\\StudentData\\' + problemName + '.dat', 'r')
file = open('H:\\JudgesData\\' + problemName + '.dat', 'r')

while True:
    line = file.readline().strip()
    if line == '': break

    words = line.split(' ')
    dict = {}
    for word in words:
        dict[word] = word
    keys = dict.keys()
    keys.sort()

    finalString = ''
    for key in keys:
        finalString += key + " "
    print finalString