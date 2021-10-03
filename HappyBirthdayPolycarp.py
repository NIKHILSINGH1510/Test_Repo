t=int(input())
for T in range(t):
    n=int(input())
    c=0
    flag=0
    i=11
    if(n<=10):
        c=n
    elif n>10 and n<=11111:
        c=9
        while(i<=n):
            flag=0
            N=str(i)
            #print("N : ",N)
            l=len(N)
            #print("L : ",l)
            for j in range(l):
                #print("J : ",j)
                try:
                    if(N[j+1]!=N[j]):
                        flag=1
                        #print(f"Flag=1,\t {N[j+1]} != {N[j]}")
                        break
                except IndexError:
                    q=0
            if flag==0:
               # print(f"FLAG = 0 \t {i}")
                c+=1
            i+=1
    elif(n>11111 and n<=99999): #10^5
        c=37
        i=11111
        while(i<=n):
            i+=11111
            c+=1
    elif(n>99999 and n<=999999): #10^6
        c=37
        i=111111
        while(i<=n):
            i+=111111
            c+=1
    elif(n>999999 and n<=9999999): #10^7
        c=46
        i=1111111
        while(i<=n):
            i+=1111111
            c+=1
    elif(n>9999999 and n<=99999999):   #10^8
        c=55
        i=11111111
        while(i<=n):
            i+=11111111
            c+=1
    elif(n>99999999 and n<=1000000000): #10^9
        c=64
        i=111111111
        while(i<=n):
            i+=111111111
            c+=1
    print(c)
    