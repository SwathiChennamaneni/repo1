#55. find out all perfect numbers in given range

how_many_num = input("In how many numbers you want to search perfect numbers: ")

for num in range(2, how_many_num + 1):
    sum = 0
    for i in range(1, num):
        if not num % i:
            sum += i
    if sum == num:
        print(num, "is a perfect number")
