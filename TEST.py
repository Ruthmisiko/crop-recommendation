from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
 
dataset = load_iris()
object= StandardScaler()
 
# Splitting the independent and dependent variables
i_data = dataset.data
response = dataset.target
 
# standardization 
scale = object.fit_transform(i_data) 
print(scale)