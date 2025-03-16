import pytest
from appium import webdriver
from appium.webdriver.common.MobileBy import MobileBy
from datetime import datetime, timedelta

@pytest.fixture
def driver():
    desired_caps = {
    'platformName': 'Android',           
    'deviceName': 'Task2',         #假設TASK2為手機名
    'platformVersion': '11',            #Android 版本
    'appPackage': 'hko.MyObservatory_v1_0',  
    'appActivity': '.MainActivity',     
    'automationName': 'UiAutomator2'   
}
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    yield driver
    driver.quit()

def test_weather_forecast_date(driver):
 from datetime import datetime

driver.implicitly_wait(10)
forecast_button = driver.find_element(MobileBy.ACCESSIBILITY_ID, "9-Day Forecast")
forecast_button.click()
date_element = driver.find_element(MobileBy.XPATH, "//android.widget.TextView")  
displayed_date = date_element.text  
date_part = displayed_date.split(' (')[0]  
try:
    parsed_date = datetime.strptime(date_part, "%d %b")  
    parsed_date = parsed_date.replace(year=datetime.now().year)  
except ValueError as e:
    assert False, f"讀取日期失誤: {date_part}, 錯誤: {e}"

today = datetime.now().date()

assert parsed_date.date() == today, \
    f"預訂日期為 {today}，但得到的日期為 {parsed_date.date()}"


