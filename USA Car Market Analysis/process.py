#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import tui

file_path = "CarPrice.csv"
records = []

try:
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        headings = next(csv_reader)
        
        for rows in csv_reader:
            records.append(rows)
except IOError:
    print("File could not be read")


# In[3]:


# A. Load the data from a CSV file
def a():
    tui.started("Loading records")
    for record in records:
        rec = (f"{len(records)} records loaded successfully")
        return rec
        tui.closing()


# In[ ]:


# B. Retrieve a record for an individual car by id
def b():
    import pandas as pd
    df = pd.read_csv("carPrice.csv")
    try:
        tui.started("Retrieving record for individual cars")
        selection = input("What car ID information do you want (1-205)?\n")
        carid = int(selection)
        chosen_ID = df.iloc[carid -1] # -1 is used so the exact car_id on the csv is displayed and not the index number
        return chosen_ID
        tui.closing()
    except IOError:
        print("Invalid input pls try again")


# In[ ]:


# C. Retrieve all cars for a specified cylinder number
def c():
    import pandas as pd
    df = pd.read_csv("carPrice.csv")
    tui.started("Retrieving all cars for a specified cylinder number")
    selection = input('Please select choice of car based on number of cylinder numbers(2,3,4,5,6,8,12)\n')
    try:
        num = df.loc[df['cylindernumber'] ==int(selection)]
        return num
        tui.closing()
    except:
        print("Invalid input pls try again")

# it can also be displayed using; df.loc[df['cylindernumber'] ==int(selection)]


# In[ ]:


# D. Retrieve all cars in the specified car body
def d():
    import pandas as pd
    df = pd.read_csv("carPrice.csv")
    tui.started("Retrieving all cars based on specified car body")
    selection = input('Please select choice of car based on car body(convertible,hatchback,wagon,hardtop,sedan,)\n')
    try:
        carbody = df.loc[df['carbody'] ==str(selection)]
        return carbody
        tui.closing()
    except IOError:
        print("Error! Please select the right input")


# In[ ]:


# E. Retrieve a specific number of columns (2 up to 5) related to an individual car by id
def e():
    import pandas as pd
    df = pd.read_csv("carPrice.csv")
    tui.started("Retrieving data based on specific columns")
    # Ask the user for the car ID
    selection = int(input('Enter the car ID: '))
    # Select the row with the specified car ID
    car = df.loc[df['car_ID'] == selection]
    # Select the car_id, carName, fueltype, drivewheel abd horspower
    selected_columns = car[['CarName', 'fueltype', 'drivewheel', 'horsepower', 'price']]
    # Print the selected columns
    return selected_columns
    tui.closing()


# In[ ]:


# F. Retrieve the car names alphabetically
def f():
    import pandas as pd
    df = pd.read_csv("carPrice.csv")
    tui.started("Retrieving names of cars alphabetically")
    a_z = df.sort_values('car_ID')
    return a_z
    tui.closing()


# In[ ]:


# Retrieve summary of sales (total car price) for each car body
def g():
    import pandas as pd
    import numpy as np
    df = pd.read_csv("carPrice.csv")
    # Group the DataFrame by car body
    df_grouped = df.groupby('carbody')

    # Define a function to select the top 5 car sales for each group
    def top_5_sales(group):
        return group.sort_values('price', ascending=False).head(5)

    # Apply the function to each group and store the results in a new DataFrame
    df_top5 = df_grouped.apply(top_5_sales)

    # Print the resulting DataFrame
    return df_top5
    tui.closing()


# In[ ]:


# Retrieve top 5 car sales per car body
def h():
    import pandas as pd
    df = pd.read_csv("carPrice.csv")
    tui.started("Retrieving top 5 car sales")
# Sort the data by price
    sort = df.sort_values(by='price', ascending=False)
# Group the sorted data according to car body
    grouped = sort.groupby('carbody')
    top_5 = grouped.head(1)
#  Display result
    return top_5
    tui.closing()


# In[ ]:


# I. Retrieve the detail of cars based on your own selection
def i():
    import pandas as pd
    df = pd.read_csv("carPrice.csv")
    tui.started("Retrieving details of cars based on drivewheel")
    # retrieving car details based on drivewheel(4wd)
    drive_wheel = df.loc[df['drivewheel'] == '4wd']
    return drive_wheel
    tui.closing()


# In[ ]:



# J.Display the number of cars per fuel system using a bar chart
def j():
    import pandas as pd
    df = pd.read_csv("carPrice.csv")
    tui.started("Plotting bar chart for cars per fuel system")
    get_ipython().run_line_magic('matplotlib', 'inline')
    import matplotlib.pyplot as plt
# Group the DataFrame by fuel system and count the number of cars in each group
    fuel_counts = df.groupby('fuelsystem')['fuelsystem'].count()
# Generate a bar chart
    fig = plt.figure(figsize=(15,8))
    fuel_counts.plot(kind='bar')

    plt.title('Cars per fuel system')
# Show the plot
    plt.show()
    tui.closing()


# In[ ]:


# K.Display the horsepower of the top 5 car sale by price (the cheapest) using a subplot
def k():
    import pandas as pd 
    import matplotlib.pyplot as plt
    get_ipython().run_line_magic('matplotlib', 'inline')
    df = pd.read_csv("carPrice.csv")
    tui.started("Displaying subplot for horsepower of top 5 car sale by price")
     # Sort the DataFrame by price 
    fig, ax = plt.subplots(figsize=(14, 7)) #Setting a suitable fig size for the subplot
    data_tmp = df.sort_values(by='price')[:5]
    carname = data_tmp['CarName'].to_list()
    hp = data_tmp['horsepower'].to_list()
    plt.suptitle("Horsepower of top 5 car sale (Cheapest)", fontsize=17)
    for x in range(len(data_tmp['CarName'])): #iterate through the length to add new subplots
        ax = plt.subplot(1, 5, x + 1)
        ax.bar(carname[x],hp[x])
        ax.set_ylim(0,100)
    plt.show()
    tui.closing()
   


# In[4]:


# # L.Display percentage of car purchase in relation to horspower using pie chart
def l():
    import pandas as pd 
    import matplotlib.pyplot as plt
    get_ipython().run_line_magic('matplotlib', 'inline')
    df = pd.read_csv("carPrice.csv")
    tui.started("Displaying percentage of car purchase in relation to horsepower")
    df = pd.read_csv("carPrice.csv")

    # Extract the horsepower and price data
    fuel = df['fueltype']
    data = {'gas': 0, 'diesel': 0}
    for ft in fuel:
        data[ft] += 1
    plt.figure(figsize=(7, 7))
    plt.pie(data.values(), labels=data.keys())
    plt.title("Pie chart showing the percentage of cars that use either gas or diesel")
    plt.legend(loc='upper right')
    plt.show()
    tui.closing()


# In[ ]:




