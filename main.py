import pandas as pd

df = pd.read_csv('iris_csv.csv')
df.to_csv('s3://smurfcoders/iris.csv')