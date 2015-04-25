problemName = 'histonum'

#file = open('..\\StudentData\\' + problemName + '.dat', 'r')
file = open('H:\\JudgesData\\' + problemName + '.dat', 'r')

dict = [0,0,0,0,0,0,0,0,0,0]
while True:
    myString = file.readline().strip()
    if myString == '': break;

    for char in myString:
        dict[int(char)] += 1

for i in range(10):
    if dict[i] == 0:
        continue
    stars = ''
    for j in range(dict[i]):
        stars += '*'
    strDict = str(dict[i])
    print str(i) + '|' + stars + " {" + str(dict[i]) + "}"