#dictionary datatype store in key value pair
dt={'A':10,'B':20,'C':30,'D':40}
print(dt)
#key value m koi restriction nahi h bo kisi bhi datatype ki ho skti h
print(dt['B'])   #access the value
dt['d']=500 #update value of key
print(dt)
dt['E']=5000 #adding new key value pair
print(dt)
dt.pop('C')  #remove pair from dt
print(dt)
print(dt.keys())  # only show keys
print(dt.values())  # to show only values in dt
student_marks={'name':['manshi','ram','kishan','harsh'],'marks':[25,41,52,63],'subject':'science'}
print(student_marks)
print(student_marks['name'])
print(student_marks['subject'])
student_marks['name'].pop () 
student_marks['marks'].pop ()
print(student_marks)

 #how to remove harsh and 63 marks from this 
  #how 
# to add abhishek and 55 marks in 1st position of this dict.
student_marks['name'].insert(1,'abhishek')
student_marks['marks'].insert(1,55)
print(student_marks)

# program how many students are in this record
print(len(student_marks['name']))


#CONDITIONAL IF ELSE STATEMENT = it is used to define condition in task
# if ,else,elif,nested if else
age=23
if age>21:
    print('You can vote!')
else:         
    print('You can not vote!')

# to understand the overall concept of conditional statement we make a new file atm simulation 