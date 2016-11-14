import numpy as np
#-----No Copy at All
a = np.arange(12)
#print a.shape
#print '\n'
b = a            # no new object is created
#print b
#print b is a           # a and b are two names for the same ndarray object
b.shape = 3,4    # changes the shape of a
#print b.shape
#print a.shape

def f(x):
    print(id(x))
#print id(a)   # id is a unique identifier of an object
#print f(a)

#----------View or Shallow Copy

#print '\n'
c = a.view()
#print c
#print c is a
#print c.base is a  # c is a view of the data owned by a

#print c.flags.owndata
c.shape = 2,6                      # a's shape doesn't change
#print a.shape

c[0,4] = 1234                      # a's data changes
print '\n'
#print a

#Slicing an array returns a view of it:
s = a[ : , 1:3]     # spaces added for clarity; could also be written "s = a[:,1:3]"
#print s
#print '\n'
s[:] = 10           # s[:] is a view of s. Note the difference between s=10 and s[:]=10
#print s
#print '\n'
#print a

#------------Deep Copy---------
print a
d = a.copy()                          # a new array object with new data is created
print d is a
print d.base is a                           # d doesn't share anything with a
d[0,0] = 9999
print a
