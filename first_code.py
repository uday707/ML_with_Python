import pandas as pd

data = {'Name': ["John", "Anna", "Peter", "Linda"], 'Location': ["New York", "Paris", "Berlin", "London"], "Age": [24,13,53,33]}

data_pandas = pd.DataFrame(data)

print(data_pandas)