i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
    print num

# use for-loop

for i in range(0, 6):
    numbers.append(i)

#for num in numbers:
#    print num
print numbers
