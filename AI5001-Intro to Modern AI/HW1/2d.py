
import numpy as np
r1 = 3 
r2 = -1 
c = 0.5 
#c = gamma = 0.5 
#r_move= r1 and r_stay = r2
# A(good) = {move,stay}
# A(bad) = {move,stay}
#v(good) = Vg , v(bad) = Vb
# vs : if action is move , va : if action is stay
Vb = 0 
Vg = 0
d1 = 0
d2 = 0
t = 0.00000001

p = 0
while(p == 0) : 
#for i in range(10):    
    #if s = bad
    v1 = Vb
    #if action is move 
    Sm1 = (1) * (r1 + c *  Vg)
    #if action is stay 
    Ss1 =  1 * (r2 + c * Vb) 
    #if s = good
    v2 = Vg
    #if action is move 
    Sm2 =  (r2 + c * Vb) * (1)
    #if action is stay 
    Ss2 = (r1 + c * Vg) * 0.5  +  (r2 + c *Vb) * (0.5)
    Vb = max(Sm1,Ss1)
    Vg = max(Sm2,Ss2)
    e1 = abs(v1 - Vb)
    e2 = abs(v2 - Vg)

    if(e1 < t and e2<t):
        p = 1
    
    d1 = max(d1,e1) 
    d2 = max(d2,e2)
    
print "V(bad) =  ", Vb    
print "V(good) =  ",Vg  


Pi_b = np.argmax([Sm1 , Ss1 ])
#policy = A(Pi_l)
print("policy for bad state is stay")
Pi_h = np.argmax([Sm2 , Ss2 ])
print("policy for good state is move")
