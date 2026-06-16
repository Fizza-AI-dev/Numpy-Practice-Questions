import numpy as np

# if there is a infinite value in array like 1/0, it returns a boolean
arr=np.array([1,2,np.inf,6])
print(np.isinf(arr))

cleaned_arr=np.nan_to_num(arr,posinf=4)
print(cleaned_arr)