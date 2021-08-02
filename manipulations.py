# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a file containing functions for the manipulation of files.
We expect these functions to be used with readlines method before,
thus they mainly work on the created list of lines.
Please note that the list manipulated and returned generally contains
strings type objects.
"""

# Function to check that a file has constant number of columns.
# If true, returns number of raw and columns.
# If false return False and the number of the line with unconsistant number of column. 

def numbercolumn(lines):
    raw = len(lines)
    line1 = lines[0].split()
    length1 = len(line1)
    k = 1
    for k in range(1,len(lines)):
        line = lines[k].split()
        length = len(line)
        if length != length1:
            return(False,k+1)
        else:
            k+=1
    return(raw,k)

# Function that creates the list of columns from the lines of the file.
# It can also be used from columns to lines.
    
def linestocolumns(lines):
    line1 = lines[0].split()
    length1 = len(line1)
    allcolumns = []
    for k in range(length1):
        column = []
        for j in range(len(lines)):
            line = lines[j].strip().split()
            item = line [k]
            column.append(item)
        allcolumns.append(column)
    return(allcolumns)
        
# Function to extract lines with a specific list of strings starting at position n.
# It also returns the numerotation of the lines.

def lineswithstrings(lines,string,n):
    linesstrings = []
    numberlines = []
    for k in range(len(lines)):
        line = lines[k].split()
        i=0
        for j in range(len(string)):
            if (line[n+j]!=string[j]):
                i=1
        if i==0:
            linesstrings.append(line)
            numberlines.append(k)
    return(linesstrings,numberlines)

# Function to get items from a line based on their position.

def itemsline(line,i,j):
    items = line.split()
    listitem = []
    n = len(items)
    for k in range(n):
        if (i<=k<=j):
            item = items[k]
            listitem.append(item)
    return(listitem)

"""
Functions to change numerical values in a list of lists and turn them into file.
"""

# Function to check that a list of list of numbers has constant number of columns.
# Returns the number of raws and columns if it is true.

def dimensionlist(list1):
    n1 = len(list1)
    n2 = len(list1[0])
    for k in range(1,n1+1):
        length = len(list1[k])
        if length != n2:
            return(False)
    return(n1,n2)

# Function to transform list of lists of numbers into list of lists of string

def numbertostr(list1):
    lines = []
    n1 = len(list1)
    n2 = len(list1[0])
    for k in range(n1):
        line = []
        for i in range(n2):
            item = str(list1[k][i])
            line.append(item)
        lines.append(line)
    return(lines)

# Function to transform list of lists of strings into list of lists of numbers (float)

def strtonumber(list1):
    lines = []
    n1 = len(list1)
    n2 = len(list1[0])
    for k in range(n1):
        line = []
        for i in range(n2):
            item = float(list1[k][i])
            line.append(item)
        lines.append(line)
    return(lines)
    
# Function to transform list of list of string into written file

def strtofile(lines,file):
    n1 = len(lines)
    n2 = len(lines[0])
    with open(file,'w') as tofill:
        for k in range(n1):
            line = '  '
            for i in range(n2):
                line+=lines[k][i] + '  '
            line+='\n'
            tofill.write(line)
            
# Function to operate on the elements of a list of lists.
# This is usefull to change numerical value of a line of a file.
# We already assume it is rectangular.

def operation(list1,n,r,operation):
    if operation=='+':
        for j in range(len(list1[0])):
            item = list1[n][j]
            list1[n][j] = item + r
    elif operation=='-':
        for j in range(len(list1[0])):
            item = list1[n][j]
            list1[n][j] = item - r
    elif operation=='*':
        for j in range(len(list1[0])):
            item = list1[n][j]
            list1[n][j] = item * r
    elif operation=='/':
        for j in range(len(list1[0])):
            item = list1[n][j]
            list1[n][j] = item / r
            
# Function to add line at position n of a list of list.
# We already assume listtochange is rectangular and 
# listtoadd of the correct length.

def addline(listtochange,listtoadd,n):
    newlist = listtochange [:n]
    newlist += listtoadd
    newlist += listtochange[n:]
    return(newlist)