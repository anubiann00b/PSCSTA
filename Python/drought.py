problemName = 'drought'

#file = open('..\\StudentData\\' + problemName + '.dat', 'r')
file = open('H:\\JudgesData\\' + problemName + '.dat', 'r')

numLines = int(file.readline())

for i in range(numLines):
    nums = file.readline().split(' ')
    average = float(nums[0])
    nums = nums[1:]
    sum = 0
    for num in nums:
        sum += float(num)
    if sum > average*4:
        print 'drought over'
    elif sum >= average*2:
        print 'improving'
    else:
        print 'continuing'

