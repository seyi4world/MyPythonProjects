#!/usr/bin/env python
# coding: utf-8

# # >> This code defines a simple customer management system using a CSV file. It includes functions to automate company customer information:
# 
# # * Add Details (add_details): Takes user input for customer name, number, and email, then appends this information to a CSV file named 'cus_data.csv'.
# 
# # * View Information (view_info): Reads the 'cus_data.csv' file using pandas and displays the customer details in a tabular format. If the file is empty, it notifies the user.
# 
# # * Search Name (search_name): Takes a customer name as input, reads the CSV file, and searches for a customer with the given name. It returns the matching records or notifies if the name is not found.
# 
# # * Delete Name (delete_name): Takes a customer name as input, reads the CSV file, deletes the customer with the specified name, and updates the 'cus_data.csv' file. It notifies the user if the name is not found."""
# 
# # * In summary, this code aims to create a basic customer management system that allows adding, viewing, searching, and deleting customer details stored in a CSV file.

# In[1]:


import pandas as pd


# In[2]:


def add_details():
    # Prompt user for customer name
    cust_name = input("Enter customer name: ")
    
    try:
        # Attempt to read the CSV file into a pandas DataFrame
        df = pd.read_csv('cust_data.csv') # header=None, names=['Customer Name', 'Phone Number', 'Email:'])
        
        # Check if the name already exists
        existing_name = df[df['Customer Name'].str.lower() == cust_name.lower()]
        
        # If the name exists
        if not existing_name.empty:
            print(f"Customer '{cust_name}' already exists in the inventory.")
            update_option = input('Do you want to update the existing name? (y/n): ').lower()
            
            # If user chooses to update the existing name
            if update_option == 'y':
                # Get new phone number and email
                NewPhone_number = int(input('Enter new phone number: '))
                New_Email = input('Enter new email: ')
                
                # Update phone number and email for the existing name
                df.loc[df['Customer Name'].str.lower() == cust_name.lower(), 
                       ['Phone Number', 'Email:']] = [NewPhone_number, New_Email]
                
                # Save the updated DataFrame back to the CSV file
                df.to_csv('cust_data.csv', index=False)
                print(f'Customer: {cust_name} updated successfully.')
                return df
            else:
                # If user chooses not to update, exit the function
                print('No changes made.')
                return
    except FileNotFoundError:
        # If the file doesn't exist, create a new DataFrame with column names
        df = pd.DataFrame(columns=['Customer Name', 'Phone Number', 'Email:'])
    
    # Prompt user for phone number and email
    phonenumber = int(input('Enter phone number: '))
    email = input('Enter email address: ')
    
    # Add new name to the DataFrame
    NewCust_name = pd.DataFrame({'Customer Name': [cust_name], 'Phone Number': [phonenumber], 'Email:': [email]})
    df = pd.concat([df, NewCust_name], ignore_index=True)
    
    # Print the updated DataFrame
    print(df)
    
    # Save the updated DataFrame back to the CSV file
    df.to_csv('cust_data.csv', index=False)
    
    print(f'Customer: {cust_name} added successfully!\n')
    return df


# In[3]:


# View inventory
def view_info():
    try:
        # Attempt to read the CSV file into a pandas DataFrame
        df = pd.read_csv('cust_data.csv') # header was removed:
        
        # Check if the DataFrame is empty
        if df.empty:
            print('No available customer information')
        else:
            print('\n')
            print('Customer information:')
            return df
    except FileNotFoundError:
        print('Custmer information does not exist')

# Search for a product
def search_name():
    # Prompt user for the name of the product to search
    search_name = input('Enter the name of the customer to search: ')
    
    try:
        # Attempt to read the CSV file into a pandas DataFrame
        df = pd.read_csv('cust_data.csv') #, header=None, names=['Customer Name', 'Phone Number', 'Email'])
        # removed header and columns
        
        # Filter the DataFrame based on the search name
        result = df[df['Customer Name'].str.lower() == search_name.lower()]

        # Check if the result DataFrame is empty
        if result.empty:
            print(f"No customer with the name :'{search_name}'")
        else:
            print('Customer name found:')
            print(result)
    except FileNotFoundError:
        print('Customer name not found')


# In[4]:


add_details()


# In[5]:


view_info()


# In[6]:


search_name()


# In[7]:


def delete_name():
    cust_name = input('Enter the name of the customer to delete: ')
    try:
        # read the csv file into a pandas dataframe
        df = pd.read_csv('cust_data.csv', header=None, names=['Customer Name', 'Phone Number', 'Email:'])
        
        #check if the name already exists
        result = df[df['Customer Name'].str.lower() == cust_name.lower()]
        
        if result.empty:
            print(f"No customer found with the name '{cust_name}'. ")
        else:
            df = df[df['Customer Name'].str.lower() != cust_name.lower()]
            df.to_csv('cust_data.csv', index=False)
            
            # notify the user that the change has been made
            print(f"Customer: '{cust_name}' deleted succesfuly.")
    except FileNotFoundError:
        print("No available customer information.")


# In[8]:


delete_name()


# In[9]:


def run_cust_management():
    while True:
        print('\nCustomer Management System')
        print('1, add_details')
        print('2, view_info')
        print('3, search_name')
        print('4, delete_name')
        print('5, Exit')
    
        choice = input('Enter your choice (1-5): ')
        if choice == '1':
            add_details()
        elif choice == '2':
            view_info()
        elif choice == '3':
            search_name()
        elif choice == '4':
            delete_name()
        elif choice == '5':
            break
        else:
            print('Invalid choice, please enter a number between 1 and 5.')


# In[11]:


run_cust_management()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




