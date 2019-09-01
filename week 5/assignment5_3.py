def isprime(n):
    if(n<=1):
        return False
    for i in range(2,int(n**0.5)+1):
        if(not n%i):
            return False;
    return True;


def issemiprime(n):
    #return sum(prime_factors(n).values)==2;
    i,c=2,0;
    while(i<=int(n**0.5)):
        same=0;
        while(not n%i):
            same+=1;
            n=int(n/i);
        i+=1;
        c+=same;
        if(c>2 or same>=2):
            return False;
    if(n>=2):
        c+=1;
    if(c==2):
        return True;
    else:
        return False;

def issumsemiprime(n):
    if(n<=3):
        return False;
    for i in range(2,n):
        if(issemiprime(i) and issemiprime(n-i)):
            return True;
    return False;

n=int(input());
print('Yes' if issumsemiprime(n) else 'No');