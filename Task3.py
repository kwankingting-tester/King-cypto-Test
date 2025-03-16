from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
url = "https://www.szse.cn/English/siteMarketData/siteMarketDatas/lookup/index.html?code=000001"
driver.get(url)
time.sleep(10)
try:
    high_elements = driver.find_elements(By.CSS_SELECTOR,"li:nth-child(5) span:nth-child(2)")
    low_elements = driver.find_elements(By.CSS_SELECTOR,"li:nth-child(6) span:nth-child(2)")
    
    high_price = high_elements[0].text
    low_price = low_elements[0].text
   
    high = float(high_price)
    low = float(low_price)
  
    if high > low:
        print(f"High ({high}) > Low ({low}): Successful")
    else:
        print(f"High ({high}) <= Low ({low}): Fail")
except Exception as e:
    print(f"Error: {e}")
finally:
    driver.quit()