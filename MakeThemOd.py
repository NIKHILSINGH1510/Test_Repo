t=int(input())
for T in range(t):
    n=int(input())
    c=0
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    flag=-1
    N=0
    while(N!=n):
        N=0
        for i in range(n):
            if(a[i]%2==0):
                c+=1
                num=a[i]
                for j in range(n):
                    if(a[j]==num):
                        a[j]=a[j]/2
        for i in range(n):
            if a[i]%2==0 and a[i]>1:
                break
            else:
                N+=1
    print(c)