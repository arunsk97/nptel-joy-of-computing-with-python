x=int(input());
l=[int(i) for i in input().split()];
sort=sorted(l);
k=int(input());
pos=l[k-1];
if pos in sort:
  ind=sort.index(pos)+1
  print(ind,end='')