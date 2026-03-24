stud1=['rihan','370cs24025']

tmarks=[67,76,87]
lmarks=[32,43,43]

tmarks=[x for x in tmarks if  x <=100 and x >=0]
print(tmarks)
lmarks=[x for x in lmarks if  x <=50 and x >=0]
print(lmarks)

if(len(tmarks)!=3 or len(lmarks)!=3):
    print("marks containt invalid value")
else:
    marks=tmarks.copy()
    marks.extend(lmarks)
    print("student marks: \n",marks)
    stud1.append(marks)
    print("student info: \n",stud1)
    sum1=sum(marks)
    print("total marks:",sum1)

    regno=list(stud1[1])

    colcode=regno[:3]

    if colcode==['3','7','0']:
        print("student is registered from svp")
    else:
        print("studentt is not registerd from svp")




