import numpy as np

a = np.floor(10*np.random.random((3,4)))
#print a
#print a.shape
#a.ravel() # flatten the array
#a.shape = (6, 2)
#print a.T
#print a
#a.resize((2,6))
#print a

#If a dimension is given as -1 in a reshaping operation, the other dimensions are automatically calculated:
#print a.reshape(2,-1)

#--------Stacking together different arrays---------
"""
a = np.floor(10*np.random.random((2,2)))
print a
b = np.floor(10*np.random.random((2,2)))
print b
print '\n'
print np.vstack((a,b))
print '\n'
print np.hstack((a,b))
print '\n'
"""
#The function column_stack stacks 1D arrays as columns into a 2D array. It is equivalent to vstack only for 1D arrays:
from numpy import newaxis
#print np.column_stack((a,b))   # With 2D arrays
print '\n'
"""
a = np.array([4.,2.])
print a
b = np.array([3.,8.])
print '\n'
print b
print '\n'
print a[:,newaxis]  # This allows to have a 2D columns vector
print '\n'
print np.column_stack((a[:,newaxis],b[:,newaxis]))
print '\n'
print np.vstack((a[:,newaxis],b[:,newaxis])) # The behavior of vstack is different
"""
#print np.r_[1:4,0,4]

#---------Splitting one array into several smaller ones
a = np.floor(10*np.random.random((2,12)))
print a
print '\n'
print np.hsplit(a,3)   # Split a into 3
print '\n\n'
print np.hsplit(a,(3,4))   # Split a after the third and the fourth column
