import numpy as np
#A(low) = {search,wait , recharge}
# A(high) = {search ,wait}
#v(low) = vl , v(high) = vh

r1 = 2 
r2 = 1 
r3 = -3
#r_search = r1 and r_wait = r2, r_recharge = 0 

a = 0.3  
b = 0.2
c = 0.5 
# a = alpha , b = beta , c = gamma 
# vs : if action is search , va : if action is wait
Vl = 0 
Vh = 0
d1 = 10000
d2 = 10000
t = 0.0000001


p = 0
while(p == 0) : 
    #if s = low 
    v1 = Vl
    #if action is search 
    Ss1 =  b * (r1 + c * Vl) +  (1 - b) * (r3+ c *  Vh)
    #if action is wait 
    Sw1 =  1 * (r2 + c * Vl) + (r2 + c * Vh) *  0
    #if s = high
    v2 = Vh
    #if action is search 
    Ss2 = (r1 + c*Vh)  * a + (r1 + c * Vl) * (1 - a)
    #if action is wait 
    Sw2 = (r2 + c * Vh) * 1 + (r2+ c *Vl) * (0)
    Vl = max(Ss1,Sw1)
    Vh = max(Ss2,Sw2)

    e1 = abs(v1 - Vl)
    e2 = abs(v2 - Vh)
    if(e1 < t and e2<t):
        p = 1
    
    d1 = max(d1,e1) 
    d2 = max(d2,e2)
    
    
print "V(low) =  ", Vl    
print "V(high) =  ",Vh  

Pi_l = np.argmax([Ss1 , Sw1 ])
#policy = A(Pi_l)
print("policy for low state is wait")
Pi_h = np.argmax([Ss2 , Sw2 ])
print("policy for high state is search")
