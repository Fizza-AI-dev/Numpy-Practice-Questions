import numpy as np


# arr=np.array([2,4,6,8,6,45,78])
# new_arr=np.append(arr, [20,30])
# print(new_arr)

arr_2d=np.array([[2,4],[6,8]])
new_row=[[5,6]]
new_arr=np.append(arr_2d,new_row, axis=0)
print(new_arr)
