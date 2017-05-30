#78. WAP to replace perticular number of substings with a given destination string

user_string = raw_input("Enter String:")
source_string = raw_input("Enter Source String:")
dest_string = raw_input("Enter Destination String:")
number = raw_input("Enter number of times to replace:")
print "\n"+user_string.replace(source_string,dest_string,int(number))
