#!/usr/bin/env python
# coding: utf-8

# In[4]:

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import re
import numpy as np
import xlwings as xw


# Step 1: Read the data from the Excel file
#excel_file = 'configMacroV2.xlsm'
#df = pd.read_excel(excel_file, sheet_name='Conveyors config')
workbook = xw.Book('configMacroV.xlsm')
sheet1 = workbook.sheets['Conveyors config'].used_range.value
df = pd.DataFrame(sheet1)
new_header = df.iloc[0] #grab the first row for the header
df = df[1:] #take the data less the header row
df.columns = new_header #set the header row as the df header
df = df.dropna(subset=['id'])
df


# Step 2: Create a 3D plot
fig = plt.figure(figsize=(20, 10))  # Adjust the width and height as needed
ax = fig.add_subplot(111, projection='3d')

# Step 3: Iterate through each row in the dataframe and plot the lines
for index, row in df.iterrows():
    line_name = row['id']
    coordinates = row['points in length units']
    line_color = row['color']

    # Parse the coordinates string to include negative numbers
    pattern = r'\{(-?\d+\.?\d*),\s*(-?\d+\.?\d*),\s*(-?\d+\.?\d*)\}'
    matches = re.findall(pattern, coordinates)
    coordinates = [(float(x), float(y), float(z)) for x, y, z in matches]

    # Check if we have at least two points
    if len(coordinates) < 2:
        print(f"Skipping line '{line_name}' because it does not have at least two points.")
        continue

    # Separate the coordinates into x, y, z lists
    x_values = [coord[0] for coord in coordinates]
    y_values = [coord[1] for coord in coordinates]
    z_values = [coord[2] for coord in coordinates]

    # Plot the line with smaller marker size
    ax.plot(y_values, x_values, z_values, marker='.', color=line_color, label=line_name, markersize=3)  # Adjust markersize as needed

# Step 4: Set labels for the axes
ax.set_xlabel('Y')
ax.set_ylabel('X')
ax.set_zlabel('Z')

# Step 5: Add a legend outside the plot
ax.legend(loc='center left', bbox_to_anchor=(1.05, 0.5))

# Step 6: Interchange the positions of the XYZ axes
ax.view_init(elev=90, azim=0)  # Adjust the viewing angle as needed
#ax.view_init(elev=30, azim=-60)  # Adjust the viewing angle as needed

# Step 7: Adjust layout and show the plot
plt.tight_layout()
plt.show()