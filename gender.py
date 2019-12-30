import requests
import pandas as pd
from pprint import pprint
import csv 

df = pd .read_csv("./data/Literature.csv")
names = list(set(df.Name.to_numpy()))

with open('gender.csv', 'w', newline="", encoding="UTF-8") as file:
		writer = csv.writer(file)
		writer.writerow(["Name","Gender"])
		for name in range(467):			
			data = requests.get("https://gender-api.com/get?", params = {
			"name" : name,
			"country" : "MN",
			"key" : "BmaNBzxlbbqGUgDxVC"
			})

			writer.writerow([names[name],data.json()['gender']])
			print(names[name],data.json()['gender'])
