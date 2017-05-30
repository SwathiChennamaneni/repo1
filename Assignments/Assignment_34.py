#34. Convert n dimentional list to single dimentiona list

old_list = [1,2,3,[11,22],4,5,6,[6,7,[33,44,55,66,77,88,[111,222,333,[1,2,3,[100,200,[888,555,[11111,22222]]]]]],3]]
#n_dimension_list = [[1,2,[2,3,4[4,5,6],[4,5]],5,6,],[[4,5,6],[3,4,5,6,7,8,9,7,8],[5,6],4,5,6]]
single_dimension_list = []
new_list = []

def my_fun(temp_list):
    for ele in temp_list:
        if type(ele) == list:
            my_fun(ele)
        else:
            new_list.append(ele)


my_fun(old_list)
print old_list
print new_list
