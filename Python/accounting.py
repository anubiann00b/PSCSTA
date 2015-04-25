from decimal import Decimal

problemName = 'accounting'

file = open('..\\StudentData\\' + problemName + '.dat', 'r')
#file = open('H:\\JudgesData\\' + problemName + '.dat', 'r')

print '****.****.****.****.****.****.****.****.'
print '       Transaction : Balance            '
sum = 0
while True:
    line = file.readline().strip()
    if line == '': break

    num = float(line.replace('$', '').replace(',', '').replace('(', '').replace(')', ''))

    if line.find('(') != -1:
        num = -num
    sum += num

    formatNum = str(sum)
    indexOfDot = formatNum.index('.')
    count = -1
    newOutput = formatNum[indexOfDot:]

    index = indexOfDot
    while index > 0:
        index -= 1
        if index == indexOfDot - 2: #first
            newOutput = formatNum[index] + newOutput
            count += 1
            continue
        if count % 2 == 0:
            newOutput = formatNum[index] + "," + newOutput
            index -= 1
        newOutput = formatNum[index] + newOutput

        count += 1


    finalString = line + ' : ' + newOutput
    padAmount = 20-finalString.index(':')-1
    paddedString = ''
    for i in range(padAmount):
        paddedString += ' '
    paddedString += finalString
    print paddedString
print '****.****.****.****.****.****.****.****.'
