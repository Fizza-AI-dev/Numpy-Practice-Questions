import numpy as np
# arr_2d=np.array([[2,4],[6,8]])
# new_arr=np.insert(arr_2d,1 , [5,6], axis=0)
# print(new_arr)

arr=np.array([[4,6],[8,7]])
new_arr=np.delete(arr,1,axis=0)
print(new_arr)