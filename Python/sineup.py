import math

def round(x):
    m = int(x*10)
    if m%10>=5:
        return math.ceil(x)
    return math.floor(x)
problemName = 'sineup'

#file = open('..\\StudentData\\' + problemName + '.dat', 'r')
file = open('H:\\JudgesData\\' + problemName + '.dat', 'r')


while True:
    string = file.readline().strip()
    if string == '': break
    vals = string.split(' ')
    diam = int(vals[0])
    angleA = int(vals[1])
    angleB = int(vals[2])
    angleC = 180 - angleA - angleB
    A = str(int(round(diam*math.sin(angleA*math.pi/180))))
    B = str(int(round(diam*math.sin(angleB*math.pi/180))))
    C = str(int(round(diam*math.sin(angleC*math.pi/180))))
    print 'Circumcircle diameter = ' + str(diam)
    print('Angles are ' + str(angleA) + ', ' + str(angleB) + ' and ' + str(angleC))
    print('Corresponding sides are ' + A + ', ' + B + ' and ' + C)