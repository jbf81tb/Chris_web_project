from selenium import webdriver
import datetime as dt
import time
import json

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)

startingDate = dt.datetime.now().date()

with open('times_and_links.json') as f:
    times_and_links = json.load(f)

times_and_links.sort(key = lambda x: (x['time']['day'], x['time']['hour'], x['time']['minute']))
numLinks = len(times_and_links)


for i, tl in enumerate(times_and_links):
    nextDay = tl['time']['day']
    nextHour = tl['time']['hour']
    nextMinute = tl['time']['minute']
    nextTime = dt.time(hour=nextHour, minute=nextMinute)


    driver.get(tl['link'])
    if i>0:
        driver.fullscreen_window()

    if i == numLinks-1:
        break


    now = dt.datetime.now()
    while now.time() <= nextTime and (now.date()-startingDate).days <= nextDay:
        time.sleep(1)
        now = dt.datetime.now()

input("Press Enter to close program.")
driver.quit() 