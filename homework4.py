from pylab import *

v=[]
t=[]
g=9.8
dt=0.1
v.append(0.)
t.append(0)
end_time=10

for i in range(int(end_time/dt)):
        u=v[i]+g*dt
        v.append(u)
        t.append(dt*(i+1))
        print t[-1],v[-1]


plot(t, v)
show()
