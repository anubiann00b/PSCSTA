problemName = 'cursed'

#file = open('..\\StudentData\\' + problemName + '.dat', 'r')
file = open('H:\\JudgesData\\' + problemName + '.dat', 'r')

months = {
    'January':'01',
    'February':'02',
    'March':'03',
    'April':'04',
    'May':'05',
    'June':'06',
    'July':'07',
    'August':'08',
    'September':'09',
    'October':'10',
    'November':'11',
    'December':'12',
}

while True:
    string = file.readline().strip()
    if string == '': break
    tokens = string.split(' ')
    month = months[tokens[0]]
    day = tokens[1].replace(',', '')
    if len(day) == 1:
        day = '0' + day
    while len(tokens[2]) < 4:
        tokens[2] = '0' + tokens[2]
    str = month+day+tokens[2]

    if str != str[::-1]:
        print str + ": OK TO TRAVEL"
    else:
        print str + ": DON'T TRAVEL"