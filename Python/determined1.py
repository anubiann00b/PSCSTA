problemName = 'determined1'

#file = open('..\\StudentData\\' + problemName + '.dat', 'r')
file = open('H:\\JudgesData\\' + problemName + '.dat', 'r')

numLines = int(file.readline())

for i in range(numLines):
    row1 = file.readline().split(' ')
    row2 = file.readline().split(' ')
    print int(row1[0])*int(row2[1]) - int(row1[1])*int(row2[0])