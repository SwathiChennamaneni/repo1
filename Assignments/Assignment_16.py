#16. Take the input from the user for(Total number of people, toatl number of busses, Number of seats for bus). Based on the input
#Decide whether there is sufficient busses or not and give solution for how many extra busses required.
import math
buses = 2
persons = 109
seats = 25

need = (float(persons)/float(seats))- buses
print "Number of Buses still Needed:",math.ceil(need)

