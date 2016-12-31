from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import datetime
import time

gcmtlist = open('gcmtlistFile.txt')
lines = gcmtlist.readlines()
gcmtlist.close()

driver = webdriver.Firefox()
driver.get("http://www.jamstec.go.jp/pacific21/OHP/SeismicData/")

for line in lines:
#	if len(line) == 7:
#		if line[5] == 0:
#			year = 20 + line[5:6]
#			month = line[0:1]
#			day = line[2:3]
#		elif line[5] == 9:
#			year = 19 + line[5:6]
#			month = line[0:1]
#			day = line[2:3]
#		else:
#			print('something wrong!')
#	elif len(line) == 13:
	year = line[0:4]
	month = line[4:6]
	day = line[6:8]
	hour = line[8:10]
	minu = line[10:12]

	print(year, month, day, hour, minu)
	origintime = datetime.datetime(int(year), int(month), int(day), hour=int(hour), minute=int(minu))
	starttime = origintime - datetime.timedelta(minutes=20)
	endtime = starttime + datetime.timedelta(hours=2)
#	else:
#		print('something wrong!')

	fromYear = Select(driver.find_element_by_name("fromYear"));
	fromMonth = Select(driver.find_element_by_name("fromMonth"));
	fromDay = Select(driver.find_element_by_name("fromDay"));
	fromHour = Select(driver.find_element_by_name("fromHour"));
	fromMin = Select(driver.find_element_by_name("fromMinute"));

	toYear = Select(driver.find_element_by_name("toYear"));
	toMonth = Select(driver.find_element_by_name("toMonth"));
	toDay = Select(driver.find_element_by_name("toDay"));
	toHour = Select(driver.find_element_by_name("toHour"));
	toMin = Select(driver.find_element_by_name("toMinute"));
#
	fromYear.select_by_visible_text(str(starttime.year));
	fromMonth.select_by_visible_text(str(starttime.month));
	fromDay.select_by_visible_text(str(starttime.day));
	fromHour.select_by_visible_text(str(starttime.hour));
	fromMin.select_by_visible_text(str(starttime.minute));
	toYear.select_by_visible_text(str(endtime.year));
	toMonth.select_by_visible_text(str(endtime.month));
	toDay.select_by_visible_text(str(endtime.day));
	toHour.select_by_visible_text(str(endtime.hour));
	toMin.select_by_visible_text(str(endtime.minute));
#
	driver.find_element_by_name("showAvailableStations").click()
	time.sleep(5)

	station = Select(driver.find_element_by_name('stationID'));
	station1 = Select(driver.find_element_by_name('stationID'));
	station2 = Select(driver.find_element_by_name("stationID"));
	station3 = Select(driver.find_element_by_name("stationID"));
	station4 = Select(driver.find_element_by_name("stationID"));
	station5 = Select(driver.find_element_by_name("stationID"));
	station6 = Select(driver.find_element_by_name("stationID"));
#
#	station.select_by_value('"0"')
	station1.select_by_visible_text(str("PS.BAG"));
	station2.select_by_visible_text('PS.KSI');
	station3.select_by_visible_text('PS.PLVO');
	station4.select_by_visible_text('PS.PSI');
	station5.select_by_visible_text('PS.SPVO');
	station6.select_by_visible_text('PS.VIVO');
#	

	component1 = Select(driver.find_element_by_name("channelID"));
	component2 = Select(driver.find_element_by_name("channelID"));
	component3 = Select(driver.find_element_by_name("channelID"));
#
	component1.select_by_visible_text('BHE');
	component2.select_by_visible_text('BHN');
	component3.select_by_visible_text('BHZ');
#	
	driver.find_element_by_id("fseed").click()
	time.sleep(3)

	driver.find_element_by_name("download").click()
	time.sleep(7)
driver.close()
