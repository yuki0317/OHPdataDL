from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("http://www.jamstec.go.jp/pacific21/OHP/SeismicData/")

Select fromYear = new Selector(driver.findElement(By.name("fromYear")));
Select fromManth = new Selector(driver.findElement(By.name("fromManth")));
Select fromDay = new Selector(drive.findElement(By.name("fromDay")));
select fromHour = new Selector(drive.findElement(By.name("fromHour")));
select fromMin = new Selector(drive.findElement(By.name("fromMin")));

Select toYear = new Selector(driver.findElement(By.name("toYear")));
Select toManth = new Selector(driver.findElement(By.name("toManth")));
Select toDay = new Selector(drive.findElement(By.name("toDay")));
select toHour = new Selector(drive.findElement(By.name("toHour")));
select toMin = new Selector(drive.findElement(By.name("toMin")));


