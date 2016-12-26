from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import re

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
	year = line[0:3]
	month = line[4:5]
	day = line[6:7]
	hour = line[8:9]
	minu = line[10:11]
#	else:
#		print('something wrong!')

	Select fromYear = new Selector(driver.findElement(By.name("fromYear")));
	Select fromMonth = new Selector(driver.findElement(By.name("fromMonth")));
	Select fromDay = new Selector(drive.findElement(By.name("fromDay")));
	Select fromHour = new Selector(drive.findElement(By.name("fromHour")));
	Select fromMin = new Selector(drive.findElement(By.name("fromMin")));

	Select toYear = new Selector(driver.findElement(By.name("toYear")));
	Select toMonth = new Selector(driver.findElement(By.name("toMonth")));
	Select toDay = new Selector(drive.findElement(By.name("toDay")));
	Select toHour = new Selector(drive.findElement(By.name("toHour")));
	Select toMin = new Selector(drive.findElement(By.name("toMin")));

	minu2 = int(minu) - 20
	fromYear.selectByVisibleText(year);
	fromMonth.selectByVisibleText(month);
	fromDay.selectByVisibleText(day);
	fromHour.selectByVisibleText(hour);
	fromMin.selectByVisibleText(str(minu2))

	driver.findElement(By.name("showAvailableStations")).click()

	Select station1 = new Selector(driver.findElement(By.name("stationID")));
	Select station2 = new Selector(driver.findElement(By.name("stationID")));
	Select station3 = new Selector(driver.findElement(By.name("stationID")));
	Select station4 = new Selector(driver.findElement(By.name("stationID")));
	Select station5 = new Selector(driver.findElement(By.name("stationID")));
	Select station6 = new Selector(driver.findElement(By.name("stationID")));

	station1.selectByVisibleText("PS.BAG");
	station1.selectByVisibleText("PS.KSI");
	station1.selectByVisibleText("PS.PLVO");
	station1.selectByVisibleText("PS.PSI");
	station1.selectByVisibleText("PS.SPVO");
	station1.selectByVisibleText("PS.VIVO");
	
	Selector component1 = new Selector(driver.findElement(By.name("channelID")));
	Selector component2 = new Selector(driver.findElement(By.name("channelID")));
	Selector component3 = new Selector(driver.findElement(By.name("channelID")));

	component1.selectByVisibleText("BHE");
	component2.selectByVisibleText("BHN");
	component3.selectByVisibleText("BHZ");

	
	driver.findElement(By.name("SEED")).click()

	driver.findElement(By.name("download")).click()
