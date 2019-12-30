import requests

data = requests.get("https://gender-api.com/get?", params = {
	"name" : "Ваня",
	"country" : "MN",
	"key" : "BmaNBzxlbbqGUgDxVC"
	})

# print(data.json())
# ret = {'name': 'хулан', 'name_sanitized': 'Хулан', 'country': 'MN', 'gender': 'female', 'samples': 4, 'accuracy': 75, 'duration': '23ms', 'credits_used': 1}
# print(ret['gender'])

