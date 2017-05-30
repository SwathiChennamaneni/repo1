#4. take a number from the user and check whether it is prime

num = input("Enter Number:")
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print "{0} is not a prime number".format(num)
            break
    else:
       	print "{0} is a prime number".format(num)
else:
    print "{0} is not a prime number".format(num)
