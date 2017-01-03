/**
 * 
 */
package ohpDataDL;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.time.LocalDateTime;
import java.util.stream.Stream;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.Select;

import io.github.kensuke1984.kibrary.util.globalcmt.GlobalCMTID;

/**
 * @version 0.0.1
 * @since 2016/12/30
 * @author Yuki
 *
 */
public class OHPdataDL {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO 自動生成されたメソッド・スタブ
		String geckoPath = "/usr/local/bin/geckodriver";
		System.setProperty("webdriver.gecko.driver", geckoPath);
		WebDriver driver = new FirefoxDriver();
		driver.get("http://www.jamstec.go.jp/pacific21/OHP/SeismicData");
		
		try (Stream<String> a = Files.lines(Paths.get("/Users/Yuki/github/OHPdataDL/gcmtlistFile.txt"))) {
			a.map(String::toUpperCase).forEach(line -> {
				GlobalCMTID id = new GlobalCMTID(line);
				LocalDateTime origin = id.getEvent().getCMTTime();
				LocalDateTime start = origin.minusMinutes(20);
				LocalDateTime end = start.plusHours(2);
				
				Select fromYear = new Select(driver.findElement(By.name("fromYear")));
				Select fromMonth = new Select(driver.findElement(By.name("fromMonth")));
				Select fromDay = new Select(driver.findElement(By.name("fromDay")));
				Select fromHour = new Select(driver.findElement(By.name("fromHour")));
				Select fromMin = new Select(driver.findElement(By.name("fromMinute")));
				Select toYear = new Select(driver.findElement(By.name("toYear")));
				Select toMonth = new Select(driver.findElement(By.name("toMonth")));
				Select toDay = new Select(driver.findElement(By.name("toDay")));
				Select toHour = new Select(driver.findElement(By.name("toHour")));
				Select toMin = new Select(driver.findElement(By.name("toMinute")));
				
				fromYear.selectByVisibleText(String.valueOf(start.getYear()));
				fromMonth.selectByVisibleText(String.valueOf(start.getMonthValue()));
				fromDay.selectByVisibleText(String.valueOf(start.getDayOfMonth()));
				fromHour.selectByVisibleText(String.valueOf(start.getHour()));
				fromMin.selectByVisibleText(String.valueOf(start.getMinute()));
				toYear.selectByVisibleText(String.valueOf(end.getYear()));
				toMonth.selectByVisibleText(String.valueOf(end.getMonthValue()));
				toDay.selectByVisibleText(String.valueOf(end.getDayOfMonth()));
				toHour.selectByVisibleText(String.valueOf(end.getHour()));
				toMin.selectByVisibleText(String.valueOf(end.getMinute()));
				
				driver.findElement(By.name("showAvailableStations")).click();
				try {
				    Thread.sleep(5000);
				} catch (InterruptedException e) {
				    e.printStackTrace();
				}
				
//				Select station = new Select(driver.findElement(By.name("stationID")));
				Select station1 = new Select(driver.findElement(By.name("stationID")));
				Select station2 = new Select(driver.findElement(By.name("stationID")));
				Select station3 = new Select(driver.findElement(By.name("stationID")));
				Select station4 = new Select(driver.findElement(By.name("stationID")));
				Select station5 = new Select(driver.findElement(By.name("stationID")));
				Select station6 = new Select(driver.findElement(By.name("stationID")));
				
//				station.selectByValue("0");
				station1.selectByVisibleText("PS.BAG");
				station2.selectByVisibleText("PS.KSI");
				station3.selectByVisibleText("PS.PLVO");
				station4.selectByVisibleText("PS.PSI");
				station5.selectByVisibleText("PS.SPVO");
				station6.selectByVisibleText("PS.VIVO");
				
				Select component1 = new Select(driver.findElement(By.name("channelID")));
				Select component2 = new Select(driver.findElement(By.name("channelID")));
				Select component3 = new Select(driver.findElement(By.name("channelID")));
				
				component1.selectByVisibleText("BHE");
				component2.selectByVisibleText("BHN");
				component3.selectByVisibleText("BHZ");
				
				
				driver.findElement(By.id("fseed")).click();
				try {
				    Thread.sleep(2000);
				} catch (InterruptedException e) {
				    e.printStackTrace();
				}
				
				driver.findElement(By.name("download")).click();
				try {
				    Thread.sleep(15000);
				} catch (InterruptedException e) {
				    e.printStackTrace();
				}
			});
		} catch (IOException e) {
		    e.printStackTrace();
		}
		
		driver.close();
	}

}
