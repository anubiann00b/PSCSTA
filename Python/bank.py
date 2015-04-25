problemName = 'bank'

#file = open('..\\StudentData\\' + problemName + '.dat', 'r')
file = open('H:\\JudgesData\\' + problemName + '.dat', 'r')

numCases = int(file.readline())

for i in range(numCases):
    str = file.readline().strip()
    numOps = int(file.readline())

    for j in range(numOps):
        case = file.readline().strip()

        inputs = case.split(" ")
        name = inputs[0]
        first = inputs[1]
        second = ""
        for s in range(0, len(inputs)-2):
            if s != len(inputs)-3:
                second += inputs[s+2] + ' '
            else:
                second += inputs[s+2]
        if name == "SEARCH":
            print str.index(second, int(first))+1
        elif name == "REPLACE":
            print str[:int(first)-1] + second + str[int(first):]
        elif name == "DELETE":
            print str[:int(first) - 1 ] + str[int(first) + int(second)-1:]
        elif name == "INSERT":
            print str[:int(first)-1] + second + ' ' + str[int(first)-1:]