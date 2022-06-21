t=  int(input())
for k in range(t):
    f=0
    s = input()
    print(s)
    if(len(s)>3):
        if(s[0]=='<' and s[1]=='/' and s[-1]=='>'):
            for i in range(2,len(s)-1):
                if(48<=ord(s[i])<=57 or 97<=ord(s[i])<=122):
                    continue
                else:
                    print('Error')
                    f=1
                    break
        else:
            print('Error')
            print(s[0],s[1],s[2],s[-1])
            f=1
    else:
        print('Error')
        f=1
    if(f==0):
        print('Success')