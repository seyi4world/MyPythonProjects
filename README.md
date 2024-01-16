This code defines a simple "Customer Management System" and "Automating Accounting Task" for a local retail business dealing with variety of products, aims to stremline and automate accounting produdures...

For "Customer Management System" using a CSV file. It includes functions to automate company customer information:- 
A. * Add Details (add_details): Takes user input for customer name, number, and email, then appends this information to a CSV file named 'cus_data.csv'.
B. * View Information (view_info): Reads the 'cus_data.csv' file using pandas and displays the customer details in a tabular format. If the file is empty, it notifies the user.
C. * Search Name (search_name): Takes a customer name as input, reads the CSV file, and searches for a customer with the given name. It returns the matching records or notifies if the name is not found.
D. * Delete Name (delete_name): Takes a customer name as input, reads the CSV file, deletes the customer with the specified name, and updates the 'cus_data.csv' file. It notifies the user if the name is not found."""
E. * In summary, this code aims to create a basic customer management system that allows adding, viewing, searching, and deleting customer details stored in a CSV file.

For "Automating Essential Accounting Tasks" including calculating total sales, worker salaries, profit, tips, and total tips for the day. in which business operates two shifts per day with one worker on each shift:
These includes fuctions to automate the whole process of accounting tasks by:-
A. * Calculate Total Sales for the Day
B. * Calculate Worker's Salary
C. * Calculate Profit
D. * Calculate Tips for a Shift
E. * Calculate Total Tips for the Day
F. * Exit.
The whole process is to encapsulate the each accounting tasks into a functions that will prompts user to input there choice in the provided option range between(1-6), 
perform the process according to the provided option from the user and to Exit by picking the last option to end the process.
