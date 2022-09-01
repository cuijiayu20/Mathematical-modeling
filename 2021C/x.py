from ast import Pass
from site import USER_BASE
import xlrd

def weekxStroe(a,nrows,ncols,x):
    a1=[]
    b=[]
    c=[]
    for i in range(1,nrows):
        if a[i][x]=="A":
            a1.append(a[i])
            # b.sort()
        elif a[i][x]=="B":
            b.append(a[i])
        else:
            c.append(a[i])
    for i in range(len(a1)):
         for j in range(len(a1)-1):
            if a1[j][x+1]<a1[j+1][x+1]:
                a1[j],a1[j+1]=a1[j+1],a1[j]
    for i in range(len(b)):
         for j in range(len(b)-1):
            if b[j][x+1]<b[j+1][x+1]:
                b[j],b[j+1]=b[j+1],b[j]
    for i in range(len(c)):
         for j in range(len(c)-1):
            if c[j][x+1]<c[j+1][x+1]:
                c[j],c[j+1]=c[j+1],c[j]
        
    
    return a1,b,c

def useWho(a1,x):
    sum=0
    use=set()
    for i in range(len(a1)):
        if sum<=28200:
            if a1[i][x+1]>=6000:
                sum=sum+6000
                use.add(a1[i][0])
            else: 
                sum=sum+a1[i][x+1]
                use.add(a1[i][0])
                
        if sum>28200:
            use.add(a1[i][0])
            break

        
    return use






file1="D:\\数学建模\\2021C\\a.xls"
data=xlrd.open_workbook(file1)
sheet=data.sheet_by_index(1)
a=[]
minx=[]
usea=set()
userb=set()
userc=set()
nrows=sheet.nrows
ncols=sheet.ncols

for row in range(sheet.nrows):
    b=[]
    for col in range(sheet.ncols):
        b.append(sheet.cell_value(row,col))
    a.append(b)
# for i in range(1,241):
#     a1,b,c=weekxStroe(a,nrows,ncols,i)
#     print(a1)
#     usea=useWho(a1,i),
#     useb=useWho(b,i)
#     usec=useWho(c,i)
#     x=min(len(usea),min(len(useb),len(usec)))
#     if len(useb)==x:
#         minx.append("usea")
#     elif len(usea)==x:
#         minx.append("useb")
#     else:
#         minx.append("usec")

a1,b,c=weekxStroe(a,nrows,ncols,2)
print(a1)
# # print(minx)
# print(usea)