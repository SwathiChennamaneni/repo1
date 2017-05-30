# Defination of Dic Operations
# ADD: Appends the values of dissimilar keys and For Similar keys add the values of it and appends to a dictionary
# SUBTRACTION: Appends the values of dissimilar keys and For Similar keys subtract the values of it and appends to a dictionary
# MULTIPLICATION: Appends the values of dissimilar keys and For Similar keys multiplies the values of it and appends to a dictionary

class dic:
    def __init__(self, x = 0):
        self.x = x

    def __add__(self,other):
        d3={}
        d3.update(self.x)
        for i in other.x:
            if i in self.x:
                d3[i]=self.x[i]+other.x[i]
            else:
                d3[i]=other.x[i]
        return d3

    def __sub__(self,other):
        d3={}
        d3.update(self.x)
        for i in other.x:
            if i in self.x:
                d3[i]=self.x[i]-other.x[i]
            else:
                d3[i]=other.x[i]
        return d3

    def __mul__(self,other):
        d3={}
        d3.update(self.x)
        for i in other.x:
            if i in self.x:
                d3[i] = self.x[i]*other.x[i]
            else:
                d3[i]=other.x[i]
        return d3
                
        
p1 = dic({1:10,3:20})
p2 = dic({3:30,4:40})

print "Addition of Two Dictionaries:", p1+p2
print "Subtraction of Two Dictionaries:", p1-p2
print "Multiplication of Two Dictionaries:", p1*p2



