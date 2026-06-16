import numpy as np

arr=np.array([1,2,np.nan,6])
print(np.isnan(arr))

print(np.nan==np.nan) #we cannot directly compare these values