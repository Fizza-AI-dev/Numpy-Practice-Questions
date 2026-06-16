
import numpy as np
arr2=np.array([[2,4],[6,8]])
arr1=np.array([[3],[5]])
new_arr=np.concatenate((arr2,arr1),axis=1)
print(new_arr)

# arr1=np.array([2,3])
# arr2=np.array([2,6])
# new_arr=np.concatenate((arr1,arr2))
# print(new_arr)