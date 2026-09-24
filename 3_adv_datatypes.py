data = b'hello' # Immutable bytes object
mutable_data = bytearray(b'Hello') # Mutable bytearray 
# object
view = memoryview(mutable_data) # Memory view of the 
# bytearray

print(data)
print(mutable_data)
print(view)

# NumPy arrays
import numpy as np

data1 = np.array([1, 2, 3, 4]) # 1Dimensional Array
data2 = np.array([[1, 2], [3, 4]]) # 2Dimensional Array
data3 = np.array([[[1], [2]], [[3], [4]]]) # 3Dimensional Array

# Performing element-wise operations
squared = data2 ** 2

print(data1)
print(data2)
print(data3)
print(squared)

# Pandas DataFrames - tabular data structures
# Good for filtering, grouping, merging, and aggregating
# large datasets
# For modern data analysis
import pandas as pd

pd_data = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [12, 30]})

# Filtering rows using conditions
adults = pd_data[pd_data['Age'] > 18]
print(adults)

# Adding new column
pd_data['isAdult'] = pd_data['Age'] > 18

# Print the DataFrame
print(pd_data)
