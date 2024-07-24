#vriable
# variable declares
# variable naming rule
# datatype int float
msg="upflairs hello"
print(msg[8])
print(msg[1:])
print(msg[:9])
print(msg[3:9])
print(msg[::2])
print(msg.upper())
print(msg.title())
print(len(msg))
print(msg.count('j'))
print(msg.find('p'))
print(msg.find('hello'))
print(msg.split())
st='upflairs,pvt,limited,jaipur rajasthan'
print(st.replace('p','mn'))
var1=True
var2=False
print(var1,var2)
print(type(var1),type(var2))
#list in python
ls=[10,20,30,40,50,25,41,2.3,'upflairs',True]
print(ls)
print(type(ls))
ls=[10,20,30,40,50,60,70]
print(ls[0])
print(ls[::3])
print(ls[::1])
#list built in function
student_name=['ram','shyam','mohit','reena']
print(student_name)
#insertion in list
student_name.append('manshi')
print(student_name)
#pop function in list
student_name.pop()
print(student_name)
print(student_name.pop(0))
# update item in list
print(student_name)
student_name[2]='reena kuntal'
print(student_name)
# insertion at anywhere in list
student_name.insert(2,'manshi')
print(student_name)
#count fuction in list
ls=[10,20,30,40,50,50,60,60,70,70,70]
print(ls.count(70))
print(len(ls))
ls.sort()
print(ls)
#list in list
ls=[10,20,30,[30,40,50]]
print(ls[3])
# replace value in list
ls=['ram','shaym']
print(ls)
ls[0]='seeta'
print(ls)
#datatype tuple in python
tp=(10,20,30,40,'ram',3.5)
print(tp)

tp[3]=45
print(tp)




