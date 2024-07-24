# loops for loop description used for when loop ki value pta ho hume ki kitni baar loop chlana h.
for var in range(100):
    print("Welcome to upflairs! ",var)

company="upflairs"
student_name=['ram','shyam','rohit','raman']
student_marks=(10,20,30,40,50,60,70)

for char in company:
    print(char)
for char in student_marks:
    print(char)
for char in student_name:
    print(char)

dt={1:'a',2:'b',3:'c',4:'d'} #key value dono for loop se print krwana h 


num=[10,20,30,45,56,67,85,67,48,59]
for item in num:
    print(item)

num=[10,20,30,45,56,67,85,67,48,59]
count=0    # to find 85 in it and which position              
for item in num:
    if item ==85:
        print(count)
    count=count+1

num=[14,52,63,96,85,74,8,15,25,36,147,966,42,15,36,4]
count=0    # to find less than 50 no. in it  and which position              
for item in num:
    if item >=50:
        print(count)
    count=count+1

# while loop syntanx
i=0                       #initialization
while i<=100:              #condition
    print("hello world", i)       # block of code
    i=i+1                     #increment

# break keyword  stop the loop 
for i in range(11):
    print(i)
    if i==5:      # i ==5 tk chlega bss 
        break

for i in range(11):
    if i==5: 
        continue     # i ==5 nhi chlega bss or chlega 
    print(i)

count=0
for i in range(10):
    break            # output 0 he aayega bs
    count+=1
print(count)

count=0
for i in range(10):
    continue        # output 0  aayega bs
    count+=1
    
print(count)

count=0
for i in range(10):
    count+=1
    continue 
print(count)                  # output 10  aayega bs
   

count=0
for i in range(10):
    count+=1
    break             
print(count)                   # output 1 aayega bs
   

#  function : block of code tast perform certain task aagain and again

# user defined function syntax
#  len ki place pe my_len function bnana h (replica of len())

age=[10,20,30,40,50,60,70,80,90]
age2=[10,20,30,40]
def my_len(ls):
    count=0
    for i in ls:           # define the function
        count +=1
    return count          #return behave as break in function and return the value of code

print(my_len(ls=age))    # calling the function
print(my_len(age))
print(my_len(age2))

'''ASSIGNEMENT QUESTIONS:

A.  my_min() and my_max () function create krna of list'''







''''B. 
 lambda function pdna h kya hota h ? = lambda function nameless hota h and single line of code hota h 
syntax: var=lambda argument:expression       example given below:
 '''

sum=lambda x,y:x+y
print(sum(10,30))

double=lambda x:x*2
print(double(9))


'''  C.

    1 
    12
    123
    1234
    12345

create this using loop'''

n=int(input("enter the no.of rows:")) 
for i in range(n):                               
    for j in range(i+1):
        print(j+1,end=' ')
    print()


'''D.
    
    *
    **
    ***
    ****
    *****
    ******

create this using nested loop
'''

for i in range(6):
    for j in range(i+1):
        print('*',end=' ')
    print()    




list=[10,20,30,40]
def my_max(ls):
    highest_num =0
    for number in list:           # define the function
        if number > highest_num:
            highest_num=number
            return max
                                          #return behave as break in function and return the value of code
print(my_max(ls=list))






