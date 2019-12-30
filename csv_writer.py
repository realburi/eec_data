from pprint import pprint 
import pandas as pd 
from eec import crawler as crawl
import csv

subjects = ["History","Physics","Chemistry","Geography","English","Biology","Mathematic","Literature","Russian","Social_Science"]
provinces = "Архангай,Баян-Өлгий,Баянхонгор,Булган,Говь-Алтай,Говьсүмбэр,Дархан-Уул,Дорноговь,Дорнод,Дундговь,Завхан,Орхон,Сэлэнгэ,Сүхбаатар,Төв_аймаг,Увс,Ховд,Хэнтий,Хөвсгөл,Өвөрхангай,Өмнөговь,Багануур,Улаанбаатар".split(",")

for j in range(1,11):
	with open('./data/{}'.format(subjects[j-1]) + '.csv', 'w', newline="", encoding="UTF-8") as file:
		print(subjects[j-1])
		writer = csv.writer(file)
		writer.writerow("Rank,Score,ID,Surname,Name,First_Score,Scaled_Score,Percental,Grade,Province".split(","))
		for aimag in range(1,24):
			for data in crawl("http://list.eec.mn/{}/{}.html?".format(aimag,j)):
				if "Байр" in data:
					pass
				else:
					data.append(provinces[aimag-1])
					writer.writerow(data)
		