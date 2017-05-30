"""76.  write a class program to demonstrate method overloading in python using
below scenario.Write a class and constructor to create an instances like below
a. p1 = person(id=1,name="ashok",age=23,sal=56787)
b. p2 = person(id=2,age=24,adhar=23456)
c. p3 = person(id=4,pan="brcp3456",sal=23,age=45)	
make instance iterable and provide the operations p1+p2, p1-p2.
Give your own definition for the operations"""

#My Defination on Operations
#Add: Returns Union of both the instances and for the common keys their values will be in the form of List
#Subtraction: Returns only the values of common keys as List
class person(object):
    def __init__(self,**kwargs):
        self.kwargs = kwargs

    def __str__(self):
        return "({0},{1})".format(self.kwargs,other.kwargs)

    def __iter__(self):
        yield self.kwargs.get('ids')
        yield self.kwargs.get('name')
        yield self.kwargs.get('age')
        yield self.kwargs.get('sal')
        yield self.kwargs.get('adhar')
        yield self.kwargs.get('pan')
        
        
    
    def __add__(self,other):
        d3={}
        d3.update(self.kwargs)
        for i in other.kwargs:
            if i in self.kwargs:
                d3[i]=[self.kwargs[i],other.kwargs[i]]
            else:
                d3[i]=other.kwargs[i]
        return d3

    def __sub__(self,other):
        d3={}
        for i in other.kwargs:
            if i in self.kwargs:
                d3[i]=[self.kwargs[i],other.kwargs[i]]
        return d3

        
p1 = person(id=1,name="ashok",age=23,sal=56787)
p2 = person(ids=2,age=24,adhar=23456)
p3 = person(ids=4,pan="brcp3456",sal=23,age=45)

print "** Wtih Keyword Args **\n"
print "Iteration on p1 Instance..\n"
for i in p1:
    print i

print "\n**My Defination on Operations**"
print "\nAdd: Returns Union of both the instances and for the common keys their values will be in the form of List"
print "\nSubtraction: Returns only the values of common keys as List"
print "\n***Output***"
print "\nAddition:\n",p1+p3
print "\nSubtraction:\n",p1-p2
