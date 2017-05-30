# Assignment 18
#Determine the factors of a number entered  by the user

user_input = input("Enter a number to findout its factors:")
Factor_List = []
for i in range(1,user_input+1):
    if user_input%i ==0:
        Factor_List.append(i)
print "\nFactors of {0} are:".format(user_input),Factor_List
