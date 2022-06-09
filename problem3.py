from scipy import linalg
import numpy as np

#create the matrix and store it as a
a=np.array([[1,0,4],[-2,3,-2],[-2,0,6]])

#use qr function for Qr factorization
q,r = linalg.qr(a)
q=q*-1
r=r*-1
q[0,2]=q[0,2]*-1
q[1,2]=q[1,2]*-1
q[2,2]=q[2,2]*-1
r[2,0]=r[2,0]*-1
r[2,1]=r[2,1]*-1
r[2,2]=r[2,2]*-1

#print Q & R
np.allclose(a,np.dot(q,r))
print("Q:")
print(q)
print("R:")
print(r)



