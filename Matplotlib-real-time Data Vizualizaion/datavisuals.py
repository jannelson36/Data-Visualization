
import pandas as pd
import matplotlib.pyplot as plt
  
  
# reading the database
Names = ['x','Cat','Dat','Eat','Pat','Kat','Tat','x']
Marks = ['0','40','50','60','70','80','90','0']
  
# Scatter plot with day against tip
plt.bar(Names, Marks)
plt.scatter(Names, Marks)

# Adding Title to the Plot
plt.title("Scatter Plot")
  
# Setting the X and Y labels
plt.xlabel('Names')
plt.ylabel('Marks')
  
plt.show()