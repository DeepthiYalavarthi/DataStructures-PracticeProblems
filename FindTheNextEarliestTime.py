import datetime
def permutation(list):
    if len(list) == 0:
        return []
    if len(list) == 1:
        return [list]
    emplist = [] # empty list that will store current permutation 
    for i in range(len(list)):
       m = list[i] 
       rLst = list[:i] + list[i+1:] 
       for p in permutation(rLst):
           emplist.append([m] + p)
    return emplist
time = datetime.datetime.now()
hour = str(time.hour)
minutes = str(time.minute)
if len(minutes)==1:
    minutes = str(0)+minutes
current_time = hour+":"+minutes 
print ("Current time is: "  + current_time)      
list = []
for i in current_time:
    if i.isdigit() or i==0:
        list.append(i)
lt= []
for p in permutation(list):
    lt.append(p)   
def validity(q):
    if int(str(q[0])+str(q[1]))>23 or int(str(q[2])+str(q[3]))>59:
        return q
def noOfMinutes(q):
    y=[]
    for items in q:
        z = int(str(items[0])+str(items[1]))*60+int(str(items[2])+str(items[3]))
        y.append(z)
    return y    
def greatestAndSmallest(q,l):
    if len(q)==1:
        great=q[0]
        small =q[0]
        return great,small
    if l not in q:
        print("Invalid Time")
        great=None
        small=None
    else:
        diff = 24*60
        x = (int(str(l[0])+str(l[1]))*60)+int(str(l[2])+str(l[3]))
        y = noOfMinutes(q)
        z=[]
        for i in y:
            if i-x>=0:
                r1 = i-x
                z.append(r1)
            elif i-x<0:
                r2 = diff-x+i
                z.append(r2)    
        maximum=0
        for i,value in enumerate(z):
            if value>maximum:
                maximum=value
                index=i
        for n, i in enumerate(z):
            if i == 0:
                z[n] = 10000
        minimum=z[0]
        for i in range(len(z)-1):
            if minimum>z[i+1]:
                minimum=z[i+1]
                ind=i+1
        great = q[index]
        small = q[ind]
    return great,small
s = validity(list)
if(s==None):
    li=[]
    invalid=[]
    for item in lt:
        li=validity(item)
        if(li!=None):
            invalid.append(li)
    validlist=[item for item in lt if item not in invalid]
else:
    print("Invalid Time")
(greatest,smallest) = greatestAndSmallest(validlist,list)
if greatest==None and smallest==None:
    print("Time is Invalid")
else:
    print("Time is Valid")
    print("The next greatest possible time is-",str(greatest[0])+str(greatest[1]),":",str(greatest[2])+str(greatest[3]))
    print("The next earliest possible time is-",str(smallest[0])+str(smallest[1]),":",str(smallest[2])+str(smallest[3]))