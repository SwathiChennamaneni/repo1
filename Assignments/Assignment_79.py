#79. WAP top remove substring form the given string without using replace function

user_string = raw_input("Enter String:")
sub_string = raw_input("Enter SubString:")
n = input("Enter occurences:")
try:
    for i in range(n):
        user_string = user_string[0:user_string.index(sub_string)]+ user_string[user_string.index(sub_string)+len(sub_string):]
except Exception :
    print "\nFound only {0} occurences and removed them".format(i)
finally:
    print "\nFinal String after removing substring:",user_string
