# search,sort,filter

import numpy as np 

# ar = np.array([[4,2,5,62,3,6],[5,3,6,2,6,10]])
# print(np.sort(ar))

# ar = np.array([3,4,1,7,8])
# s = np.where(ar % 2 == 0)
# print(s)

# ar = np.array([1,2,3,4,5])
# ss = np.searchsorted(ar,4)
# print(ss)


# ar = np.array([20,30,40,50])

# fa = [False, False, False, True]

# new = ar[fa]
# print(new)


ar = np.array([2,3,4,5])

fa = ar%2==1

new = ar[fa]
print(new)