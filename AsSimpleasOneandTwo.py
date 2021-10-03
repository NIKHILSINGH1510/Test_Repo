t=int(input())
for T in range(t):
    s=input()
    n=len(s)
    c=0
    a=[]
    for i in range(n):
        try:
            if (s[i]=='o' and s[i+1]=='n' and s[i+2]=='e') or (s[i]=='t' and s[i+1]=='w' and s[i+2]=='o'):
                c+=1
                try:
                    s=s[:i+2]+s[i+3:]
                except IndexError:
                    s=s[:i+2]
                a.append(i+3)
        except IndexError:
            q=0
    print(c)
    for i in a:
        print(i,end=' ')