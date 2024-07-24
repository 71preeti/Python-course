'''import manager 
print(manager.assistant)
print(manager.assistant_id)
print(manager.assistant_pass)'''

'''import manager as mng
print(mng.assistant)
print(mng.assistant_id)
print(mng.assistant_pass)'''

'''from manager import assistant,assistant_id,assistant_pass

print(assistant_pass)
print(assistant)                                        # this is the best approach 
print(assistant_id)


assistant="saurabh"
print(assistant) '''                       # this is the override concept

'''from manager import manager_id,manager_name,manager_pass
print('employe file executed')
print(manager_pass)
print(manager_id)
print(manager_name)'''
'''print(manager_salary)             get error b/c it is not import from manager.py'''

from manager import assistant,assistant_id,assistant_pass
print('employe file executed')


from manager import employee_data
print(employee_data())

from manager import employee_salary
print(employee_salary)

