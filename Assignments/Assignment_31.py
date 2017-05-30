# Assignment 31
#Take numbers from the user and findout min, maximum, sum, average

how_many_num = raw_input("How many digits you want to enter:")
num_list = []
sum_value = 0
i = 1
for i in range(1,int(how_many_num)+1):
    num = input("Enter {0}nd Number:".format(i))
    num_list.append(num)
print "\nMaximum Number among {0} are:".format(num_list), max(num_list)
print "\nMinimum Number among {0} are:".format(num_list), min(num_list)
print "\nSum of {0} is:".format(num_list),sum(num_list)
print "\nAverage of {0} is:".format(num_list),float(sum(num_list))/len(num_list)
