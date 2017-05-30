#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

infile=open("D:\README.txt", "r")

edges=[]
count=0
#count the total number of lines in the file
for line in infile:
 count=count+1

total=count

print "With Sample File"
print "Total number of lines: ",total

infile.seek(0)
count=0
for line in infile:
    edge=tuple(map(str,line.strip().split(",")))
    edges.append(edge)
    count=count+1
    #for every million lines print memory consumption
    if count%1000000==0:
        print "Position: ", edge
        print "Read ",float(count)/float(total)*100,"%."
        mem=sys.getsizeof(edges)
        for edge in edges:
            mem=mem+sys.getsizeof(edge)
            for node in edge:
                mem=mem+sys.getsizeof(node)
        print "Memory (Bytes): ", mem
