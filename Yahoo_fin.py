from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.action_chains import ActionChains

PATH = '/Users/alexduntoye/chromedriver'

driver = webdriver.Chrome(PATH)

driver.get('https://uk.finance.yahoo.com/')

time.sleep(4)

cookie_monster = driver.find_element_by_xpath('//button[@name="agree"]').submit()

time.sleep(4)

quote_look_up = driver.find_element_by_xpath('//input[@id="yfin-usr-qry"]')

quote_look_up.send_keys("FB")

quote_look_up.send_keys(Keys.RETURN)

time.sleep(10)

historical_data = driver.find_element_by_xpath('//a[@href="/quote/FB/history?p=FB"]').click()

time.sleep(4)

date_picker = driver.find_element_by_xpath('//div[@class="M(0) O(n):f D(ib) Bd(0) dateRangeBtn O(n):f"]').click()

time.sleep(3)

day_period = driver.find_element_by_xpath('//button[@data-value="1_D"]').click()

time.sleep(3)

submit = driver.find_element_by_xpath('//button[@class=" Bgc($linkColor) Bdrs(3px) Px(20px) Miw(100px) Whs(nw) Fz(s) Fw(500) C(white) Bgc($linkActiveColor):h Bd(0) D(ib) Cur(p) Td(n)  Py(9px) Fl(end)"]').click()

time.sleep(5)

download_hist_data = driver.find_element_by_xpath('//a[@download="FB.csv"]').click()







