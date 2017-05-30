# Assignment 17
#17. Print the first 100 odd numbers

Odd_Numbers = []
for i in range(101):
    if not i%2 == 0:
        Odd_Numbers.append(i)
print "First 100 Odd Numbers:",Odd_Numbers
