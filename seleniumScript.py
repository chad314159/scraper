import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def init_driver():
    #driver = webdriver.Chrome()
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images":2}
    chromeOptions.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(chrome_options=chromeOptions)
    driver.wait = WebDriverWait(driver, 25)
    return driver
 
 
def lookup(driver, query):
    driver.get("https://www.tripadvisor.com/Restaurant_Review-g53942-d544336-Reviews-The_Steak_House-Wellsboro_Pennsylvania.html")
    try:
	content = driver.find_element_by_css_selector('span.taLnk.ulBlueLinks');    
	content.click();
	#element = driver.find_element_by_xpath("//div[@id='ui_column is-9']//div[@id='innerBubble']//div[@id='wrap']//div[@id='prw_rup prw_reviews_text_summary_hsx']//p[@id='partial_entry']]//span[@id='taLnk ulBlueLinks']")
	#element.click();
    except TimeoutException:
        print("Box or Button not found in google.com")
 
 
if __name__ == "__main__":
    driver = init_driver()
    lookup(driver, "Selenium")
    time.sleep(5)
    driver.quit()
