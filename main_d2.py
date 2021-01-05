# 10 Day Coding Challenge - Day 2
# Title: Kartka z kalendarza
"""Description: Program wyswietla w czytelnej formie aktualna date, godzine, dzien tygodnia, pogode i losowy cytat.
                Jednostki powinny byc odpowiednio przeliczane.
                Program wykorzystuje request i datetime.
                Extra: Wyswietl czas dla kilku roznych miast oraz imieniny
"""

import requests
import datetime
import pytz
from selenium import webdriver

url = "https://community-open-weather-map.p.rapidapi.com/weather"
url_quotes = "https://quotes15.p.rapidapi.com/quotes/random/"

querystring = {"q":"Krakow,pl","lat":"0","lon":"0","callback":"","id":"2172797","lang":"eng","units":"metric","mode":"xml"}

headers = {
    'x-rapidapi-key': "59dd9170fbmsh540477cfa46ed2ap16d5c9jsn8e1f4e504634",
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }
headers_quotes = {
    'x-rapidapi-key': "59dd9170fbmsh540477cfa46ed2ap16d5c9jsn8e1f4e504634",
    'x-rapidapi-host': "quotes15.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
x = response.text.split("><")

response_quotes = requests.request("GET", url_quotes, headers=headers_quotes)
y = response_quotes.text.split("\",\"")

town = x[1][x[1].find("name") + 6 : -1]
temp_now = x[9][x[9].find("value") + 7 : x[9].find("min") - 2]
temp_min = x[9][x[9].find("min") + 5 : x[9].find("max") - 2]
temp_max = x[9][x[9].find("max") + 5 : x[9].find("unit") - 2]
press = x[15][x[15].find("value") + 7 : x[15].find("unit") - 2]
wind_str = x[18][x[18].find("name") + 6 : -1]
wind_from = x[22][x[22].find("name") + 6 : -1]
clouds = x[25][x[25].find("value") + 7 : x[25].find("name") - 2]
quote = y[1][y[1].find("content") + 10 : -1]
author = y[3][y[3].find("name") + 7 : ]

today = datetime.datetime.now()
print("Today is: " + str(today.day) + "th of " + str(today.strftime("%B")) + " " + str(today.year) + " " + str(today.strftime("%A")))
print("Actual time: " + today.strftime("%X"))

print("Actual weather conditions for " + town + ":")
print("Temperature now: " + temp_now + " celsius")
print("Temperature max: " + temp_max + " celsius")
print("Temperature min: " + temp_min + " celsius")
print("Pressure: " + press + " hPa")
print("Wind strength is " + wind_str + " from " + wind_from)
print("Clouds are covering " + clouds + "% of the sky")
print("Random quote for now is: \"" + quote + "\" by " + author )

print()
print("Below you can find some timezones for different cities: ")

source_time_zone = pytz.timezone("Europe/Warsaw")
source_date_with_timezone = source_time_zone.localize(today)
print("-for Warsaw timezone it is: " + str(source_date_with_timezone))

lisbon_time_zone = pytz.timezone("Europe/Lisbon")
lisbon_date_with_timezone = source_date_with_timezone.astimezone(lisbon_time_zone)
print("-for Lisbon it is: " + str(lisbon_date_with_timezone))

sydney_time_zone = pytz.timezone("Australia/Sydney")
sydney_date_with_timezone = source_date_with_timezone.astimezone(sydney_time_zone)
print("-for Sydney it is: " + str(sydney_date_with_timezone))

tijuana_time_zone = pytz.timezone("America/Tijuana")
tijuana_date_with_timezone = source_date_with_timezone.astimezone(tijuana_time_zone)
print("-for Tijuana it is: " + str(tijuana_date_with_timezone))

browser = webdriver.Chrome('C:/Users/milek/Downloads/chromedriver.exe')
browser.get("https://imienniczek.pl/widget/js")

imie_1 = browser.find_element_by_xpath("//*[@id=\"imienniczek\"]/a[2]")
imie_2 = browser.find_element_by_xpath("//*[@id=\"imienniczek\"]/a[3]")
imie_3 = browser.find_element_by_xpath("//*[@id=\"imienniczek\"]/a[4]")

print("Today is a day of: " + imie_1.text[:-1] + "a, " + imie_2.text[:-1] + "a and " + imie_3.text[:-1] + "a")

browser.quit()