import numpy as np

# replace nan with number
arr=np.array([1,2,np.nan,6])
print(np.nan_to_num(arr,nan=6)) # default value is zero