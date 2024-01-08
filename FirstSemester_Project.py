#!/usr/bin/env python
# coding: utf-8

# # Project Overview:
# 
# # A local retail business, dealing with a variety of products, aims to streamline and automate its accounting procedures. 
# # The business operates two shifts per day with one worker on each shift. 
# # The primary goal is to create a Python project that assists in automating essential accounting tasks, including calculating total sales, worker salaries, profit, tips, and total tips for the day.

# In[1]:


# a lists of morning and evening sales
morning_sales = [100, 300, 650, 700, 950]
evening_sales = [200, 500, 650, 800, 850]

# function that calculate overall sales of morning and evening
def calculate_total_sales(morning_sales, evening_sales):
    
    # overall sales will be determine according to the total sum of morning plus total sum of afternoon
    total_sales = sum(morning_sales) + sum(evening_sales)
    return total_sales


# In[2]:


total_sales = calculate_total_sales(morning_sales, evening_sales)


# In[3]:


total_sales


# In[4]:


# function that calculate workers salary
def calculate_workers_salary(hourly_rate, hours_worked):
    
    # worker salary will be determine according to amount of hourly rate multiply by hours worked
    worker_salary = hourly_rate * hours_worked
    return worker_salary


# In[5]:


worker_salary = calculate_workers_salary(500, 600)


# In[6]:


worker_salary


# In[7]:


# a list of total sales and total cost
total_sales = [4000, 5700, 10000, 6500, 7000]
total_cost = [3500, 6700, 5000, 8500, 7200]

# function to calculate profit or loss(if negative)
def calculate_profit(total_sales, total_cost):
    total_sales = sum(total_sales)
    total_cost = sum(total_cost)
    
    if total_sales > total_cost:
        profit = total_sales - total_cost
        print('Profit:')
        print(f"\nYou Made Profit of: {profit}")
    elif total_cost > total_sales:
        print('Loss')
        print(f"\nYou Loss total Amount of: {profit}")
    else:
        print('No Profit No Loss')
    return profit


# In[8]:


calculate_profit(total_sales, total_cost)


# In[9]:


# a lists of shift sales
shift_sales = [2000, 1800, 1500, 700, 3000]

# function that calculate tips percentage according to the sales per shift
def calculate_shift_tips(shift_sales):
    shift_sales = sum(shift_sales)
    
    # tip precentage is 2%
    tip_percentage = 0.02
    tips = shift_sales * tip_percentage
    return tips


# In[10]:


calculate_shift_tips(shift_sales)


# In[11]:


# a lists of morning and evening shift sales
morning_shift_sales = [2000, 1800, 1500, 700, 3000]
evening_shift_sales = [5000, 1900, 3500, 900, 600]

# function that calculate overall tips percentage according to the sales of both morning and evening shift
def calculate_total_tips(morning_shift_sales, evening_shift_sales):
    morning_shift_sales = sum(morning_shift_sales)
    evening_shift_sales = sum(evening_shift_sales)
    
    tip_percentage = 0.02  # 2% tip rate
    total_tips = (morning_shift_sales + evening_shift_sales) * tip_percentage
    return total_tips


# In[12]:


calculate_total_tips(morning_shift_sales, evening_shift_sales)


# # Welcome to the Sales Operation Menu!
# 
# # Please choose from the following options:
# # 1. Calculate Total Sales for the Day
# # 2. Calculate Worker's Salary
# # 3. Calculate Profit
# # 4. Calculate Tips for a Shift
# # 5. Calculate Total Tips for the Day
# # 6. Exit
# 
# # Enter your choice (1-6): 
# 
# # If you choose 1, please enter the total sales for the morning shift and evening shift separated by a comma (e.g., 1000,2000): 
# 
# # If you choose 2, please enter the hourly rate and hours worked by the worker separated by a comma (e.g., 10,8): 
# 
# # If you choose 3, please enter the total sales and total cost of items sold separated by a comma (e.g., 5000,3000): 
# 
# # If you choose 4, please enter the shift sales as a list separated by commas (e.g., 1000,2000,3000): 
# 
# # If you choose 5, please enter the shift sales for the morning and evening shifts separated by a comma (e.g., 1000,2000): 
# 
# # If you choose 6, the program will exit.
# 
# # What would you like to do?

# In[2]:


def run_sales_operation():
    while True:
        print('\nWelcome to Sales Operation Interface')
        print("Please choose from the following options:")
        print('1, calculate_total_sales')
        print('2, calculate_workers_salary')
        print('3, calculate_profit')
        print('4, calculate_shift_tips')
        print('5, calculate_total_tips')
        print('6, Exit')
    
        choice = input('Enter your choice (1-6): ')
        if choice == '1':
            morning_sales, evening_sales = input("kindly enter total morning shift sales and evening shift sales seperated by commas: ").split(',')
            total_sales = int(morning_sales) + int(evening_sales)
            print(f"Total sales for the day: {total_sales}")
        elif choice == '2':
            hourly_rate, hour_worked = input("kindly enter hourly rate and hours worked by the worker seperated by a commas: ").split(',')
            workers_salary = float(hourly_rate) * float(hour_worked)
            print(f"Worker Salary is: {workers_salary}")
        elif choice == '3':
            total_sales, total_cost = input("kindly enter the total sales and the total cost of the items sold seperated by a commas: ").split(',')
            profit = int(total_sales) - int(total_cost)
            if total_sales > total_cost:
                print(f"You Make Profit of: {profit}")
            else:
                total_sales <= total_cost
                print(f"You Loss or You did not make a Profit: {profit}")
        elif choice == '4':
            shift_sales = list(map(int, input("kindly enter your shift sales as a list seperated by commas: ").split(',')))
            tip_percentage = 0.02
            tips = sum(shift_sales) * float(tip_percentage)
            print(f"Tips for the Shift: {tips}")
        elif choice == '5':
            morning_shift_sales, evening_shift_sales = map(int, input("kindly enter the shift sales for the morning and evening shifts separated by a comma: ").split(','))
            tip_percentage = 0.02
            total_shift_sales = morning_shift_sales + evening_shift_sales
            tips = total_shift_sales * tip_percentage
            print(f"Total Tips for the day: {tips}")
        elif choice == '6':
            break
        else:
            print('Invalid choice, please enter a number between 1 and 6.')
            print('Kindly press 6 to Exit the Operation: Thank You!')


# In[3]:


run_sales_operation()


# In[4]:


run_sales_operation()


# # *Challenge encountered during the process of encapsulating my code together in a one organized function of
# # run_sales_operation(): it such a taskful requirement to define user interface that can prompt user for different option of
# # operation ranging from 1-5 and 6 option to Exit the process. i really went through a series of code debugging from each
# # step of the operation code to others but it was such an interesting project to work on, which put me on a step of being
# # a solution provider for business entities as a data practitioner.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




