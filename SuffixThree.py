t=int(input())
for T in range(t):
    s=input()
    S=""
    if s[-1]=='o' and s[-2]=='p':
        S="FILIPINO"
    elif s[-1]=='u' and s[-2]=='s' and s[-3]=='e' and s[-4]=='d':
        S="JAPANESE"
    elif s[-1]=='u' and s[-2]=='s' and s[-3]=='a' and s[-4]=='m':
        S="JAPANESE"
    elif s[-1]=='a' and s[-2]=='d' and s[-3]=='i' and s[-4]=='n' and s[-5]=='m':
        S="KOREAN"
    else:
        x=0
    print(S)