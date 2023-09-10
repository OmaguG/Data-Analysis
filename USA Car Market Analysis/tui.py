#!/usr/bin/env python
# coding: utf-8

# In[ ]:


line_width = 100

def welcome(msg=""):
    output = f"Car Price Analysis Program started: {msg}"
    print('Hello ' + input('What is your name? ') + ", welcome to USA car market analysis program")
    art = "*" * line_width
    print(f"{art}\n{output}\n")
    
def started(msg=""):
    output = f"Query initiated: {msg}...."
    print(f"\n{output}\n")
    
def closing(msg=""):
    art = "*" * line_width
    print(f"Query completed.\n{art}")
    
def completion(msg=""):
    art = "*" * line_width
    print(f"{art}\nThank you for using my car analysis program. GOODBYE!.")

def error(msg):
    print(f"Error! {msg}\n")
    
    
def menu():
    print(f"""Please select from the following options:
    {"[a]"} Load data
    {"[b]"} Retrieve a record for an individual car by id
    {"[c]"} Retrieve all cars for a specified cylinder number
    {"[D]"} Retrieve all cars in the specified car body
    {"[e]"} Retrieve a specific number of columns (2 up to 5) related to an individual car by id
    {"[f]"} Retrieve the car names alphabetically
    {"[g]"} Retrieve summary of sales (total car price) for each car body
    {"[h]"} Retrieve the top 5 car sale by price (the most expensive) and per car body
    {"[i]"} Retrieve the detail of cars based on your own selection
    {"[j]"} Display the number of cars per fuel system using a bar chart
    {"[k]"} Display the horsepower of the top 5 car sale by price (the cheapest) using a subplot
    {"[l]"} Display the selection of data by your choice to present the customers’ buying behaviour using a suitable visualisation
    {"[exit]"} Exit Program
    """)
    menu_opt = input("Your selection: ")
    return menu_opt.strip().lower()


# In[ ]:




