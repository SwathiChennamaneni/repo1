#32. l=[10,20,30,[40,50,60],70,[80,90,20]].
#Convert this list as sigle dimentiona list
old_list=[10,20,30,[40,50,60],70,[80,90,20]]
single_dimension_list = []
new_list = []

def my_fun(temp_list):
    for ele in temp_list:
        if type(ele) == list:
            my_fun(ele)
        else:
            new_list.append(ele)

my_fun(old_list)
print "Source List:",old_list
print "\nConverted Source List to Single Dimensional List:",new_list
