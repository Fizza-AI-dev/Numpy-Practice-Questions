import numpy as np


arr=np.array([2,4,6,8,6,45,7,8,9])
arr_reshape=arr.reshape(3,3)
print(arr_reshape)
# reshaping does not create a copy it show view only