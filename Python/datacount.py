files = ['accounting.dat',
'bank.dat',
'buoyancy.dat',
'cross.dat',
'cursed.dat',
'determined1.dat',
'determined2.dat',
'drought.dat',
'histonum.dat',
'shuffle.dat',
'sineup.dat',
'splatter.dat']

count = 0
for fileName in files:
    #file = open('..\\StudentData\\' + fileName, 'r')
    file = open('H:\\JudgesData\\' + fileName, 'r')
    for line in file:
        count += 1
print 'THERE ARE', count, 'LINES OF DATA FOR THIS PACKET'