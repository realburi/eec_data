import pandas as pd
import numpy as np
import sys
from pprint import pprint 

subjects = ["History","Physics","Chemistry","Geography","English","Biology","Mathematic","Literature","Russian","Social_Science"]
result = []
for subject in subjects:
	df = pd.read_csv('./data/{}.csv'.format(subject))
	data = dict({ subject : df.query("Score == 800")[["Province","Name","Surname","Score"]].to_numpy()})
	result.append(data)
# pprint(result)

gender_data = pd.read_csv("gender.csv")
print(gender_data.Gender.value_counts())