n,v1,v2=map(int,input().split());
t1=((2**0.5)*n)/v1
t2=(2*n)/v2
print('Cab' if t1>t2 else 'Walk',end='');