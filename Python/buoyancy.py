from math import ceil
problemName = 'buoyancy'

#file = open('..\\StudentData\\' + problemName + '.dat', 'r')
file = open('H:\\JudgesData\\' + problemName + '.dat', 'r')

numLines = int(file.readline())

for i in range(numLines):
    volume = float(file.readline().strip())
    print int(ceil(0.54/(0.011*volume)))