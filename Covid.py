import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as amn
import numpy as np

# reading the csv file first
dataset = pd.read_csv("Dataset.csv")
# get the first 5 head of the dataset
print(dataset)
# get the last 5 tails of the dataset
print(dataset.tail(5))

# getting the covid data for australia
dataset_australia = dataset[dataset["Country"] == "Australia"]
print(dataset_australia.head(5))
plt.bar(x="Date", height="Confirmed", color="red", data=dataset_australia)
plt.xlabel("Date from 22nd Jan to 30th Aug")
plt.ylabel("Total number of confirmed cases")
plt.title("Australia")
plt.show()

# dataset for india
dataset_india = dataset[dataset["Country"] == "India"]
print(dataset_india.head(5))
plt.bar(x="Date", height="Confirmed", color="green", data=dataset_india)
plt.xlabel("Date from 22nd Jan to 30th Aug")
plt.ylabel("Total number of confirmed cases")
plt.title("India")
plt.show()


# getting the covid data for china
dataset_china = dataset[dataset["Country"] == "China"]
print(dataset_china.head(10))
plt.bar(x="Date", height="Confirmed", color="yellow", data=dataset_china)
plt.xlabel("Date from 22nd Jan to 30th Aug")
plt.ylabel("Total number of confirmed cases")
plt.title("China")
plt.show()

date_lists = dataset["Date"].unique()
print(date_lists)


