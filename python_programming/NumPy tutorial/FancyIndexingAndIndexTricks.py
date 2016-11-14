import numpy as np
#------------Indexing with Arrays of Indices
a = np.arange(12)**2                       # the first 12 square numbers
#print a
#print '\n'
i = np.array( [ 1,1,3,8,5 ] )              # an array of indices
#print i
#print a[i]                                       # the elements of a at the positions i
#print '\n'

j = np.array( [ [ 3, 4], [ 9, 7 ] ] )      # a bidimensional array of indices
#print a[j]                                       # the same shape as j

palette = np.array( [ [0,0,0],                # black
                      [255,0,0],              # red
                      [0,255,0],              # green
                      [0,0,255],              # blue
                      [255,255,255] ] )       # white
#print palette
print '\n'
image = np.array( [ [ 0, 1, 2, 0 ],       # each value corresponds to a color in the palette
                    [ 0, 3, 4, 0 ]  ] )
#print palette[image]                            # the (2,4,3) color image

a = np.arange(12).reshape(3,4)
#print a
#print a.shape
i = np.array( [ [0,1],                        # indices for the first dim of a
                [1,2] ] )
#print i.shape
j = np.array( [ [2,1],                        # indices for the second dim
                [3,3] ] )
#print j.shape
#print a[i,j]                                     # i and j must have equal shape
a[i,2]
a[:,j]                                     # i.e., a[ : , j]
l = [i,j]
a[l]

#Another common use of indexing with arrays is the search of the maximum value of time-dependent series :
time = np.linspace(20, 145, 5)                 # time scale
data = np.sin(np.arange(20)).reshape(5,4)      # 4 time-dependent series
#print time
#print data
ind = data.argmax(axis=0)                   # index of the maxima for each series
#print ind
print '\n'
time_max = time[ ind]                       # times corresponding to the maxima
#print time_max
data_max = data[ind, xrange(data.shape[1])] # => data[ind[0],0], data[ind[1],1]...
#print time_max
#print data_max
np.all(data_max == data.max(axis=0))

#You can also use indexing with arrays as a target to assign to:
a = np.arange(5)
a[[1,3,4]] = 0

# However, when the list of indices contains repetitions, the assignment is done several times, leaving behind the last value:
a = np.arange(5)
#print a
a[[0,0,2]]=[1,2,3]
#print a

#This is reasonable enough, but watch out if you want to use Python’s += construct, as it may not do what you expect:
a = np.arange(5)
a[[0,0,2]]+=1
#print a

#Indexing with Boolean Arrays
a = np.arange(12).reshape(3,4)
#print a
b = a > 4
#print b   # b is a boolean with a's shape
#print a[b]  # 1d array with the selected elements
a[b] = 0  # All elements of 'a' higher than 4 become 0
#a
#The second way of indexing with booleans is more similar to integer indexing; for each dimension of the array we give a 1D boolean array selecting the slices we want.
a = np.arange(12).reshape(3,4)
b1 = np.array([False,True,True])             # first dim selection
print a
print b1
b2 = np.array([True,False,True,False])       # second dim selection
a[b1,:]                                   # selecting rows
a[b1]                                     # same thing
a[:,b2]                                   # selecting columns
a[b1,b2]                                  # a weird thing to do
