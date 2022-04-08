import requests
import re 


class Days():
        def __init__(self,day_week,numbers_month,name_month,cloud_cover,day_temperature,night_temperature):
                self.day_week = day_week
                self.numbers_month = numbers_month
                self.name_month = name_month
                self.cloud_cover = cloud_cover
                self.day_temperature = day_temperature
                self.night_temperature = night_temperature

def get_weather_forecast():
	response = requests.get("https://world-weather.ru/pogoda/russia/nizhny_novgorod/")
	response.encoding = "utf-8"
	e=re.compile('vertical_tabs.+</ul>')
	res= e.findall(response.text)
	res= re.split("</li>",res[0])
	res.pop()
	
	data = []
	
	for i in res:
		res = i.split('<')
		day = res[2].split('>')[1]
		numbers_month = res[4].split('>')[1]
		name_month = res[6].split('>')[1]
		cloud_cover = res[8].split('title')[1][2:-2]

		temperature_day_and_night = i.split("day-temperature")[1].split("night-temperature")
		e = re.compile(">.\d+.<")
		try:
			day_temperature = e.findall(temperature_day_and_night[0])[0][1:-1]
		except:
			day_temperature = "0°"
		try:
			night_temperature = e.findall(temperature_day_and_night[1])[0][1:-1]
		except:
			night_temperature = "0°"	
		data.append(Days(day,numbers_month,name_month,cloud_cover,day_temperature,night_temperature))
	return data
