# write a program to do the following
# enter a vector b and find the projection of b orthogonal to given vector u 
import numpy as np
def opprojection(of_vec,on_vec):
    v1 = np.array(of_vec)
    v2=np.array(on_vec)
    scal  = np.dot(v1,v2)/np.dot(v2,v2)
    vec=scal*v2
    return round(scal ,10),np.around(vec,decimals=10)

print(opprojection([4.0,4.0],[1.0,0.0]))

print(opprojection([4.0,4.0],[8.0,2.0]))