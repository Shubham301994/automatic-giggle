import numpy as np
import time

def test_run():
#    print (np.array([(2,3,4),(5,6,7)]))#2 rows and 3 columns
#    print(np.empty(5))#empty 5 numbers, spits out whatever was in memory
#    print(np.empty((4,3)))#4x3, spits out w/e was in memory

#print(np.ones((5,4),dtype=np.int_))#5x4 array of ones, dataType int
#print(np.random.normal(size=(2,3))) #2x3 "standard normal" (mean=0, sd=1)

#a = np.random.normal(50,10,size=(2,3)) #2x3(mean=50, sd=10)Values Centered around 50
#print(a.dtype)#Returns float64 as data type of a
#print(a.sum())
    a = np.random.rand(5,4)

    print('Array: ',a)
    element = a[3,2]
    print(element)

if __name__=="__main__":
    test_run()
