import numpy as np


# arr=np.array([2,4,6,8,6,45,78])
# new_arr=np.insert(arr,2,100)
# print(new_arr)


# insertion in 2D array

arr_2d=np.array([[2,4],[6,8]])
new_arr=np.insert(arr_2d,1 , [5,6], axis=0)
print(new_arr)