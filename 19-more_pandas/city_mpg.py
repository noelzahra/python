import pandas as pd

df = pd.read_csv("vehicles.csv")
print(df.head())
city_mpg = df["city08"]
print(city_mpg.head())