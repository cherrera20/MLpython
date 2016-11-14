import numpy as np

a = np.arange(15)
#print a
a = np.arange(15).reshape(3,5)
#print a
#print a.shape
#print a.ndim
#print a.dtype.name
#print type(a)

b = np.array([2, 3, 4])
#print type(b)
#print b.dtype.name
b = np.array([1.2, 3.5, 5.1])
#print b.dtype.name

c = np.array([(1.5,2,3), (4,5,6)])
#print c
#print 'complex type'
c = np.array( [ [1,2], [3,4] ], dtype=complex )
#print c

d = np.zeros( (3,4) )

d = np.ones( (2,3,4), dtype=np.int16 )
#print d
#print d.shape
#print d.ndim
d = np.empty( (2,3) )
#print d

e = np.arange( 10, 30, 5 )
#print e
e = np.arange( 0, 2, 0.3 )
#print e

from numpy import pi
e = np.linspace( 0, 2, 9 ) # 9 numbers from 0 to 2
#print e
x = np.linspace( 0, 2*pi, 100 )        # useful to evaluate function at lots of points
#print x
f = np.sin(x)
#print f

#Printing Arrays

#To disable this behaviour and force NumPy to print the entire array, you can change the printing options using set_printoptions.
#np.set_printoptions(threshold='nan')

#Basic Operations
a = np.array( [20,30,40,50] )
b = np.arange( 4 )
c = a-b
#print c
#print b*2
#print a<35
A = np.array( [[1,1], [0,1]] )
B = np.array( [[2,0], [3,4]] )

#print A*B                         # elementwise product
#print A.dot(B)                    # matrix product
#print np.dot(A, B)                # another matrix product

#Some operations, such as += and *=, act in place to modify an existing array rather than create a new one.
a = np.ones((2,3), dtype=int)
#print a
b = np.random.random((2,3))
#print b
a*= 3
#print a
b += a
#print b
#a += b  # b is not automatically converted to integer type

#When operating with arrays of different types, the type of the resulting array corresponds to the more general or precise one (a behavior known as upcasting).
a = np.ones(3, dtype=np.int32)
b = np.linspace(0,pi,3)
#print b.dtype.name float64
c = a+b
#print c
#print c.dtype.name
d = np.exp(c*1j)
#print d
#print d.dtype.name

#------UNARY OPERATIONS---------
a = np.random.random((2,3))
#print a
#print a.sum()
#print a.min()
#print a.max()

b = np.arange(12).reshape(3,4)
#print b
#print b.sum(axis=0)                            # sum of each column
#print b.min(axis=1)                            # min of each row
#print b.cumsum(axis=1)                         # cumulative sum along each row

#----universal funcitons------
B = np.arange(3)
#print B
#print np.exp(B)
np.sqrt(B)
C = np.array([2., -1., 4.])
#print B
#print C
#print np.add(B, C) #suma

#-------Indexing, Slicing and Iterating
a = np.arange(10)**3
#print a
#print a[2]
#print a[2:5] #5 exclusive
#a[:6:2] = -1000    # equivalent to a[0:6:2] = -1000; from start to position 6, exclusive, set every 2nd element to -1000
#print a
#print a[ : :-1]                                 # reversed a
#for i in a:
#    print(i**(1/3.))
print '--------------'
def f(x,y):
    return 10*x+y
b = np.fromfunction(f,(5,4),dtype=int)
#print b
#print b[2,3]
#print b[0:5, 1]  # each row in the second column of b
#print b[ : ,1]   # equivalent to the previous example
#print b[1:3, : ]  # each column in the second and third row of b
#print b[-1]  # the last row. Equivalent to b[-1,:]

c = np.array( [[[  0,  1,  2],               # a 3D array (two stacked 2D arrays)
                [ 10, 12, 13]],
               [[100,101,102],
                [110,112,113]]])
#print c.shape
#print c[1,...] # same as c[1,:,:] or c[1]
#print c[...,2] # same as c[:,:,2]

#Iterating over multidimensional arrays is done with respect to the first axis:
for row in c:
    print(row)
for element in c.flat:
    print(element)
