problemName = 'practiceproblem'

#file = open('..\\StudentData\\' + problemName + '.dat', 'r')
file = open('H:\\JudgesData\\' + problemName + '.dat', 'r')

numLines = int(file.readline())

for i in range(numLines):
    print 'Let\'s play', file.readline().strip() + "!"