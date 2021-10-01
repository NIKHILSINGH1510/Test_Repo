t=int(input())
for T in range(t):
    x=int(input())
    s=input()
    l=1
    c=""
    S=s
    while(l<=x):
       # print()
        s=s[0:l]
        #print("L : ",l)
       # print("S[0:l] : ",s)
        c=S[l:]
       # print("C = s[l:] = ",c)
        n=int(s[-1])
       # print("N = s[-1] = ",n)
        s=s+(c*n)
        l+=1
       # print("S : ",s)
        S=s
    l=len(s)
    print(l)