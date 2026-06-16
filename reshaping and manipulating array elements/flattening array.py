import numpy as np
# .ravel() => returns view
# .flatten() => return copy

arr=np.array([[2,4],[6,8]])
print(arr.flatten())
print(arr.ravel())