def rollTheString(s, roll):
    if len(roll)!=0 :
        for i in range(len(roll)):
            str=[]
            x=roll[i]
            for i in range(x):
                if s[i]=="z" or s[i]=="Z":
                    s1 = chr(ord(s[i])-25)
                else:    
                    s1 = chr(ord(s[i])+1)
                str.append(s1)
                l = s[x:]
            for num in l:
                str.append(num)   
            s=str
        return ''.join(str)        
s = "abz"      
roll=[3,1]
b = rollTheString(s,roll)
print(b)