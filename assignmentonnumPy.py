# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 14:06:25 2023

@author: ACER
"""

"""
write a NumPy program  to get the numpy version 
and show the numpy
"""
import numpy as  np
print(np.__version__)

##################################
'''
write numpy program to test whether 
none of the elements of a given array are zero
'''

import numpy as np
x= np.array([1,2,3,4])
print("Original array")
print(x)
print("test if none of the elememnts of the said array is zero")
print(np.all(x))
x=np.array([0,1,2,3])
print("Original array")
print(x)
print("test if none of the elements of the said array is zero:")
print(np.all(x))
###############################################

'''
write numpy program to test if any of the element
of a given array are non zero.
'''

#import numpy program to test if
#any of the element of a given array are non 

import numpy as np
x=np.array([1,0,0,0,0])
print("original array")
print(x)

print("twst whether any of the element of a given array")
print(np.array(x))
x=np.array([0,0,0,0])
print(x)
print(np.any(x))


#############################################
'''
write numpy program to test a given array
element wise for finiteness(not inifinity or not a number)
'''

import numpy as np 
a=np.array([1,0,np.nan,np.inf])
print("original array")
print(a)
print("Test a given array element wise for finiteness")
print(np.isfinite(a))

##############################################

'''
write numpy program to test element wise for
nan of a given array
'''
import numpy as np 
a=np.array([1,0,np.nan,np.inf])
print("original array")
print(a)
print("Test a given array element wise for finiteness")
print(np.isnan(a))
###############################################

'''
write numpy program to create on elementwise
comparision (greater, greater equal, less and
             less equal) of two given array
'''

import numpy as np
x=np.array([3,5])
y=np.array([2,5])
print("original number")
print(x)
print(y)

print("comparision - greater")
print(np.greater(x,y))
print("camparision - greater_equal")
print(np.greater_equal(x,y))
print("comparision - less")
print(np.less(x,y))
print("comparision - less_equal")
print(np.less_equal(x,y))
########################################
'''
write a numpy program to create a 3 by 3 identity
matrix
'''
import numpy as np
arr_2D=np.identity(3)
print("3x3 matrix:")
print(arr_2D)
##############################################

'''
write a numpy program to generate a random number
between 0 and 1
'''
import numpy as np
rand_num = np.random.normal(0,1,1)
print("Random number beween  0 and 1")
print(rand_num)
############################################

'''
write numpy program to create array and iterate
over it

'''
import numpy as np
a=np.arange(10,22).reshape((3,4))
print("original array")
print(a)
print("each element of the array is:")
for x in np.nditer(a):
    print(x,end=" ")
    print()
    
############################################

##write  numpy program to create a vector of
#lenght 10 with values evenly dustributed
#between 5 and 50

import numpy as np
v=np.linspace(10,49,5)
#10 start point, 49 end point, 5 numbers in vector
print("lenght 10 with values evently distributed")
print(v)
###################################
'''
write numpy program to create matrix 3x3 
with values ranging 2 to 10
'''

import numpy as np
x = np.arange(2,11).reshape(3,3)
print(x)

#######################################
'''
write a numpy program to reverse an array
(the first element becomes a last)
'''
import numpy as np
x=np.arange(12,38)
print("original array:")
print(x)
print("reverse array:")
x=x[::-1]
print(x)
#################################################
'''
write numpy program to compute the multiplication
of to given matrix 
'''

import numpy as np
p=[[1,0],[0,1]]
q=[[1,2],[3,4]]
print("original matrix")
print(p)
print(q)
result1=np.dot(p,q)
print("result of the said matrix multiplication:")
print(result1)
###########################################
'''
write a numpy program to compute the cross 
product of two mitrices
'''
import numpy as np
p=[[1,0],[0,1]]
q=[[1,2],[3,4]]
print("original matrix")
print(p)
print(q)
result1=np.cross(p,q)
result2=np.cross(q,p)
print("result of the said matrix cross product:")
print(result1)
print(result2)
###########################################
'''
write numpy program to compute determinent of
given square array
'''

import numpy as np
from numpy import linalg as LA
a=np.array([[1,0],[1,2]])
print("Original 2-D array")
print(a)
print("Determinent of the said 2-D array:")
print(np.linalg.det(a))
########################################
'''
write a numpy program to compute the eigenvalues
and right eigenvectors of a given square array
'''

import numpy as np
m=np.mat('3 -2;1 0')
print("original matrix:")
print("a\n",m)
w,v=np.linalg.eig(m)
print("eigenvalues of the said matrix",w)
print("eigenvalues of the said matrix",v)
#########################################
'''
write a numpy program to compute the inverse
of the given matrix 
'''
import numpy as np
m=np.array([[1,2],[3,4]])
print("original matrix:")
print(m)
result = np.linalg.inv(m)
print("Inverse of the said matrix:")
print(result)
#############################################

'''
write  
'''