import pandas as pd
l=[]
def college(s,a,p,per,km,st,bf):
    campus={
        'college':s,
        'Branch':a,
        'Placements':p,
        'Percentage':per,
        'Distance':km,
        'Status':st,
        'Transport':bf
    }
    l.append(campus)
   
n=int(input("No.of colleges: "))
for i in range(1,n+1):
    s=input("Name of the college: ")
    a=list(input("List of branches: ").split())
    p=int(input("No.of placements: "))
    per=float(input("Pass percentage: "))
    km=int(input("Distance: "))
    st=input("Status: ")
    bf=input("Transport: ")
    college(s,a,p,per,km,st,bf)
print('college\tBranch\tPlacements\tPercentage\tDistance\tStatus\tTransport\t')
for i in range(n):
    print(l[i])
df=pd.DataFrame(l)
print(df)
k=input()
for i in range(n):
    if l[i]['college']==k:
        print("Details of college: ")
        print(l[i]['college'],l[i]['Branch'],l[i]['Placements'],l[i]['Percentage'],l[i]['Distance'],l[i]['Status'],l[i]['Transport'])
for i in range(n):
    if l[i]['Placements']>500:
        print('Placements greater than 500: ',l[i]['college'])
g=input()
for i in range(n):
    if l[i]['college']==g:
        print('Branches: ',l[i]['Branch'])
for i in range(n):
    if l[i]['Transport']=='yes':
        print('Transport available college: ',l[i]['college'])
for  i in range(n):
    if l[i]['Percentage']>60:
        print('percentage of college: ',l[i]['college'])
v=0
for i in range(n):
    if l[i]['Status']=='autonomous':
        v=v+1
        print('Autonomous college: ',l[i]['college'])
print('count:', v)
c=[]
for i in range(n):
    c.append(l[i]['Placements'])
mx=max(c)
for i in range(n):
    if l[i]['Placements']==mx:
        print('Max Placements of college: ',mx,l[i]['college'])
d=[]
for i in range(n):
    d.append(l[i]['Distance'])
mn=min(d)
for i in range(n):
    if l[i]['Distance']==mn:
        print('Min Placements of college: ',mn,l[i]['college'])
