from matplotlib import pyplot as plt
import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
file_path = 'projet_data_4.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path,sep=";")
print(df)

column = 'G-PK90'
df_select = df[column]

plt.hist(df_select, bins=10, color='skyblue', edgecolor='black')

# Add labels and title
plt.xlabel(column)
plt.ylabel('Frequency')
plt.title('Histogram of '+column)

plt.savefig('./graph/4_Figure_'+column+'.png')