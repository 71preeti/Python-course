# manager records
'''manager_name="ram singh"
manager_id="ramsingh123@gmail.com"
manager_pass="hello@123"
manager_salary=50000'''


# employee records
employee_list=['rohit','abhi','manshi','harsh']
assistant='manshi'
assistant_id='manshi245@gmail.com'
assistant_pass='hello234'



def employee_data():
    print('your employee list:',employee_list)
    print('your assistant name is :',assistant)
    print('assistant_id:',assistant_id)
    print('assistant_pass:' ,assistant_pass)

print('manager file excutetd the content that present outside from the condition')
if __name__ == "__main__":
    print(' manager file excutetd the content that present inside from the condition')
    manager_name="ram singh"
    manager_id="ramsingh123@gmail.com"
    manager_pass="hello@123"
    manager_salary=50000



    def manager_data():
        print(manager_name)
        print(manager_id)
        print(manager_pass)
        print(manager_salary)


employee_salary=[25,35,45,67,78,89]
def min_salary_finder(salary_ls):
    number=0
    for number in employee_salary:
        if number>0:
            return number
print(min_salary_finder(employee_salary))

'''employee_salary=[25,35,45,67,78,89]
def max_salary_finder(salary_ls):
    number=max
    return number
print(max_salary_finder(employee_salary))'''
