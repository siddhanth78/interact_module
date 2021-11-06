from selenium import webdriver
import time

web = 'https://www.whatsapp.com'
path = 'C:/Users/siddh/OneDrive/Desktop/chromedriver_win32/chromedriver'

driver = webdriver.Chrome(path)
driver.get(web)

time.sleep(5)

whatsappweb = driver.find_element_by_xpath('//*[@id="footer-wrapper"]/div/footer/div[1]/div/div[1]/a[4]/h4')
whatsappweb.click()

time.sleep(5)

papa = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[11]/div/div/div[2]/div[1]/div[1]')
papa.click()

